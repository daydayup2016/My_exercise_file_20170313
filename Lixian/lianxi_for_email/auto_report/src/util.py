# encoding=utf-8

import platform
import subprocess
import signal
import time
import os
import copy
import ConfigParser
import csv
import logging
import re
import tempfile
import sys
import smtplib
import xlrd
import mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
from email.Utils import COMMASPACE
from email.mime.application import MIMEApplication
from ConfigParser import ConfigParser
from src.logger import logger

def get_info(info_file, section_name, var_name):
    info = "UNKNOWN"
    if os.path.isfile(info_file):
        try:
            config_ver = ConfigParser()
            config_ver.read(info_file)
            info = config_ver.get(section_name, var_name)
        except Exception as err:
            print "[Warning]:Unknown info : {0}".format(var_name)
            print sys.exc_info()[1]
    
    return info

class TimeoutError(Exception):
    pass

def command(cmd, log_file, log_dir, timeout=600):
    """Run command and return the output
    cmd - the command to run
    timeout - max seconds to wait for
    log_dir - log folder also for record
    """
    is_linux = platform.system() == 'Linux'
    print "cmd = ", cmd

    os.environ.update({'LC_RESULT_PATH': '%s'%log_dir})
    p = subprocess.Popen(cmd,
                         stderr=subprocess.STDOUT,
                         stdout=subprocess.PIPE,
                         shell=True,
                         preexec_fn=os.setsid if is_linux else None)

    t_beginning = time.time()
    t_ending = t_beginning + float(timeout)
    f_timeout = False

    try:
        with open(log_file, "ab") as log_des:
            while p.poll() is None:
                buff = p.stdout.readline()
                log_des.write(buff)
                print buff.rstrip()
                if timeout and time.time() > t_ending:
                    log_des.write("{0}{1}Timeout after testing: {2} seconds{1}{0}{1}".format("*"*10, os.linesep, timeout))
                    f_timeout = True
                    break
    except Exception as err:
        print "[ERROR:]Run process error"
        print sys.exc_info()[1]

    if f_timeout:
        if is_linux:
            os.killpg(p.pid, signal.SIGTERM)
        else:
            os.system("TASKKILL /F /T /PID {pid}".format(pid=p.pid))
        raise TimeoutError("{0} running longer than {1}".format(cmd, timeout))
    with open(log_file, "ab") as log_des:
        log_des.write("{0}{1}return code:{2}{1}{0}{1}".format("*"*10, os.linesep, p.returncode))
    return p.returncode

def send_mail(sender, receivers, subject='', content='', ccs=[], bccs=[], attachment=[]):
    try:
        print "Sending Email"
        # All receivers
        all_recvs = []
        all_recvs.extend(receivers)
        all_recvs.extend(ccs)
        all_recvs.extend(bccs)

        msg = MIMEMultipart()
        msg.attach(MIMEText(content, 'html', 'utf-8'))
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = COMMASPACE.join(receivers)
        print msg['To']
        msg['Cc'] = COMMASPACE.join(ccs)

        for att in attachment:
            part = MIMEApplication(open(att, "rb").read())
            part.add_header("Content-Disposition",
                        "attachment",
                        filename=os.path.basename(att))
            msg.attach(part)

        server = smtplib.SMTP('mail.intel.com')
        server.sendmail(sender, all_recvs, msg.as_string())

        print "Email sent out"
        server.quit()

    except Exception as err:
        print "[ERROR:]{0}".format(str(err))
        print sys.exc_info()[1]
        return False
    return True

def copy_dir(path, dest, log_file=None, move=False):
    """Copy directory using robocopy"""
    dest = re.sub(r'([^\\])(\\+)$', r'\1', dest)  # robocopy did not accept directory end with '\'

    logging.info('Copy %s to %s' % (path, dest))

    if log_file:
        command = 'robocopy "%s" "%s" /mt /e /is >> "%s"' % (path, dest, log_file)
    else:
        command = 'robocopy "%s" "%s" /mt /e /is' % (path, dest)

    logging.debug('Command %s' % command)

    ret = os.system(command)
    if ret <= 3:
        logging.info('Direcotry copied successfully')
    else:
        logging.error('Failed to copy %s. Error code %d' % (path, ret))
        raise Exception('Failed to copy %s. Error code %d' % (path, ret))

    if move:
        logging.info("Delete directory %s" % path)
        cmd = 'rmdir /S /Q "%s"' % path
        os.system(cmd)


def check_python_ver(asking=True):
    version = sys.version_info
    major, minor, micro = version.major, version.minor, version.micro
    if major != 2:
        print "[Error:]Current Python version is ( %d.%d.%d ). Acutally need version 2.7.xx" % (major, minor, micro)
        return 1, "[Error:]Current Python version is ( %d.%d.%d ). Acutally need version 2.7.xx" % (major, minor, micro)
    
    if minor < 7:
        if asking:
            ans = raw_input("[Warning:]We need (2.7.xx) version Python, now is (%d.%d.%d). Will you Continue?(y/n)" % (major, minor, micro))
            if str(ans).lower() == "y" or str(ans).lower() == "yes":
                print "Continue..."
                return (0,"")
        return 2, "[Warning:]We need (2.7.xx) version Python, now is (%d.%d.%d). Will you Continue?(y/n)" % (major, minor, micro)

    return (0, "")

