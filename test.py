#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : test.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/8/1
 * Time: 下午3:37
'''

# coding=UTF-8
from socket import *
import sys


HOST = '127.0.0.1'
PORT = 8782
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('>')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZE).decode("UTF-8")
    if not data:
        break
    print (data.strip())
    tcpCliSock.close()