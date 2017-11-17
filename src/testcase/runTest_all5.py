# urs/bin/python
# encoding:utf-8

import unittest,os,sys
import time, datetime



p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("path: %s" %p)

sys.path.append(p+"/")
localPath = "/var/appiumRunLog"
reportPath = localPath + "/report/"
# failReport = localPath + "/failReport/"
logPath = localPath + "/logs/"
iniPath = localPath + '/ini/'
print("report: %s" %reportPath)
print("report: %s" %logPath)


from src.testcase.v731.testSend import TestSend
from src.testcase.v731.testContant import TestContant
from src.testcase.v731.test139Selected import TestSelect
from src.testcase.v731.testPush import TestPush
from src.testcase.HTMLTestRunner import HTMLTestRunner
from src.testcase.v731.testLogin import TestLogin
from src.mail.sendEmailSmtp import SendMail
from src.testcase.v731.testDownFile import TestDownFile
from src.otherApk.testSpeed import TestSpeed
from src.base.baseTime import BaseTime
# from src.testcase.v722.firstLogin import InitData
# from src.base.baseAdb import BaseAdb
from src.readwriteconf.rwconf import ReadWriteConfFile

logfileName= BaseTime.getDateHour() + '.log'

'''
优化测试结果：
1、成功是每天晚上8点发送邮件。
2、失败次数达到N次后，发送邮件。

'''


if __name__ == "__main__":
    for i in range(100):
        # 获取当前网速
        ts = TestSpeed()
        ts.setUp()
        speed = ts.testCase()
        ts.tearDown()

        speed='调试中'
        print("speed: %s" %speed)
        time.sleep(10)

        print('需要运行的脚本')
        result = {}
        testtxt = {}

        result['testCaseLogin'] = 'Success'


        # 用例名 与用例说明
        testtxt['账号登录'] = 'testCaseLogin'

        suite = unittest.TestSuite()
        # suite.addTest(InitData("testCase"))
        suite.addTest(TestLogin('testCaseLogin'))

        runner = unittest.TextTestRunner()
        print('运行结束')
        # time.sleep(15)
    #
    # # 生成html
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename_now = time.strftime("%Y_%m_%d_%H_%M_%S")
    # filename = reportPath + now + '_result.html'
    # # filename = r'/Users/apple/git/pytest/report/index.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner(stream=fp,
    #                         title='Test Report',
    #                         description='DialsMeasured with: ')
    # testResultReport = runner.run(suite)
    # fp.close()

