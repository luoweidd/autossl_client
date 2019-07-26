#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : basetools.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/7/25
 * Time: 下午5:32
'''

import os,platform,subprocess


class timeformat:
    pass

class systemtools:

    @staticmethod
    def basepath():
        return os.getcwd()

    @staticmethod
    def osdircatflag():
        if platform.system() == 'Windows':
            return '\\'
        else:
            return '/'

    @staticmethod
    def CMD(command, check_name=None):
        checkresult = subprocess.getstatusoutput('%s %s' % (command, check_name))
        return checkresult