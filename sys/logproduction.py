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

import logging,os

class Logbase:

    logfilename = './logs/ssl_apply.log'

    if not os.path.exists('logs'):
        os.makedirs("logs",mode=0o777)
    else:
        if not os.path.exists(logfilename):
            f = open(logfilename, 'w+')
            f.close()

    logger = logging.getLogger("lw-ghy-acme")
    logger.setLevel('DEBUG')
    BASIC_FORMAT = "%(asctime)-15s [%(funcName)s] %(lineno)d -- %(message)s"
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
    chlr = logging.StreamHandler()  # 输出到控制台的handler
    chlr.setFormatter(formatter)
    # chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level
    fhlr = logging.FileHandler(logfilename)  # 输出到文件的handler
    fhlr.setFormatter(formatter)
    logger.addHandler(chlr)
    logger.addHandler(fhlr)