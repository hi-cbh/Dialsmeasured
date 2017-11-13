import unittest
from src.mail.sendEmailSmtp import  SendMail
from src.otherApk.testSpeed import TestSpeed
import time, datetime
from src.base.baseTime import BaseTime
from src.readwriteconf.rwconf import ReadWriteConfFile

logPath = "/Users/apple/autoTest/workspace/DialsMeasured/logs/"
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
            self.assertTrue(False, "测试错误")
            print("testCase01")
        except BaseException:
            self.fail("testCase01 错误")

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

    # @unittest.skipIf(unittest.testRun , "当条件为True跳过测试")
    # def test_skip_if(self):
    #     print("test bbb")
    #
    # @unittest.skipUnless(testRun, "当条件为True执行测试")
    # def test_skip_unless(self):
    #     print("test ccc")

class MyTest2(unittest.TestCase):


    def setUp(self):
        print("MyTest2 setUp.....")
        self.testRun = False

    def tearDown(self):
        print("MyTest2 tearDown......")


    def testCase03(self):
        print("testCase01")

    def testCase04(self):
        try:
            self.assertTrue(False, "测试错误")
            print("testCase03")
        except BaseException:
            self.fail("MyTest2 testCase04 错误")

        else:
            print("testCase01")

if __name__ == '__main__':
    speed = ''
    # ts = TestSpeed()
    # ts.setUp()
    # speed = ts.testCase()
    # ts.tearDown()

    print("speed: %s" %speed)


    result = {}
    result['testCase01'] = 'Success'
    result['testCase02'] = 'Success'
    result['testCase03'] = 'Success'
    result['testCase04'] = 'Success'

    testtxt = {}
    testtxt['用例1'] = 'testCase01'
    testtxt['用例2'] = 'testCase02'
    testtxt['用例3'] = 'testCase03'
    testtxt['用例4'] = 'testCase04'




    suite = unittest.TestSuite()
    suite.addTest(MyTest('testCase01'))
    suite.addTest(MyTest('testCase02'))
    suite.addTest(MyTest2('testCase03'))
    suite.addTest(MyTest2('testCase04'))


    runner = unittest.TextTestRunner(verbosity=2)
    testResultReport = runner.run(suite)

    # print('All case number')
    # print(testResultReport.failures)

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
        ReadWriteConfFile.addSection( 'sendconf')
        x = ReadWriteConfFile.getSectionValue('sendconf','error')
        x = int(x) + 1
        ReadWriteConfFile.setSectionValue( 'sendconf','error',str(x))

    # print(result)
    # print(testtxt)


    for k1, v1 in result.items():
        for k2, v2 in testtxt.items():
            if k1 == v2:
                testtxt[k2] = result[k1]

    print(testtxt)



    resulttxt = []
    sendresult = []
    resulttxt.append('\n'+"================================"+'\n')
    sendresult.append(speed+'\n')
    for case, reason in testtxt.items():
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

    print("预备发送 %s：" %allSendtxt)

    ReadWriteConfFile.addSection( 'sendconf')
    changetime = ReadWriteConfFile.getSectionValue( 'sendconf','changetime',)
    changetime = int (changetime)


    print('当前时间：%s ' %datetime.datetime.now().hour)
    print('对比时间：%s ' %changetime)
    # 当前小时 大于晚上8点(20-23)
    if datetime.datetime.now().hour >= changetime:

        sendOrNot = ReadWriteConfFile.getSectionValue('sendconf','send')
        print('sendOrNot %s' %sendOrNot)
        if sendOrNot == 'False':
            print('到点发送邮件')
            s = SendMail("13580491603","chinasoft123","13697485262")
            s.sendMailMan2('拨测出现异常',allSendtxt)
            ReadWriteConfFile.setSectionValue('sendconf','send','True')
            ReadWriteConfFile.setSectionValue('sendconf','error','0')

    # 1 - 20
    else:
        if datetime.datetime.now().hour in [1, 2]:
            ReadWriteConfFile.setSectionValue('sendconf','send','False')


        error = ReadWriteConfFile.getSectionValue('sendconf','error')
        maxtimes = ReadWriteConfFile.getSectionValue('sendconf','maxtimes')

        # 错误次数
        if int(error) >= int(maxtimes):
            s = SendMail("13580491603","chinasoft123","13697485262")
            s.sendMailMan2('拨测出现异常',allSendtxt)
            ReadWriteConfFile.setSectionValue('sendconf','error','0')