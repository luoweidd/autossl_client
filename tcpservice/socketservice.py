#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : socketservice.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/7/26
 * Time: 上午9:24
'''

from sysbase.confparser import configparser
from sysbase.logproduction import Logbase
import socket,threading,os,select,queue
from tcpservice.requesthandle import requesthandle

class tcpserver:

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
        self.log.info("Service startup!")
        self.service.listen(self.backlog)

    def start(self):
        if hasattr(select,'epoll'):
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
                    socket_request = fd_to_socket[fd]
                    # 可读事件
                    if event & select.EPOLLIN:
                        # 如果活动socket为服务器所监听，有新连接
                        if socket_request == self.service:
                            con, address = self.service.accept()
                            con.setblocking(0)
                            # 注册新连接fd到待读事件集合
                            epoll.register(con.fileno(), select.EPOLLIN)
                            fd_to_socket[con.fileno()] = con
                            message_queues[con] = queue.Queue()
                            self.log.info(message_queues)
                        # 否则为客户端发送的数据
                        else:
                            data = socket_request.recv(self.buffer_size)
                            if data == '':
                                self.log.error('消息空，强制关闭链接！')
                                epoll.unregister(con)
                                fd_to_socket[con.fileno()].close()
                            else:
                                message_queues[socket_request].put(data)
                                # 修改读取到消息的连接到等待写事件集合
                                epoll.modify(fd, select.EPOLLOUT)
                    # 可写事件
                    elif event & select.EPOLLOUT:
                        try:
                            request = message_queues[socket_request].get_nowait()
                            handle = requesthandle(request)
                            result = handle.handle()
                            socket_request.send(result.encode('utf-8'))
                            self.log.info('返回 ——》%s'%result)
                        except queue.Empty as e:
                            epoll.modify(fd, select.EPOLLIN)
                    # 关闭事件
                    elif event & select.EPOLLHUP:
                        epoll.unregister(fd)
                        fd_to_socket[fd].close()
                        del fd_to_socket[fd]
        elif hasattr(select,'select'):
            inputs = [self.service, ]
            while True:
                rlist, wlist, xlist = select.select(inputs, [], [])
                for socket_request in rlist:
                    if socket_request == self.service:
                        con, address = self.service.accept()
                        inputs.append(con)
                    else:
                        data = socket_request.recv(self.buffer_size)
                        if data:
                            socket_request.send(data)
                            inputs.remove(socket_request)
                            socket_request.close()

