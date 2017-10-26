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
        print("testCase01")
        self.fail("testCase01 错误")

    def testCase02(self):
        print("testCase02")
        self.fail("testCase02 错误")

    def testCase03(self):
        print("testCase02")
        self.fail("testCase02 错误")
    # @unittest.skipIf(unittest.testRun , "当条件为True跳过测试")
    # def test_skip_if(self):
    #     print("test bbb")
    #
    # @unittest.skipUnless(testRun, "当条件为True执行测试")
    # def test_skip_unless(self):
    #     print("test ccc")

    def writelogs(self):
        with open("run.log") as fn:
            fn.write("hello")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyTest('testCase01'))
    suite.addTest(MyTest('testCase02'))

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

        if reason.find("fail") != -1:
            resulttxt.append(reason[reason.find("fail"):] + '\n')
            print("打印：%s" %resulttxt)


    #所有问题
    for line in resulttxt:
        with open(logPath + "errorAll.log",'a+') as fn:
            fn.write(line)
            sendresult.append(line)


    time.sleep(5)

    print("发送 %s：" %sendresult)


    # print(line)
    s = SendMail("13580491603","chinasoft123","13697485262")
    s.sendMailMan('拨测出现异常',sendresult)

