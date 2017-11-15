# urs/bin/python
# encoding:utf-8

import unittest,os,sys
import time


p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("path: %s" %p)

sys.path.append(p+"/")
localPath = "/var/appiumRunLog"
reportPath = localPath + "/report/"
# failReport = localPath + "/failReport/"
logPath = localPath + "/logs/"
print("report: %s" %reportPath)
print("report: %s" %logPath)


from src.testcase.v722.testSend import TestSend
from src.testcase.v722.testContant import TestContant
from src.testcase.v722.test139Selected import TestSelect
from src.testcase.v722.testPush import TestPush
from src.testcase.HTMLTestRunner import HTMLTestRunner
from src.testcase.v722.testLogin import TestLogin
from src.mail.sendEmailSmtp import SendMail
from src.testcase.v722.testDownFile import TestDownFile
from src.otherApk.testSpeed import TestSpeed
# from src.testcase.v722.firstLogin import InitData
# from src.base.baseAdb import BaseAdb

'''
优化测试结果：
1、用例1：success
2、用例2：success
3、用例3：Fail
4、用例4：success

'''


if __name__ == "__main__":
    # 获取当前网速
    ts = TestSpeed()
    ts.setUp()
    speed = ts.testCase()
    ts.tearDown()


    print("speed: %s" %speed)
    time.sleep(10)

    print('正式运行脚本')
    result = {}
    testtxt = {}

    result['testCaseLogin'] = 'Success'
    result['testCaseSend'] = 'Success'
    result['testCaseFwdSend'] = 'Success'
    result['testDownFile'] = 'Success'
    result['testCaseCheckAddressList'] = 'Success'
    result['testCaseSelected'] = 'Success'
    result['testCasePush'] = 'Success'

    # 用例名 与用例说明
    testtxt['账号登录'] = 'testCaseLogin'
    testtxt['发送邮件带附件'] = 'testCaseSend'
    testtxt['转发邮件带附件'] = 'testCaseFwdSend'
    testtxt['附件下载'] = 'testDownFile'
    testtxt['联系人同步'] = 'testCaseCheckAddressList'
    testtxt['收件箱列表中精选'] = 'testCaseSelected'
    testtxt['接收推送'] = 'testCasePush'

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
    # filename = r'/Users/apple/git/pytest/report/index.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Test Report',
                            description='DialsMeasured with: ')
    testResultReport = runner.run(suite)
    fp.close()



    '''以下是结果筛选，写入日志，并发送简单的汇报邮件'''
    time.sleep(2)

    l = []
    for case, reason in testResultReport.failures:
        print("case：%s" % case)
        l.append(str(case))

    # print('ces %s'  %l)

    # 将运行错误的坐标记
    for k, v in result.items():
        for line in l:
            if line.find(k) != -1:
                result[k] = 'Fail'

    # print(result)
    # print(testtxt)


    # 将两个字典合并，将测试结果整理
    for k1, v1 in result.items():
        for k2, v2 in testtxt.items():
            if k1 == v2:
                testtxt[k2] = result[k1]

    print(testtxt)



    resulttxt = [] # 写入日志
    sendresult = [] # 邮件发送正文
    resulttxt.append('\n'+"====="+now +"====="+'\n')
    resulttxt.append(speed +'\n')
    sendresult.append('\n'+"====="+now +"====="+'\n')
    sendresult.append(speed +'\n')

    for case, reason in testtxt.items():
        resulttxt.append('case：%s , result：%s \n' %(case, reason) )
        if reason == 'Fail':
            sendresult.append('case：<font size="3" color="blue"> %s </font> , result：<font size="4" color="red"> %s </font>\n' %(case, reason) )
        else:
            sendresult.append('case：<font size="3" color="blue"> %s </font> , result：<font size="3" color="green"> %s </font>\n' %(case, reason) )

    print("过滤日志，写入日志：%s" %resulttxt)


    #所有问题
    for line in resulttxt:
        with open(logPath + "All.log",'a+') as fn:
            fn.write(line)

    time.sleep(5)

    print("预备发送 %s：" %sendresult)


    # print(line)
    s = SendMail("13580491603","chinasoft123","13697485262")
    s.sendMailMan('139Android客户端V722版本_功能拨测<请勿回复>',sendresult)
