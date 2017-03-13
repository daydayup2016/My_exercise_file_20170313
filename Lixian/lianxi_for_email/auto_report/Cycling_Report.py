import argparse
import os
import sys
import time
import tempfile
from src.logger import logger
from jinja2 import Environment, FileSystemLoader
from src.util import *
allplatform = ['DNV', 'BSF', 'GreenlowR', 'KNL_SRK', 'KNL_CRK']
dirdict = {'DNV':'DNV', 'BSF':'BSF', 'GreenlowR':'Greenlow-R', 'KNL_SRK':'KNL', 'KNL_CRK':'KNL-CRK'}
cur_dir= os.path.dirname(os.path.realpath(__file__))

def parse_args():
    parser = argparse.ArgumentParser(prog="Cycling Auto-send Test Reprot", description="Auto-send test result report")
    parser.add_argument('-p', '--platform', dest="PLATFORM", required=True,
                        help="The platform you want to collect and send test report, "
                             "e.g. all platform, -p all"
                             "e.g more platform is gap by : word, -p DNV:BSF")
    parser.add_argument('-w', '--reportweekly', dest="REPORTWEEKLY", help="which weekly test report, e.g. WW48")
    parser.set_defaults(func=send_email)
    return parser.parse_args()

def send_email(args):
    logger.info("input parameter is {} {}".format(args.PLATFORM, args.REPORTWEEKLY))
    if args.REPORTWEEKLY:
        weekly = args.REPORTWEEKLY
    else:
        weekly = "WW" + str(int(time.strftime("%W")) +1)
    if args.PLATFORM == "all":
        platforms = allplatform
    else:
        platforms = args.PLATFORM.split(":")
    logger.info("{} | {}".format(platforms, weekly))
    for platform in platforms:
        execlpath, emaillist = get_config(platform)
        logger.info("{} | {}".format(execlpath, emaillist))
        if execlpath:
            execlcontent = read_execl(execlpath, weekly)
            summaryinfo = analysis_reult(execlcontent)
            print summaryinfo
            template_dir = os.path.join(cur_dir, "email_template")
            mail_title = "{0} Platform {1} Cycling Test Report".format(platform, weekly)
            #mail_sender = "DCG_OBDU@intel.com"
            mail_sender = "pingpingx.wu@intel.com"
            template_file = "template.html"
            logser = r"\\ccr\ec\proj\deg\PID\BKC\Auto\ProductCyclingRecord"
            if dirdict.has_key(platform):
                print platform
                logdir = os.path.join(logser, dirdict[platform])
            else:
                logdir = logser
            print 'Generate mail content'
            res_dict = {
                "test_result_list": execlcontent,
                "log_dir": logdir,
                "summary_info": summaryinfo,
                "platform": platform,
                "weekly": weekly
                }
            env = Environment(loader=FileSystemLoader(template_dir))
            template = env.get_template(template_file)
            mail_body = template.render(res_dict)

            logger.info('Send mail to {}'.format(emaillist))
            attchment_list = []
            if os.path.exists(execlpath):
                attchment_list.append(execlpath)
            if send_mail(mail_sender, emaillist,
                         mail_title, mail_body,
                         ccs="", attachment=attchment_list):
                print 'Mail has been sent successfully'
            else:
                print 'Failed to send mail'
        else:
            logger.error("Can not found the execl file")

def main():
    args = parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
