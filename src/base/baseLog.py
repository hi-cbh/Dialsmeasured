# urs/bin/python
# encoding:utf-8

import os
from src.base.baseTime import BaseTime


'''记录记录，使用elk'''
class LogAction():

    def save(self, func, status="success", explain="null"):
        print("log_time=%s, func=%s, status=%s, explain=%s"  %(BaseTime.get_current_time(), func, status,explain))


LogAction=LogAction()


if __name__ == '__main__':
    LogAction.save(func = "testCase01", status="Fail", explain="用例1错误")