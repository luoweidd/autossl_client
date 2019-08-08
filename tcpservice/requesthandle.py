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
from sysbase.basetools import systemtools
import json

class Reques:

    request = None

class requesthandle():

    __doc__ = '''
        消息格式：
                格式必须为json格式。
                {【heard】：root,【msg】：‘法师法’}
                必要字段：heard：最终会被程序识别为消息处理路由或处理方法。 
                必要字段：msg：我们最终奥传输的数据，可以是任意格式或数据类型，由使用者自己处理
                其余需要自定义处理字段必须全部放在msg字段中。
              '''


    def __init__(self):
        self.log = Logbase.logger
        self.sysbase = systemtools()
    respons = {"ok": "处理成功"}
    heards = {}
    req_messga = None

    def route(self,heard):
        if heard not in self.heards:
            def func(routefunc):
                self.heards.update({heard:routefunc})
            return func
        else:
            assert '"%s" Routing already exists! '

    def handle(self):
        try:
            self.log.info(Reques.request)
            data = json.loads(Reques.request)
            if type(data) is dict:
                heard = data["heard"]
                if heard not in self.heards:
                    return "{'error','nofund'}"
                else:
                    resutl = self.heards[heard]()
                    return resutl
            else:
                return "{'error':'非法消息'}"
        except Exception as e :
            # self.log.error(e)
            return "{'error':'非法消息'}"



    def messgesformat(self,msg):
        return str(msg)



