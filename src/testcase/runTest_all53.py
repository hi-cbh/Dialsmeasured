# urs/bin/python
# encoding:utf-8

import unittest,os,sys,time


# 添加环境路径，脚本
from src.psam.psam import Psam
from testcase.v746.test139Selected import TestSelect
from testcase.v746.testCalendar import TestCalendar
from testcase.v746.testContant import TestContant
from testcase.v746.testDiscover import TestDiscover
from testcase.v746.testDownFile import TestDownFile
from testcase.v746.testLogin import TestLogin
from testcase.v746.testPerson import TestPersion
from testcase.v746.testPush import TestPush
from testcase.v746.testSend import TestSend
from testcase.v746.testSkyDrive import TestSkyDrive

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("path: %s" %p)
sys.path.append(p+"/")

localPath = "/var/appiumRunLog"
# 信息存储路径
reportPath = localPath + "/report/"

from src.testcase.HTMLTestRunner import HTMLTestRunner
from src.reportlib.reportclass import ReportClass
from src.base.baseAdb import BaseAdb



'''
1、账号统一；
2、用例使用一个文件中
'''

class TestCase(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(self):
        BaseAdb.adb_intall_uiautmator()
        # self.driver = Psam()
        self.driver = Psam(version="6.0")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)


    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def testCaseOnBtnLogin(self):
        '''一键登录'''
        TestLogin(self.driver).testCaseOnBtnLogin()

    def testCaseLogin(self):
        '''账号登录'''
        TestLogin(self.driver).testCaseLogin()

    def testCaseSend(self):
        '''发送邮件'''
        TestSend(self.driver).testCaseSend()

    def testCaseFwdSend(self):
        '''云端转发'''
        TestSend(self.driver).testCaseFwdSend()

    def testCaseReply(self):
        '''回复邮件'''
        TestSend(self.driver).testCaseReply()

    def testCaseForward(self):
        '''SMTP转发附件'''
        TestSend(self.driver).testCaseForward()

    def testDownFile(self):
        '''下载附件'''
        TestDownFile(self.driver).testDownFile()

    def testCaseCalendar(self):
        '''日历'''
        TestCalendar(self.driver).testCaseCalendar()


    def testCaseDiscover(self):
        '''发现主页'''
        TestDiscover(self.driver).testCaseDiscover()

    def testCasePersionMessages(self):
        '''个人资料'''
        TestPersion(self.driver).testCasePersionMessages()

    def testCaseCheckAddressList(self):
        '''联系人同步'''
        TestContant(self.driver).testCaseCheckAddressList()

    def testCaseSelected(self):
        '''收件箱列表139精选'''
        TestSelect(self.driver).testCaseSelected()

    def testCaseSkyDrive(self):
        '''彩云网盘'''
        TestSkyDrive(self.driver).testCaseSkyDrive()

    def testCasePush(self):
        '''推送'''
        TestPush(self.driver).testCasePush()


if __name__ == "__main__":
    BaseAdb.adb_wake_up()
    time.sleep(5)

    print('需要运行的脚本')
    testtxt = []

    _run = 5

    testtxt.append(('账号登录',"testCaseLogin"))

    testtxt.append(('一键登录',"testCaseOnBtnLogin"))

    testtxt.append(('发送邮件带附件',"testCaseSend"))

    testtxt.append(('云端转发',"testCaseFwdSend"))

    testtxt.append(('回复邮件',"testCaseReply"))

    testtxt.append(('SMTP转发',"testCaseForward"))

    testtxt.append(('日历',"testCaseCalendar"))

    testtxt.append(('发现主页',"testCaseDiscover"))

    testtxt.append(('个人资料',"testCasePersionMessages"))

    testtxt.append(('彩云网盘',"testCaseSkyDrive"))

    testtxt.append(('附件下载',"testDownFile"))

    testtxt.append(('联系人同步',"testCaseCheckAddressList"))

    testtxt.append(('收件箱列表中精选',"testCaseSelected"))

    testtxt.append(('接收推送',"testCasePush"))


    suite = unittest.TestSuite()
    suite.addTest(TestCase('testCaseOnBtnLogin'))

    suite.addTest(TestCase('testCaseLogin'))

    suite.addTest(TestCase('testCaseSend'))

    suite.addTest(TestCase('testCaseFwdSend'))

    suite.addTest(TestCase('testCaseForward'))

    suite.addTest(TestCase('testCaseReply'))

    suite.addTest(TestCase('testCaseCalendar'))

    suite.addTest(TestCase('testCaseDiscover'))

    suite.addTest(TestCase('testCasePersionMessages'))

    suite.addTest(TestCase('testCaseSkyDrive'))

    suite.addTest(TestCase('testDownFile'))

    suite.addTest(TestCase('testCaseCheckAddressList'))

    suite.addTest(TestCase('testCaseSelected'))

    suite.addTest(TestCase('testCasePush'))

    runner = unittest.TextTestRunner()



    # 生成html
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename_now = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename = reportPath + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,title='Test Report', description='DialsMeasured with: ')
    testResultReport = runner.run(suite)
    fp.close()



    ReportClass(testResultReport.failures,testtxt,"",now).all()

    time.sleep(5)
    # 休眠状态
    BaseAdb.adb_sleep()

    time.sleep(5)