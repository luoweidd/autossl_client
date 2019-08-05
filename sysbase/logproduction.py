#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : logproduction.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/7/25
 * Time: 下午5:28
'''

import logging,os,datetime
from logging import handlers
from sysbase.confparser import configparser
from sysbase.basetools import systemtools
class Logbase:

    config_obj = configparser()
    config_set = config_obj.confparser()
    sys_toosl = systemtools()
    logfile = config_set["log"]["PATH"]
    logfilename = sys_toosl.dirflagformat(logfile)
    backup_Count = config_set["log"]["backup_Count"]
    max_cut = config_set["log"]["max_cut"]
    if not os.path.exists('logs'):
        os.makedirs("logs",mode=0o777)
    else:
        if not os.path.exists(logfilename):
            f = open(logfilename, 'w+')
            f.close()

    logger = logging.getLogger("lw-ghy-acme")
    logger.setLevel('DEBUG')
    BASIC_FORMAT = config_set["log"]["FORMAT"]
    DATE_FORMAT = config_set["log"]["ASCTIME_FORMAT"]
    formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
    chlr = logging.StreamHandler()  # 输出到控制台的handler
    chlr.setFormatter(formatter)
    # chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level
    fhlr = logging.FileHandler(logfilename)# 输出到文件的handler
    fhlr.setFormatter(formatter)#日子格式handler
    sizecut = logging.handlers.RotatingFileHandler(filename=logfilename,mode=0o777,maxBytes=10240*max_cut,backupCount=backup_Count)
    datacut = logging.handlers.TimedRotatingFileHandler(filename=logfilename, when='D', interval=1, backupCount=backup_Count, atTime=datetime.time(0, 0, 0, 0))
    logger.addHandler(chlr)
    logger.addHandler(fhlr)
    logger.addHandler(sizecut)
    logger.addHandler(datacut)