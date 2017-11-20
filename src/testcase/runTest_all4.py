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
logPath = localPath + "/logs/"
iniPath = localPath + '/ini/'



from src.testcase.v722.testSend import TestSend
from src.testcase.v722.testContant import TestContant
from src.testcase.v722.test139Selected import TestSelect
from src.testcase.v722.testPush import TestPush
from src.testcase.HTMLTestRunner import HTMLTestRunner
from src.testcase.v722.testLogin import TestLogin
from src.mail.sendEmailSmtp import SendMail
from src.testcase.v722.testDownFile import TestDownFile
from src.otherApk.testSpeed import TestSpeed
from src.base.baseTime import BaseTime
# from src.testcase.v722.firstLogin import InitData
# from src.base.baseAdb import BaseAdb
from src.readwriteconf.rwconf import ReadWriteConfFile as rwc
from src.readwriteconf.saveData import save

# 文件名
logfileName= BaseTime.getDateHour() + '.log'

'''
优化测试结果：
1、成功是每天晚上8点发送邮件。
2、失败次数达到N次后，发送邮件。

'''


if __name__ == "__main__":
    # 获取当前网速


    ts = TestSpeed()
    ts.setUp()
    speed = ts.testCase()
    ts.tearDown()

    # speed='调试中'
    print("speed: %s" %speed)
    time.sleep(10)

    print('需要运行的脚本')
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

    errortimes = 0
    for k, v in result.items():
        for line in l:
            if line.find(k) != -1:
                result[k] = 'Fail'
                errortimes +=1 # 出现错误，自加1

    if errortimes != 0:
        # 这里设置添加错误次数
        rwc.addSection( 'sendconf')
        x = rwc.getSectionValue('sendconf','error')
        x = int(x) + 1
        rwc.setSectionValue( 'sendconf','error',str(x))


    # print(result)
    # print(testtxt)


    # 将两个字典合并，将测试结果整理
    for k1, v1 in result.items():
        for k2, v2 in testtxt.items():
            if k1 == v2:
                testtxt[k2] = result[k1]

    print(testtxt)

    # 获取时间
    demotime=save.getValue()
    print("时延：%s" %demotime)


    resulttxt = [] # 写入日志
    sendresult = [] # 邮件发送正文
    resulttxt.append('\n'+"====="+now +"====="+'\n')
    resulttxt.append(speed +'\n')
    sendresult.append('\n'+"====="+now +"====="+'\n')
    sendresult.append(speed +'\n')

    # 写入文件，并添加发送邮件格式
    for case, reason in testtxt.items():

        if case in demotime:
            resulttxt.append('case：%s , 时延：%s, result：%s \n' %(case,demotime[case], reason ))
            if reason == 'Fail':
                sendresult.append('case：<font size="3" color="blue"> %s </font> ,result：<font size="4" color="red"> %s </font>\n' %(case, reason) )
            else:
                sendresult.append('case：<font size="3" color="blue"> %s </font> , 时延：%s,  result：<font size="3" color="green"> %s </font>\n' %(case,demotime[case], reason) )

        else:

            resulttxt.append('case：%s , result：%s \n' %(case, reason) )
            if reason == 'Fail':
                sendresult.append('case：<font size="3" color="blue"> %s </font> , result：<font size="4" color="red"> %s </font>\n' %(case, reason) )
            else:
                sendresult.append('case：<font size="3" color="blue"> %s </font> , result：<font size="3" color="green"> %s </font>\n' %(case, reason) )


    print("过滤日志，写入日志：%s" %resulttxt)
    # print("过滤日志，写入日志：%s" %sendresult)


    #每天的测试记录
    for line in resulttxt:
        with open(logPath + logfileName,'a+') as fn:
            fn.write(line)

    #每天的测试记录(邮件内容)
    for line in sendresult:
        with open(logPath + '1_'+logfileName,'a+') as fs:
            fs.write(line)


    time.sleep(5)



    allSendtxt = []
    with open(logPath + '1_'+logfileName,'r') as fs:
        allSendtxt = fs.readlines()

    # print("预备发送 %s：" %allSendtxt)

    rwc.addSection( 'sendconf')
    changetime = rwc.getSectionValue( 'sendconf','changetime',)
    changetime = int (changetime)


    print('当前时间：%s ' %datetime.datetime.now().hour)
    print('对比时间：%s ' %changetime)
    # 当前小时 大于晚上8点(20-23)
    if datetime.datetime.now().hour >= changetime:

        sendOrNot = rwc.getSectionValue('sendconf','send')
        print('sendOrNot %s' %sendOrNot)
        if sendOrNot == 'False':
            print('到点发送邮件')
            s = SendMail("13580491603","chinasoft123","13697485262")
            s.sendMailMan('139Android客户端V722版本_功能拨测<请勿回复>',allSendtxt)
            rwc.setSectionValue('sendconf','send','True')
            rwc.setSectionValue('sendconf','error','0')

    # 1 - 20
    else:
        if datetime.datetime.now().hour in [1, 2]:
            rwc.setSectionValue('sendconf','send','False')


        error = rwc.getSectionValue('sendconf','error')
        maxtimes = rwc.getSectionValue('sendconf','maxtimes')

        # 错误次数
        if int(error) >= int(maxtimes):
            s = SendMail("13580491603","chinasoft123","13697485262")
            s.sendMailMan('139Android客户端V722版本_功能拨测<请勿回复>',allSendtxt)
            rwc.setSectionValue('sendconf','error','0')

    print('运行结束')
    time.sleep(15)