# urs/bin/python
# encoding:utf-8

import os
from src.base.baseTime import BaseTime

_path = "/Users/apple/autoTest/elk_tmp/logstash/data/" + BaseTime.current_data_file() +".csv"

'''记录记录，使用elk'''
class LogAction():

    def save(self, func, status="success", explain="null",version="744"):
        print("log_time=%s,func=%s,status=%s,explain=%s,version=%s"  %(BaseTime.get_current_time(), func, status,explain,version))
        # msg = "log_time=%s,func=%s,status=%s,explain=%s,version=%s"  %(BaseTime.get_current_time(), func, status,explain,version)
        msg = "%s,%s,%s,%s,%s"  %(BaseTime.get_current_time(), func, status,explain,version)
        print(_path)
        # 去除前后空格
        with open(_path.lstrip(" ").rstrip(" "),'a+') as fn:
            fn.write(msg+'\n')

LogAction=LogAction()


if __name__ == '__main__':
    LogAction.save(func = "testCase01", status="Fail", explain="run error")