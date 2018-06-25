# urs/bin/python
# encoding:utf-8

import os
from src.base.baseTime import BaseTime

_path = "/Users/apple/autoTest/elk_tmp/logstash/data/" + BaseTime.current_data_file() +".csv"

'''记录记录，使用elk'''
class LogAction():

    def __init__(self):
        self.s = ""

    def save(self, func, status="success", explain="null",version="746"):
        print("log_time=%s,func=%s,status=%s,explain=%s,version=%s"  %(BaseTime.get_current_time(), func, status,explain,version))
        msg = "%s,%s,%s,%s,%s"  %(BaseTime.get_current_time(), func, status,explain,version)
        print(_path)
        print(msg)
        # 去除前后空格
        with open(_path.lstrip(" ").rstrip(" "),'a+') as fn:
            fn.write(msg+'\n')

    def print(self, str="", isReset= False):
        print(str)
        if(isReset):
            self.s = ""
        else:
            self.s=self.s + str
        return self.s


LogAction=LogAction()


if __name__ == '__main__':
    LogAction.print("123")
    LogAction.print("123")
    LogAction.print("123")
    print(LogAction.print(""))