# urs/bin/python
# encoding:utf-8

import time,unittest
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import duser
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save
from src.base.baseLog import LogAction

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}
print(user)

class TestDiscover(unittest.TestCase):
    '''发现页面是否显示正常'''
    def __init__(self,driver):
        self.driver = driver

    def testCaseDiscover(self):
        '''发现主页'''
        try:
            LogAction.print(isReset=True)
            Login(self.driver,user['name'], user['pwd']).login()

            LogAction.print('=>发现')
            self.driver.click(u'uiautomator=>发现')
            start = time.time()

            LogAction.print('【验证点：页面是否显示正常】')
            self.assertTrue(self.driver.element_wait(u"uiautomator=>139精选",80),"页面显示不正常")

            print('=>记录当前时间，时间差')
            value_time = str(round((time.time() - start), 2))

            print('[发现页面]: %r'  %value_time)
            save.save("发现主页:%s" %value_time)
            LogAction.save(func = "testCaseDiscover", status="success", explain="value_time:%s" %value_time)
        except BaseException:
            BaseImage.screenshot(self.driver, "testCaseDiscover")
            time.sleep(5)
            LogAction.save(func = "testCaseDiscover", status="fail", explain=LogAction.print())
            self.fail("【发现】出错！")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestDiscover('testCaseDiscover'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)