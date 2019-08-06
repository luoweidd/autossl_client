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
from nginx_service.heartbeat import heartbeats
from nginx_service.nginxoperation import nginxperation
import json

req = requesthandle()

@req.route('nginx_ssl')
def root():
    data = Reques.request
    data = json.loads(data)
    # ngop = nginxperation()
    return data["msg"]["domain"]

@req.route('good')
def good():
    data = Reques.request
    data = json.loads(data)
    return json.dumps(data["msg"])

@req.route('heartbeat')
def heartbeat():
    data = Reques.request
    data = json.loads(data)
    hb = heartbeats()
    result = hb.heartbeat_check(data)
    return json.dumps(result)


server = tcpserver()

if __name__ == "__namin__":
    server
