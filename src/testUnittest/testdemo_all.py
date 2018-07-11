import unittest

from readwriteconf.rwconf import ReadWriteConfFile
from testUnittest.runTest_rest import RunAll
from testUnittest.testcasedemo.testdemo1 import MyTest1
from testUnittest.testcasedemo.testdemo2 import MyTest2
from testUnittest.testcasedemo.testdemo3 import MyTest3


class TestCase(unittest.TestCase):

    def setUp(self):
        print("TestCase.setUp")

    def tearDown(self):
        print("TestCase.tearDown")

    def testcase01(self):
        MyTest1().testCase01()

    def testcase02(self):
        MyTest2().testCase01()

    def testcase03(self):
        MyTest3().testCase01()


if __name__ == "__main__":
    ReadWriteConfFile.value_set_true_false(True)
    print('=================中文-英文对应测试用例=================')
    testtxt = []

    testtxt.append(('测试1',"testcase01"))
    testtxt.append(('测试2',"testcase02"))
    testtxt.append(('测试3',"testcase03"))



    print('=================测试用例加入测试套件=================')
    suite = unittest.TestSuite()
    suite.addTest(TestCase("testcase01"))
    suite.addTest(TestCase("testcase02"))
    suite.addTest(TestCase("testcase03"))

    runner = unittest.TextTestRunner()
    testResultReport = runner.run(suite)

    RunAll.run_case()