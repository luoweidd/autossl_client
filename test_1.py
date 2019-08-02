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


def clientconnect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8782
    try:
        client.connect(('127.0.0.1', 8782))
        return client,host,port
    except Exception as e:
        print(e)
        sys.exit(0)

def recv(client,host,port):
    while True:
        try:
            data =  client.recv(10240)
            if data != b'':
                print('\n接收到新消息：“%s”'%data.decode('utf-8'))
            else:
                print('\n服务连接断开！')
                client.close()
        except OSError as ea:
            client.close()
            print('断线重连……')
            reconnect(client,host,port)
            sys.exit(1)
        except OSError as e:
            print(e)
            sys.exit(1)

def send(client,host,port):
    while True:
        msg = input('请输入：')
        if msg != None and msg != b'':
            try:
                client.sendall(msg.encode('utf-8'))
            except OSError as ea:
                client.close()
                print('断线重连……')
                sys.exit(1)
                reconnect(client,host,port)
            except OSError as e:
                print(e)
                sys.exit(1)

def heartbeat(client,host,port):
    while True:
        import time
        time.sleep(10)
        try:
            msg = b'0x01'
            client.send(msg)
        except OSError as ea:
            client.close()
            print('断线重连……')
            reconnect(client,host,port)
        # except Exception as e:
        #     print(e)
        #     sys.exit(0)

def reconnect(client,host,port):
    for i in range(0,3):
        # try:
        import time
        time.sleep(3)
        client.connect((host,port))
        # except Exception as e:
        #     print(e)
    else:
        print('重连失败！')
        sys.exit(1)
if __name__ == '__main__':
    client = clientconnect()
    t1=threading.Thread(target=send,args=client,)
    t2=threading.Thread(target=recv,args=client)
    # t3=threading.Thread(target=heartbeat,args=client)
    t2.start()
    t1.start()
    # t3.start()