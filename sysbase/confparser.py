#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : confparser.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/7/25
 * Time: 下午5:30
'''

from sysbase.basetools import systemtools
import yaml

class configparser:

    def __init__(self):
        sys_tools = systemtools()
        self.config_path = "conf/client.yml"
        self.configabsolutepath = sys_tools.dirflagformat(self.config_path)

    def readconfig(self):
        with open(self.configabsolutepath,'r')as f:
            data = f.read()
        return data

    def confparser(self):
        return yaml.safe_load(self.readconfig())