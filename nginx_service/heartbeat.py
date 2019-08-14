#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : heartbeat.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/8/6
 * Time: 上午9:15
'''

class heartbeats:

    def heartbeat_check(self,data):
        try:
            msg = data["msg"]
            if msg != None and msg != '':
                if msg["check"] == "On-line":
                    return {"msg":{"check":"On"}}
                else:
                    return {"error":"无法识别的消息"}
            else:
                return {"error":"消息内容为空"}
        except Exception:
            return {"error": "无法识别的消息"}