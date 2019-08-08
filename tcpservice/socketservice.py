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
from sysbase.basetools import systemtools
import socket,threading,os,select,queue
from tcpservice.requesthandle import requesthandle,Reques

class tcpserver:

    def __init__(self):
        _config_set = configparser()
        _listen_set = _config_set.confparser()
        self.host = _listen_set["lisent"]["host"]
        self.prot = _listen_set["lisent"]["port"]
        self.log = Logbase.logger
        self.service = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.service.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.service.bind((self.host,self.prot))
        self.backlog = _listen_set["lisent"]["maxconnect"]
        self.service.listen(self.backlog)
        self.log.info("Service startup!")
        self.log.info("lisent port: %s:%s"%(self.host,self.prot))
        self.log.info("maxconnect: %d"%self.backlog)
        self.logout = systemtools()

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
                            con.setblocking(False)
                            # 注册新连接fd到待读事件集合
                            epoll.register(con.fileno(), select.EPOLLIN)
                            fd_to_socket[con.fileno()] = con
                            message_queues[con] = queue.Queue()
                            self.log.info("%s:%s —— 已连接"%(address[0],address[1]))
                        # 否则为客户端发送的数据
                        else:
                            try:
                                heard = socket_request.recv(20)
                                # self.log.info(heard)
                                if heard == b'':
                                    epoll.unregister(fd)
                                    fd_to_socket[fd].close()
                                    self.log.error('消息空，强制关闭链接！,或客户端断开链接！')
                                else:
                                    data_size = int(heard.hex(),16)
                                    recv_size = 0
                                    full_data = b''
                                    while recv_size < data_size:
                                        data = socket_request.recv(1024)
                                        full_data += data
                                        recv_size += len(data)
                                    # full_data = full_data[20::]
                                    message_queues[socket_request].put(full_data)
                                    epoll.modify(fd,select.EPOLLOUT)
                            except Exception as e:
                                if e is object:
                                    for i in e:
                                        self.log.error(i)
                                    else:
                                        self.log.error(e)
                                message_queues[con].empty()
                                epoll.modify(fd,select.EPOLLHUP)
                                self.log.debug("%s:%s —— 链接已断开"%(address[0],address[1]))

                    # 可写事件
                    elif event & select.EPOLLOUT:
                        try:
                            data = message_queues[socket_request].get_nowait()
                            Reques.request =data
                            handle = requesthandle()
                            result = handle.handle()
                            socket_request.send(result.encode('utf-8'))
                            self.log.info('返回 ——》%s'%(result))
                        except queue.Empty as e:
                            epoll.modify(fd,select.EPOLLIN)
                            #队列内无消息，重回新连接等待中
                        except Exception as e:
                            epoll.modify(fd,select.EPOLLHUP)
                            self.log.error(e)
                            self.log.debug("%s:%s —— 链接已断开" % (address[0], address[1]))
                    # 关闭事件
                    elif event & select.EPOLLHUP:
                        epoll.unregister(fd)
                        fd_to_socket[fd].close()
                        del fd_to_socket[fd]
        elif hasattr(select,'select'):
            while True:
                inputs = [self.service, ]
                rlist, wlist, xlist = select.select(inputs, [], [])
                for socket_request in rlist:
                    if socket_request == self.service:
                        con, address = self.service.accept()
                        inputs.append(con)
                    else:
                        try:
                            heard = socket_request.recv(20)
                            self.log.info(heard)
                            if heard == b'':
                                inputs.remove(socket_request)
                                socket_request.close()
                                self.log.error('消息空，强制关闭链接！,或客户端断开链接！')
                            else:
                                data_size = int(heard.hex(), 16)
                                recv_size = 0
                                full_data = b''
                                while recv_size < data_size:
                                    data = socket_request.recv(1024)
                                    full_data += data
                                    recv_size += len(data)
                                # full_data = full_data[20::]
                                socket_request.send(full_data)
                        except Exception as e:
                            if e is object:
                                for i in e:
                                    self.log.error(i)
                                else:
                                    self.log.error(e)
                            inputs.remove(socket_request)
                            socket_request.close()
                            self.log.debug("%s:%s —— 链接已断开" % (address[0], address[1]))


