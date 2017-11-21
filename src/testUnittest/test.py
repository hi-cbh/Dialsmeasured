import unittest
from src.mail.sendEmailSmtp import  SendMail
from src.otherApk.testSpeed import TestSpeed
import time, datetime
from src.base.baseTime import BaseTime
from src.readwriteconf.rwconf import ReadWriteConfFile as rwc
from src.readwriteconf.initData import InitData
from src.readwriteconf.saveData import save
from src.readwriteconf.calcSucPer import CalcSuccess

logPath = InitData().getsysPath()["savepath"]+"/logs/"
logfileName= BaseTime.getDateHour() + '.log'



class MyTest(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        print("setUp.....")
        self.testRun = False

    @classmethod
    def tearDownClass(self):
        print("tearDown......")


    def testCase01(self):
        try:
            start = time.time()
            self.assertTrue(True, "测试错误")
            print("testCase01")
            time.sleep(1)
            print('=>记录当前时间，时间差')
            valueTime = str(round((time.time() - start), 2))
            print('[登录时延]: %r'  %valueTime)
            save.save("用例1:%s" %valueTime)
        except BaseException:
            self.fail("用例1 错误")

        else:
            print("testCase01")


    def testCase02(self):
        try:
            self.assertTrue(False, "测试错误")
            print("testCase02")
        except BaseException:
            self.fail("testCase02 错误")

        else:
            print("testCase02")


class MyTest2(unittest.TestCase):


    def setUp(self):
        time.sleep(1)
        print("MyTest2 setUp.....")
        self.testRun = False


    def tearDown(self):
        print("MyTest2 tearDown......")



    def testCase03(self):
        print("testCase01")
        start = time.time()
        time.sleep(1)
        print('=>记录当前时间，时间差')
        valueTime = str(round((time.time() - start), 2))
        print('[登录时延]: %r'  %valueTime)
        save.save("用例3:%s" %valueTime)


    def testCase04(self):
        try:
            self.assertTrue(False, "测试错误")
            print("testCase03")

        except BaseException:
            self.fail("MyTest2 testCase04 错误")
        else:
            print("testCase04 return")
            return 0





if __name__ == '__main__':
    speed = ''
    # ts = TestSpeed()
    # ts.setUp()
    # speed = ts.testCase()
    # ts.tearDown()

    print("speed: %s" %speed)

    # 添加测试的用例
    testtxt=[]
    testtxt.append(("用例1","testCase01"))
    testtxt.append(("用例2","testCase02"))
    testtxt.append(("用例3","testCase03"))
    testtxt.append(("用例4","testCase04"))

    # 中文与英文对应字典
    testtxt = dict(testtxt)

    # 统计用例结果字典
    result = {}
    # 传入发送邮件结果列表
    testcaselist = []

    for k, v in testtxt.items():
        testcaselist.append(k)
        result[v] = "Success"

    print(result)
    print(testcaselist)

    suite = unittest.TestSuite()
    suite.addTest(MyTest('testCase01'))
    suite.addTest(MyTest('testCase02'))
    suite.addTest(MyTest2('testCase03'))
    suite.addTest(MyTest2('testCase04'))


    runner = unittest.TextTestRunner(verbosity=2)
    testResultReport = runner.run(suite)
    time.sleep(2)

    # print('All case number')
    # print(testResultReport.failures)

    time.sleep(2)

    l = []
    for case, reason in testResultReport.failures:
        print("case：%s" % case)
        l.append(str(case))

    # print('ces %s'  %l)
    # 将用例错误标识
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

    # 用例中文-英文替换
    for k1, v1 in result.items():
        for k2, v2 in testtxt.items():
            if k1 == v2:
                testtxt[k2] = result[k1]

    print(testtxt)

    # 获取时间
    demotime=save.getValue()
    print("时延：%s" %demotime)


    resulttxt = []
    sendresult = []
    resulttxt.append('\n'+"================================"+'\n')
    sendresult.append(speed+'\n')
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
    cs = CalcSuccess(testcaselist,logPath + logfileName)

    # =============发送内容读取============
    allSendtxt = []
    # 汇总信息添加
    allSendtxt.append("====="+BaseTime.getCurrentTime()+"  当天运行记录结果汇总=====")
    for cline in cs.getSuccessercentage():
        allSendtxt.append(cline)
    # 详细结果
    allSendtxt.append("=====详细结果如下=====")
    with open(logPath + '1_'+logfileName,'r') as fs:
        tmplist = fs.readlines()

    for cline in tmplist:
        allSendtxt.append(cline)
    #==============发送内容读取=========


    print("预备发送 %s：" %allSendtxt)

    rwc.addSection( 'sendconf')
    changetime = rwc.getSectionValue( 'sendconf','changetime')
    changetime = int (changetime)


    print('当前时间：%s ' %datetime.datetime.now().hour)
    print('对比时间：%s ' %changetime)
    # 当前小时 大于晚上8点(20-23)
    if datetime.datetime.now().hour >= changetime:
        # 是否发送
        sendOrNot = rwc.getSectionValue('sendconf','send')
        print('sendOrNot %s' %sendOrNot)
        if sendOrNot == 'False':
            print('到点发送邮件')
            s = SendMail("13580491603","chinasoft123","13697485262")
            s.sendMailMan2('拨测出现异常',allSendtxt)
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
            s.sendMailMan2('拨测出现异常',allSendtxt)
            rwc.setSectionValue('sendconf','error','0')