import unittest
import re




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
    l = []
    for case, reason in testResultReport.failures:
        # print(case.id())
        # print(reason, )
        # l.append(case.id()+'\n')
        # l.append(reason +'\n')
        # print(reason)
        print(reason)
        # print("find: %r" %reason.find("AssertionError"))
        print(reason[reason.find("AssertionError")+16:])
        l.append(reason[reason.find("AssertionError")+16:]+'\n')


    with open("/Users/apple/autoTest/workspace/DialsMeasured/logs/run.log",'a+') as fn:
        for line in l:
            fn.write(line)

