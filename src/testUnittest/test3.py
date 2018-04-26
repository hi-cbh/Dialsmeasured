import unittest,os,sys
# 添加环境路径，脚本
p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("path: %s" %p)
sys.path.append(p+"/")

import time, datetime
from src.base.baseTime import BaseTime
from src.readwriteconf.initData import InitData
from src.base.baseLog import LogAction
import random
localPath = InitData().get_sys_path()["savepath"]
# 信息存储路径
reportPath = localPath + "/report/"
logPath = localPath + "/logs/"
iniPath = localPath + '/ini/'


logfileName= BaseTime.get_date_hour() + '.log'




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
            if int(random.random() * 10) > 5:
                self.assertTrue(True, "测试错误")
            else:
                self.assertTrue(False, "测试错误")

            print("testCase01")
            time.sleep(1)
            print('=>记录当前时间，时间差')
            value_time = str(round((time.time() - start), 2))
            print('[登录时延]: %r'  %value_time)
            # save.save("用例1:%s" %value_time)
        except BaseException:
            LogAction.save(func = "testCase01", status="Fail", explain="case 1 run error")
            self.fail("用例1 错误")


        else:
            print("testCase01")
            LogAction.save(func = "testCase01", status="OK")


    def testCase02(self):
        try:
            if int(random.random() * 10) > 5:
                self.assertTrue(True, "测试错误")
            else:
                self.assertTrue(False, "测试错误")
            print("testCase02")
        except BaseException:
            LogAction.save(func = "testCase02", status="Fail", explain="case 2 run error")
            self.fail("testCase02 错误")

        else:
            print("testCase02")
            LogAction.save(func = "testCase02", status="OK")


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
        value_time = str(round((time.time() - start), 2))
        print('[登录时延]: %r'  %value_time)
        # save.save("用例3:%s" %value_time)
        LogAction.save(func = "testCase03", status="OK")

    def testCase04(self):
        try:
            if int(random.random() * 10) > 5:
                self.assertTrue(True, "测试错误")
            else:
                self.assertTrue(False, "测试错误")
            print("testCase03")

        except BaseException:
            LogAction.save(func = "testCase04", status="Fail", explain="case 4 run error")
            self.fail("MyTest2 testCase04 错误")
        else:
            print("testCase04 return")
            LogAction.save(func = "testCase04", status="OK")
            return 0


if __name__ == '__main__':

    speed = ''

    print("speed: %s" %speed)

    # 添加测试的用例
    testtxt=[]
    testtxt.append(("用例1","testCase01"))
    testtxt.append(("用例2","testCase02"))
    testtxt.append(("用例3","testCase03"))
    testtxt.append(("用例4","testCase04"))

    suite = unittest.TestSuite()
    suite.addTest(MyTest('testCase01'))
    suite.addTest(MyTest('testCase02'))
    suite.addTest(MyTest2('testCase03'))
    suite.addTest(MyTest2('testCase04'))

    # 生成html
    runner = unittest.TextTestRunner()
    runner.run(suite)
