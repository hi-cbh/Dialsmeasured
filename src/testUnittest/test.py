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


    def testCase01(self):
        print("testCase01")

    def testCase02(self):
        try:
            self.assertTrue(False, "测试错误")
            print("testCase01")
        except BaseException:
            self.fail("MyTest2 testCase02 错误")

        else:
            print("testCase01")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyTest('testCase01'))
    suite.addTest(MyTest('testCase02'))
    suite.addTest(MyTest2('testCase01'))
    suite.addTest(MyTest2('testCase02'))

    runner = unittest.TextTestRunner(verbosity=2)
    testResultReport = runner.run(suite)

    # print('All case number')
    # print(testResultReport.testsRun)
    print('Failed case number')
    print(len(testResultReport.failures))
    # print('Failed case and reason')
    # print(testResultReport.failures)


    resulttxt = []
    sendresult = []
    resulttxt.append('\n'+"================================"+'\n')
    for case, reason in testResultReport.failures:
        print("所有打印：%s" %reason)
        if reason.find("fail") != -1:
            resulttxt.append(reason[reason.find("fail"):] + '\n')


    print("过滤日志，写入日志：%s" %resulttxt)




    #所有问题
    for line in resulttxt:
        with open(logPath + "errorAll.log",'a+') as fn:
            fn.write(line)
            sendresult.append(line)


    time.sleep(5)

    print("预备发送 %s：" %sendresult)


    # # print(line)
    s = SendMail("13580491603","chinasoft123","13697485262")
    s.sendMailMan('拨测出现异常',sendresult)

