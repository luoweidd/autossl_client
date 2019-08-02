#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : requesthandle.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/8/1
 * Time: 下午4:38
'''


from sysbase.logproduction import Logbase
import json

class requesthandle(object):

    __doc__ = '''
        消息格式：
                {【heard】：root,【msg】：‘法师法’}
                heard：最终会被程序识别为消息处理路由或处理方法。
                msg：我们最终奥传输的数据，可以是任意格式或数据类型，由使用者自己处理
              '''

    _heard = {}



    def __init__(self,data):
        self.request = data
        self.heard =None
        self.msg = None
        self.log = Logbase.logger

    def handle(self):
        try:
            self.log.info(self.request)
            data = json.loads(self.request)
            if type(data) == dict:
                heard = data["heard"]
                messgae = data["msg"]
                return self.controllerout(messgae,heard)
            else:
                return "{'error':'非法消息'}"
        except Exception:
            return "{'error':'非法消息'}"


    def controllerout(self,data,route_flag):
        '''

        :param route_flag: type:<str>
        :return:
        '''
        if hasattr(self._heard,route_flag):
            return map(self._heard["route_flag"](data),route_flag)
        return self.messgesformat({'error':'notfund'})

    def messgesformat(self,msg):
        return str(msg)

    def route(self,contrllfunc,route):
        self._heard.update(route,contrllfunc)
        def func():
            request = self.request
            return contrllfunc(request)
        return func


