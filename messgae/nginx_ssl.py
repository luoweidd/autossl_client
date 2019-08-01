#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : nginx_ssl.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/8/1
 * Time: 上午10:40
'''

class nginx_ssl_conf:

    def __init__(self,old_domain,domain,ca_key,privet_key):
        self.old_domain = old_domain
        self.conf_path = ''
        self.conf_back_path = ''
        self.domian = domain
        self.ca_key = ca_key
        self.privet_key = privet_key
        self.key_path_dir = ''

    def restartnignx(self):
        pass

    def reloadnginx(self):
        pass

    def loadnginxconf(self):
        pass

    def findnginxpath(self):
        pass