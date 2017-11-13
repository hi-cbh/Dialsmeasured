# urs/bin/python
# encoding:utf-8
import datetime
import os,time,unittest,sys
import configparser as cparser
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseTime import BaseTime

from src.psam.psam import Psam
from src.testcase.v722.easycase.login import Login

from src.base.baseImage import BaseImage

# sys.path.append(r"/Users/apple/git/pytest/")







class DataTest(object):

    def __init__(self):
        pass

    # 每天晚上8点后，返回更改的时间戳
    def getTestData(self):
        return BaseTime.getCurrentTime()

    def getCode(self):

        i = datetime.datetime.now()
        print ("当前的日期和时间是 %s" % i)
        print ("ISO格式的日期和时间是 %s" % i.isoformat() )
        print ("当前的年份是 %s" %i.year)
        print ("当前的月份是 %s" %i.month)
        print ("当前的日期是  %s" %i.day)
        print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
        print ("当前小时是 %s" %i.hour)
        print ("当前分钟是 %s" %i.minute)
        print ("当前秒是  %s" %i.second)

        i = datetime.datetime.now()

        h = i.hour
        d = i.day
        if int(h) >= 20:
            d = d+1

        name = str(i.year) +str(i.month) + str(d)
        print(name)



DataTest().getCode()