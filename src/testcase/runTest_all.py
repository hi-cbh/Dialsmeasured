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
# from src.testcase.v722.firstLogin import InitData
# from src.base.baseAdb import BaseAdb

if __name__ == "__main__":
    # # apkpath = ""
    # apkpath = r"/Users/apple/Downloads/Pushemail-ANDROID-V7.2.2-20170928_24603__2008001.apk"
    # try:
    #     if len(sys.argv) > 1:
    #         apkpath = sys.argv[1]
    #         if apkpath not in [None, ""]:
    #             print("获得的路径为：%s" %apkpath)
    #         else:
    #             print("安装包路径有问题....")
    #     else:
    #         print("外部传参路径有问题！，使用默认apk")
    #
    #
    #     '''卸载旧包'''
    #     if BaseAdb.adbApkExist("cn.cj.pe") == True:
    #         print('delete new apk')
    #         BaseAdb.uninstallAPP("cn.cj.pe")
    #         time.sleep(8)
    #
    #     if apkpath != None:
    #         # 安装新包
    #         print('install new apk')
    #         BaseAdb.installApp(apkpath)
    #         print(u'等待10秒')
    #         time.sleep(20)
    #         print(u"等待完成")
    #
    #     if BaseAdb.adbApkExist("cn.cj.pe") == False:
    #         print("安装包失败，不运行后续步骤，直接退出")
    #         os._exit(0)
    # except BaseException as e:
    #     print(e)



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
    if testResultReport.failures > 0:

        resulttxt = []
        resulttxt.append('\n'+now + " 运行错误：" + '\n')
        for case, reason in testResultReport.failures:
            resulttxt.append(reason[reason.find("AssertionError")+16:] + '\n')

        for line in resulttxt:
            with open(logPath + "run.log",'a+') as fn:
                fn.write(line)
