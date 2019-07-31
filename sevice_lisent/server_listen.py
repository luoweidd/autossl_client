#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : server_listen.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/7/26
 * Time: 上午9:24
'''

from sysbase.confparser import configparser
from sysbase.logproduction import Logbase
from sevice_lisent.messgroute import messagesroute
import socket,threading,os,select,queue

class TCPlisten:

    def __init__(self):
        _config_set = configparser()
        _listen_set = _config_set.confparser()
        self.host = _listen_set["lisent"]["host"]
        self.prot = _listen_set["lisent"]["port"]
        self.service = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.service.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.backlog = _listen_set["lisent"]["maxconnect"]
        self.service.bind((self.host,self.prot))
        self.buffer_size = _listen_set["lisent"]["buffer_size"]
        self.log = Logbase.logger

    def server_start(self):
        self.log.info("Service startup!")
        self.service.listen(self.backlog)
        # 新建epoll事件对象，后续要监控的事件添加到其中
        epoll = select.epoll()
        # 添加服务器监听fd到等待读事件集合
        epoll.register(self.service.fileno(), select.EPOLLIN)
        message_queues = {}
        fd_to_socket = {self.service.fileno(): self.service, }
        while True:
            # 轮询注册的事件集合
            events = epoll.poll()
            if not events:
                continue
            for fd, event in events:
                socket = fd_to_socket[fd]
                # 可读事件
                if event & select.EPOLLIN:
                    # 如果活动socket为服务器所监听，有新连接
                    if socket == self.service:
                        con, address = self.service.accept()
                        con.setblocking(0)
                        # 注册新连接fd到待读事件集合
                        epoll.register(con.fileno(), select.EPOLLIN)
                        fd_to_socket[con.fileno()] = con
                        message_queues[con] = queue.Queue()
                    # 否则为客户端发送的数据
                    else:
                        data = socket.recv(1024)
                        if data:
                            message_queues[socket].put(data)
                            # 修改读取到消息的连接到等待写事件集合
                            epoll.modify(fd, select.EPOLLOUT)
                # 可写事件
                elif event & select.EPOLLOUT:
                    try:
                        msg = message_queues[socket].get_nowait()
                    except queue.Empty:
                        epoll.modify(fd, select.EPOLLIN)
                        socket.send(msg)
                    else:
                        socket.send(msg)
                # 关闭事件
                elif event & select.EPOLLHUP:
                    epoll.unregister(fd)
                    fd_to_socket[fd].close()
                    del fd_to_socket[fd]


    def server_stop(self):
        self.service.close()

    def tcplink(self,con,address):
        while True:
            data = con.recv(self.buffer_size)
            msgclass = messagesroute()
            data = eval(data.decode("utf-8"))
            if data != 1:
                if type(data) == dict:
                    resultmsg = msgclass.getrout('heard')
                    print(resultmsg)
                    if resultmsg != None and resultmsg != '':
                        self.tcpsend(con,address,resultmsg)
                else:
                    self.tcpsend(con,address,'ERROR: 非法消息！\n')
            else:
                self.tcpsend(con,address,'online……')

    def tcpsend(self,con,address,data):
        while True:
            if data != None and data != b'':
                try:
                    self.log.info('send [%s] -> %s:%s'%(data,address[0],address[1]))
                    con.send(data.encode('utf-8'))
                except Exception as e:
                    if e is object:
                        for i in e:
                            self.log.error(i)
                            con.close()
                    else:
                        self.log.error(e)
                        con.close()
