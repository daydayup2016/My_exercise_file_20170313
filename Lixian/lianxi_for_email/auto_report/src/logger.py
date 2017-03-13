__author__ = 'zshen11'

import logging
import os
import time
format_dict = {
    "DEBUG": logging.Formatter('%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s'),
    "INFO": logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'),
    "WARNING": logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'),
    "ERROR": logging.Formatter('%(asctime)s %(name)s %(funcName)s %(levelname)s %(message)s'),
    "CRITICAL": logging.Formatter('%(asctime)s %(name)s %(funcName)s %(levelname)s %(message)s')
}

class Logger():

    __cur_logger = logging.getLogger()

    def __init__(self, loglevel):
        new_logger = logging.getLogger(__name__)
        new_logger.setLevel(logging.DEBUG)
        #create handle for stdout
        streamhandler = logging.StreamHandler()
        logname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..\\cycling_report.log")
        filehandler = logging.FileHandler(logname)
        formatter = format_dict[loglevel]
        streamhandler.setFormatter(formatter)
        filehandler.setFormatter(formatter)
        #add handle to new_logger
        new_logger.addHandler(streamhandler)
        new_logger.addHandler(filehandler)

        Logger.__cur_logger = new_logger

    @classmethod
    def getlogger(cls):
        return cls.__cur_logger

logger = Logger('DEBUG').getlogger()

