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

import os,platform,subprocess,re,logging,uuid,time
from urllib import request
# from sysbase.logproduction import Logbase


logger = logging.getLogger("lw-ghy-acme")

class timeformat:
    pass

class systemtools:


    def basepath(self):
        '''
        获取当前路径
        :return:
        '''
        return os.getcwd()

    def os_type(self):
        '''
        系统内省判断
        :return:
        '''
        return platform.system()

    def osdircutflag(self):
        '''
        系统目录路径分隔符
        :return:
        '''
        ostype = self.os_type()
        if ostype == 'Windows':
            return '\\'
        else:
            return '/'

    def dirflagformat(self,path):
        '''
        传入路径根据系统类型重新组合
        :param path:
        :return:
        '''
        if self.os_type() == "Windows":
            if re.match('^[C-Z,c-z]:\\\*',path):
                return path
            elif re.match('^\./',path):
                path = re.sub('./','',path)
                win_configpath = path.replace('/',self.osdircutflag())
                configabsolutepath = '%s%s%s'%(self.basepath(),self.osdircutflag(),win_configpath)
                return configabsolutepath
            else:
                win_configpath = path.replace('/',self.osdircutflag())
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
        '''
        系统命令组装
        :param command:
        :param check_name:
        :return:
        '''
        checkresult = subprocess.getstatusoutput('%s %s' % (command, check_name))
        return checkresult

    def readlinefile(self,configabsolutepath):
        '''
        只读文件模式
        :param configabsolutepath:
        :return:
        '''
        try:
            with open(configabsolutepath,'r')as f:
                data = f.readlines()
                return data
        except Exception as e:
            self.osdircutflag(e)
            return 'error'

    def readallfile(self,configabsolutepath):
        '''
        只读文件模式
        :param configabsolutepath:
        :return:
        '''
        try:
            with open(configabsolutepath,'r')as f:
                data = f.read()
                return data
        except Exception as e:
            self.osdircutflag(e)
            return 'error'

    def logoutput(self,error):
        '''
        日志输出
        :param error:
        :return:
        '''
        if error is object:
            for i in error:
                logger.error(i)
        else:
            logger.error(error)

    def get_dir_list(self,path):
        '''
        目录内内容名称列表
        :param path:
        :return:
        '''
        return os.listdir(path)

    def dir_path_check(self,dir):
        '''
        目录是否纯在检测，如果不存在则新建。
        :param dir:
        :return:
        '''
        if os.path.exists(dir):
            return True
        else:
            flag = self.osdircutflag()
            dir_list = dir.split(flag)
            path_tmp = ''
            for i in dir_list:
                if self.os_type() != 'Windows':
                    path_tmp += flag+i
                    if os.path.exists(path_tmp) is False:
                        os.makedirs(path_tmp[1:],0o755)
                        print('创建目录：%s' % path_tmp)
                        return True
                else:
                    path_tmp += i+flag
                    if os.path.exists(path_tmp) is False:
                        os.makedirs(path_tmp,0o755)
                        print('创建目录：%s'%path_tmp[1:])
                        return True

    def new_write_file(self,absolutepath,data):
        '''
        新写入文件，覆盖原有内容
        :param absolutepath:
        :param data:
        :return:
        '''
        try:
            with open(absolutepath,'w')as f:
                f.write(data)
                return True
        except Exception as  e:
            self.logoutput(e)
            return False

    def url_extract_doain(self,url):
        '''
        Getting domain name in URL
        :param url: url <type>: str
        :return: domain name <type>: str
        '''
        if re.match('^http://', url):
            domain = re.sub('^http://', '', url)
            domain = domain.split('/')[0]
            return domain
        elif re.match('^https://', url):
            domain = re.sub('https://', '', url)
            domain = domain.split('/')[0]
            return domain
        else:
            return url

    def getDomain(self,domain):
        '''
        Getting top-level domain names
        :param domain:  domain <type>:str
        :return: top-level domain names <type>:str
        '''
        root_doamin = [".com.cn", ".edu.cn", ".net.cn", ".org.cn", ".co.jp", ".gov.cn", ".co.uk", "ac.cn", ".com",
                       ".cn",
                       ".gov", ".net", ".edu", ".tv", ".info", ".ac", ".ag", ".am", ".at", ".be", ".biz", ".bz", ".cc",
                       ".de",
                       ".es", ".eu", ".fm", ".gs", ".hk", ".in", ".info", ".io", ".it", ".jp", ".la", ".md", ".ms",
                       ".name", ".nl",
                       ".nu", ".org", ".pl", ".ru", ".sc", ".se", ".sg", ".sh", ".tc", ".tk", ".tv", ".tw", ".us",
                       ".co", ".uk",
                       ".vc", ".vg", ".ws", ".il", ".li", ".nz"]
        for root in root_doamin:
            regex = re.compile(r'[0-9a-zA-Z_-]+' + root + '$')
            m = regex.findall(domain)
            if len(m) > 0:
                return m[0]

    def hex_time_uuid(self):
        return uuid.uuid5(uuid.NAMESPACE_DNS,time.time().hex())