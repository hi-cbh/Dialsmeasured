# urs/bin/python
# encoding:utf-8

import unittest,os,sys,time

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("path: %s" %p)
sys.path.append(p+"/")
# 添加环境路径，脚本
from src.base.baseAdb import BaseAdb
from src.testcase.runTest_all53 import TestCase
'''
全部用例重跑
'''

class RunAll(unittest.TestCase):

    def run_case(self):
        BaseAdb.adb_wake_up()
        time.sleep(5)

        print('=================重跑用例=================')
        suite = unittest.TestSuite()
        suite.addTest(TestCase('testCaseOnBtnLogin'))
        suite.addTest(TestCase('testCaseLogin'))
        suite.addTest(TestCase('testCaseSendNoAttach'))
        suite.addTest(TestCase('testCaseSendAttach'))
        suite.addTest(TestCase('testCaseFwdSend'))
        suite.addTest(TestCase('testCaseForward'))
        suite.addTest(TestCase('testCaseReply'))
        suite.addTest(TestCase('testCaseCalendar'))
        suite.addTest(TestCase('testCasePersionMessages'))
        suite.addTest(TestCase('testCaseSkyDrive'))
        suite.addTest(TestCase('testDownFile'))
        suite.addTest(TestCase('testCaseCheckAddressList'))
        suite.addTest(TestCase('testCaseSelected'))
        suite.addTest(TestCase('testCasePush'))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        print('=================运行结束=================')
        # 休眠状态
        BaseAdb.adb_sleep()
        time.sleep(5)
