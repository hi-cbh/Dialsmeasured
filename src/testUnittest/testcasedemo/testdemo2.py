import unittest

from readwriteconf.rwconf import ReadWriteConfFile

stat = ReadWriteConfFile.get_status_value()

class MyTest2(unittest.TestCase):

    def __init__(self):
        print("MyTest2,__init__%s"  %str(stat))


    def testCase01(self):
        try:
            # start = time.time()
            # if int(random.random() * 10) > 5:
            #     self.assertTrue(True, "测试错误")
            # else:
            #     self.assertTrue(False, "测试错误")
            self.assertTrue(False, "测试错误")
            print("testCase01")
            # time.sleep(1)
            # print('=>记录当前时间，时间差')
            # value_time = str(round((time.time() - start), 2))
            # print('[登录时延]: %r'  %value_time)
            # save.save("用例1:%s" %value_time)
        except BaseException:
            print("MyTest2.testCase01.fail")
            # self.fail("用例1 错误")

