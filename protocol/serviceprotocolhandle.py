#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : serviceprotocolhandle.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/8/1
 * Time: 上午11:40
'''

class protocolhandle:

    def __init__(self,protocol):
        self.protocol = protocol


    def protocolhandle(self,proctocol_func,msg):
        def proctocol():
            protocolmsg = msg
            return map(proctocol_func,protocolmsg)
        return proctocol