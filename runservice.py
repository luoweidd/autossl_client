#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : runservice.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/7/25
 * Time: 下午5:23
'''

from tcpservice.socketservice import tcpserver
from tcpservice.requesthandle import requesthandle,Reques
import json

req = requesthandle()

@req.route('root')
def root():
    data = Reques.request
    data = json.loads(data)
    return data["msg"]["domain"]

@req.route('good')
def good():
    data = Reques.request
    data = json.loads(data)
    return json.dumps(data["msg"])


server = tcpserver()

if __name__ == "__namin__":
    server
