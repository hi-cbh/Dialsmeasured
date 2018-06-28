# urs/bin/python
# encoding:utf-8

import time,unittest

from src.readwriteconf.rwconf import ReadWriteConfFile
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import duser
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}
print(user)

is_status=ReadWriteConfFile.get_status_value()

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

            LogAction.print('=>【发现页面】')
            self.assertTrue(self.driver.element_wait(u"uiautomator=>139精选",80),"页面显示不正常")
            LogAction.save(func = "testCaseDiscover", status="success", explain=LogAction.print())
            ReadWriteConfFile.value_set_zero("testCaseDiscover")
        except BaseException:
            ReadWriteConfFile.value_add_one("testCaseDiscover")
            BaseImage.screenshot(self.driver, "testCaseDiscover")
            time.sleep(2)
            LogAction.save(func = "testCaseDiscover", status="fail", explain=LogAction.print())

            if is_status:
                self.fail("【发现】出错！")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestDiscover('testCaseDiscover'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)