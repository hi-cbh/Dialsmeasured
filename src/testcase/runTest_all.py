# urs/bin/python
# encoding:utf-8

import unittest,os,sys
import time
p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("path: %s" %p)

sys.path.append(p+"/")
reportPath = p + "/report/"
logPath = p + "/logs/"
print("report: %s" %reportPath)

from src.testcase.v722.testSend import TestSend
from src.testcase.v722.testContant import TestContant
from src.testcase.v722.test139Selected import TestSelect
from src.testcase.v722.testPush import TestPush
from src.testcase.HTMLTestRunner import HTMLTestRunner
from src.mail.sendEmailSmtp import SendMail
# from src.testcase.v722.firstLogin import InitData
# from src.base.baseAdb import BaseAdb

if __name__ == "__main__":


    suite = unittest.TestSuite()
    # suite.addTest(InitData("testCase"))
    suite.addTest(TestSend('testCaseLogin'))
    suite.addTest(TestSend('testCaseSend'))
    suite.addTest(TestSend('testCaseFwdSend'))
    suite.addTest(TestContant('testCaseCheckAddressList'))
    suite.addTest(TestSelect('testCaseSelected'))
    suite.addTest(TestPush('testCasePush'))

    runner = unittest.TextTestRunner()



    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = reportPath + now + '_result.html'
    # filename = r'/Users/apple/git/pytest/report/index.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Test Report',
                            description='DialsMeasured with: ')
    testResultReport = runner.run(suite)
    fp.close()


    # 将错误结果写入 记录
    if len(testResultReport.failures) > 0:

        resulttxt = []
        resulttxt.append('\n'+"================================")
        resulttxt.append('\n'+now + " 运行错误：" + '\n')
        for case, reason in testResultReport.failures:
            # resulttxt.append(reason[reason.find("AssertionError")+16:] + '\n')
            resulttxt.append(reason + '\n')


        #所有问题
        for line in resulttxt:
            with open(logPath + "errorAll.log",'a+') as fn:
                fn.write(line)

        # 每一轮文件
        for line in resulttxt:
            with open(logPath + "tmprun.log",'w') as fn:
                fn.write(line)

        time.sleep(5)


        line = []
        with open(logPath + "tmprun.log",'r') as fn:
            line.append(fn.readlines())

        # print(line)
        s = SendMail("13580491603","chinasoft123","13697485262")
        s.sendMailMan('拨测出现异常',line)