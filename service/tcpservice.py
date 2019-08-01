#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : tcpservice.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/8/1
 * Time: 下午3:29
'''

from socketserver import TCPServer,ThreadingMixIn,ThreadingUnixDatagramServer,\
    ThreadingTCPServer,ForkingTCPServer,StreamRequestHandler,BaseRequestHandler\
    ,UnixDatagramServer
from time import ctime


HOST = '0.0.0.0'
PORT = 8782
ADDR = (HOST,PORT)
class AUTOSSL_CLIENT_SERIVER(TCPServer,ThreadingMixIn):
    pass

class requesthandle(StreamRequestHandler):
    def handle(self):
        print("链接已建立！",self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline().decode("UTF-8"))).encode("UTF-8"))
        while True:
            data = self.request.recv(1024)
            print(data)

def start_service():
    tcpservice = AUTOSSL_CLIENT_SERIVER(ADDR,requesthandle)
    print('等待新的链接……')
    tcpservice.serve_forever()
    print(tcpservice.get_request())

start_service()