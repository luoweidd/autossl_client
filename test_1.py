#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : test_1.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/7/26
 * Time: 下午4:23
'''

import socket,threading,sys

def recv():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8782
    try:
        client.connect(('127.0.0.1', 8782))
    except Exception as e:
        print(e)
        sys.exit(0)
    while True:
        try:
            data =  client.recv(1024)
            if data != b'':
                print(data.decode('utf-8'))
            else:
                print('\n服务连接断开！')
                client.close()
        except OSError as ea:
            print('断线重连……')
            reconnect()
            sys.exit(1)
        except OSError as e:
            print(e)
            sys.exit(0)

def send():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8782
    try:
        client.connect(('127.0.0.1', 8782))
    except Exception as e:
        print(e)
        sys.exit(0)
    while True:
        msg = input('请输入消息内容：\n')
        if msg != None and msg != b'':
            try:
                client.send(msg.encode('utf-8'))
            except OSError as ea:
                print('断线重连……')
                sys.exit(1)
                reconnect()
            except OSError as e:
                print(e)
                sys.exit(0)

def heartbeat():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8782
    try:
        client.connect(('127.0.0.1', 8782))
    except Exception as e:
        print(e)
        sys.exit(0)
    while True:
        import time
        time.sleep(10)
        try:
            msg = b'0x01'
            client.sendall(msg)
        except OSError as ea:
            print('断线重连……')
            reconnect()
        except Exception as e:
            print(e)
            sys.exit(0)

def reconnect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8782
    try:
        client.connect(('127.0.0.1', 8782))
    except Exception as e:
        print(e)
        sys.exit(0)
    for i in range(0,3):
        try:
            client.close()
            import time
            time.sleep(3)
            client.connect((host,port))
        except Exception as e:
            print(e)
    else:
        print('重连失败！')
        sys.exit(0)

t1=threading.Thread(target=send)
t2=threading.Thread(target=recv)
t3=threading.Thread(target=heartbeat)
t2.start()
t1.start()
t3.daemon='heartbeat'
t3.start()