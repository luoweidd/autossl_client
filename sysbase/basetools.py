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

import os,platform,subprocess,re


class timeformat:
    pass

class systemtools:

    def basepath(self):
        return os.getcwd()

    def os_type(self):
        return platform.system()

    def osdircutflag(self):
        ostype = self.os_type()
        if ostype == 'Windows':
            return '\\'
        else:
            return '/'

    def dirflagformat(self,path):
        if self.os_type() == "Windows":
            if re.match('^[C-Z,c-z]:\\\*',path):
                return path
            elif re.match('^\./',path):
                path = re.sub('./','',path)
                win_configpath = path.replace('/',self.osdircutflag)
                configabsolutepath = '%s%s%s'%(self.basepath(),self.osdircutflag(),win_configpath)
                return configabsolutepath
            else:
                win_configpath = path.replace('/',self.osdircutflag)
                configabsolutepath = '%s%s%s'%(self.basepath(),self.osdircutflag(),win_configpath)
                return configabsolutepath
        else:
            if re.match('^/',path):
                return path
            elif re.match('^\./',path):
                path = re.sub('./', '', path)
                configabsolutepath = '%s%s%s' % (self.basepath(), self.osdircutflag(), path)
                return configabsolutepath
            else:
                configabsolutepath = '%s%s%s'%(self.basepath(),self.osdircutflag(),path)
                return configabsolutepath

    def CMD(self,command, check_name=None):
        checkresult = subprocess.getstatusoutput('%s %s' % (command, check_name))
        return checkresult