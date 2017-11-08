import unittest
from src.mail.sendEmailSmtp import  SendMail
import time


logPath = "/Users/apple/autoTest/workspace/DialsMeasured/logs/"

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

    for k, v in result.items():
        for line in l:
            if line.find(k) != -1:
                result[k] = 'Fail'

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
    for case, reason in testtxt.items():
        resulttxt.append('case：%s , result：%s \n' %(case, reason) )
        if reason == 'Fail':
            sendresult.append('case：<font size="3" color="blue"> %s </font> , result：<font size="4" color="red"> %s </font>\n' %(case, reason) )
        else:
            sendresult.append('case：<font size="3" color="blue"> %s </font> , result：<font size="3" color="green"> %s </font>\n' %(case, reason) )


    print("过滤日志，写入日志：%s" %resulttxt)
    # print("过滤日志，写入日志：%s" %sendresult)




    #所有问题
    for line in resulttxt:
        with open(logPath + "testLog.log",'a+') as fn:
            fn.write(line)
            # sendresult.append(line)


    time.sleep(5)

    print("预备发送 %s：" %sendresult)


    # # print(line)
    s = SendMail("13580491603","chinasoft123","13697485262")
    s.sendMailMan2('拨测出现异常',sendresult)

