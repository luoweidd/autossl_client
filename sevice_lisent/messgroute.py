#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : messgroute.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/7/26
 * Time: 下午4:53
'''

from sysbase.logproduction import Logbase



log = Logbase.logger
routlist = {}

class messagesroute:

    def addroute(self,heard):
        '''

        :param heard: messages heard must str type: str
        :param function: 注入方法
        :return: 方法结果
        '''
        if heard not in routlist.keys():
            def routefunction(func):
                print(func.__name__)
                routlist.update({heard: func.__name__})
                return func()
            return routefunction
        else:
            assert "ERROR: '%s' message route Existing"%heard


    def getrout(self,heard):
        return routlist[heard]



