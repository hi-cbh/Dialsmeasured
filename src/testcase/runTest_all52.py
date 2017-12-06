# urs/bin/python
# encoding:utf-8

import unittest,os,sys
import time, datetime


# 添加环境路径，脚本
p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("path: %s" %p)
sys.path.append(p+"/")


localPath = "/var/appiumRunLog"
# 信息存储路径
reportPath = localPath + "/report/"




from src.testcase.v731.testSend import TestSend
from src.testcase.v731.testContant import TestContant
from src.testcase.v731.test139Selected import TestSelect
from src.testcase.v731.testPush import TestPush
from src.testcase.HTMLTestRunner import HTMLTestRunner
from src.testcase.v731.testLogin import TestLogin
from src.testcase.v731.testDownFile import TestDownFile
from src.otherApk.testSpeed import TestSpeed
from src.reportlib.reportclass import ReportClass

'''
优化测试结果：
1、成功是每天晚上8点发送邮件。
2、失败次数达到N次后，发送邮件。
将代码有，封装成类，方便理解
'''


if __name__ == "__main__":
    # 获取当前网速
    ts = TestSpeed()
    ts.setUp()
    speed = ts.testCase()
    ts.tearDown()

    # speed='调试中'
    # print("speed: %s" %speed)
    time.sleep(10)

    print('需要运行的脚本')
    testtxt = []

    testtxt.append(('账号登录',"testCaseLogin"))
    testtxt.append(('发送邮件带附件',"testCaseSend"))
    testtxt.append(('转发邮件带附件',"testCaseFwdSend"))
    testtxt.append(('附件下载',"testDownFile"))
    testtxt.append(('联系人同步',"testCaseCheckAddressList"))
    testtxt.append(('收件箱列表中精选',"testCaseSelected"))
    testtxt.append(('接收推送',"testCasePush"))


    suite = unittest.TestSuite()
    # suite.addTest(InitData("testCase"))
    suite.addTest(TestLogin('testCaseLogin'))
    suite.addTest(TestSend('testCaseSend'))
    suite.addTest(TestSend('testCaseFwdSend'))
    suite.addTest(TestDownFile('testDownFile'))
    suite.addTest(TestContant('testCaseCheckAddressList'))
    suite.addTest(TestSelect('testCaseSelected'))
    suite.addTest(TestPush('testCasePush'))

    runner = unittest.TextTestRunner()


    # 生成html
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename_now = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename = reportPath + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,title='Test Report', description='DialsMeasured with: ')
    testResultReport = runner.run(suite)
    fp.close()

    ReportClass(testResultReport.failures,testtxt,speed,now).all()