def check_content(var_name, check_point):
    #windows os will ignore lower or upper string name of variable
    var_content = os.environ.get(var_name)
    if not var_content:
        print "[Error:]No system variable '{0}'.".format(var_name)
        print "User need add it in system variables and logoff re-login to take effect"
        return 1, "[Error:]No system variable '{0}'.".format(var_name)

    if os.pathsep in var_content:
        content = var_content.split(os.pathsep)
    else:
        content = [var_content]
    check_driver, check_dir_path = os.path.splitdrive(check_point)
    f_same = False
    for path in content:
        driver, dir_path = os.path.splitdrive(path)
        if driver.lower() == check_driver.lower() and \
            dir_path.lower() == check_dir_path.lower():
            f_same = True
            break
        
    if not f_same:
        print "[Error:]( {0} ) not in '{1}'.".format(check_point, var_name)
        print "User need add it in {0} and re-launch terminal to take effect".format(var_name)
        return 1, "[Error:]( {0} ) not in '{1}'.".format(check_point, var_name)
    
    return (0, "")

def get_config(platform):
    curpath = os.path.dirname(os.path.abspath(__file__))
    configpath = os.path.join(curpath, "..\\config\config.cfg")
    #logger.info("config file path is: {}".format(configpath))
    if os.path.exists(configpath):
        with open(configpath, "r") as fp:
            cfg = ConfigParser()#.ConfigParser()
            cfg.read(configpath)
            if cfg.has_option(platform, "execlname"):
                execlname = cfg.get(platform, "execlname")
            else:
                execlname = None
            if cfg.has_option(platform, "maillist"):
                email = cfg.get(platform, "maillist")
            else:
                email = None
            execdir = cfg.get('Defaul_Setting', 'execldir')
            emaildefault = cfg.get('Defaul_Setting', 'maillist')

            if execlname:
                execpath = os.path.join(execdir, execlname)
            else:
                execpath = None
            if email:
                emaillist = emaildefault.split(";") + email.split(";")
            else:
                emaillist = emaildefault.split(";")
        logger.info(execpath)
        logger.info(emaillist)
        return execpath, emaillist
    else:
        logger.info("config error")
        return None,None

def read_execl(execlpath, weekly):
    logger.info("will read cycling result form the execl")
    readline = ['Test Weekly', 'Board', 'BKC', 'IFWI', 'OS', 'Case Name', 'Target Cycle', 'Current Cycle', 'Status', 'Comments']
    colnum = range(1,11)
    if os.path.exists(execlpath):
        try:
            logger.info("try to open the execl file")
            workbook = xlrd.open_workbook(execlpath)
            for i in range(3):
                try:
                    content = []
                    sheet = workbook.sheet_by_index(i)
                    if sheet:
                        rows = sheet.nrows
                        cols = sheet.ncols
                        logger.info("total rows is {} | total column is {}".format(rows, cols))
                        firstrow = sheet.row_values(0)
                        logger.info(firstrow)
                        if "Report Weekly" in firstrow and "Target Cycle" in firstrow:
                            logger.info("found cycling result sheet")
                            for row in range(1,rows):
                                status = sheet.cell_value(row, 9).lower()
                                if sheet.cell_value(row,0) == weekly and ("pass" in status or "fail" in status or "cancel" in status):
                                    onerow = copy.deepcopy([])
                                    for j in colnum:
                                        if type(sheet.cell_value(row,j)) is float:
                                            onerow.append(str(int(sheet.cell_value(row,j))).encode('utf-8'))
                                        else:
                                            onerow.append(sheet.cell_value(row,j).encode('utf-8'))
                                    logger.debug(onerow)
                                    content.append(onerow)
                            return content
                        else:
                            logger.info("not found report weekly column")
                            break
                except Exception, ex:
                    logger.error(ex)
            else:
                logger.error("not found the cycling result sheet")
                return None
        except Exception,ex:
            logger.error(ex)
            return None
    else:
        logger.error("not found the execl file")
        return None

def analysis_reult(execlcontent):
    summaryinfo = []
    passnum = failnum = cancelnum = 0
    for onecycle in execlcontent:
        if "pass" in onecycle[-2].lower():
            passnum += 1
        if "fail" in onecycle[-2].lower():
            failnum += 1
        if "cancel" in onecycle[-2].lower():
            cancelnum += 1
    summaryinfo.append(len(execlcontent))
    summaryinfo.append(passnum)
    summaryinfo.append(failnum)
    summaryinfo.append(cancelnum)
    return summaryinfo


if __name__ == "__main__":
    get_config("aaa")

