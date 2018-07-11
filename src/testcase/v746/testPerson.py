# urs/bin/python
# encoding:utf-8
import time,unittest

from src.readwriteconf.rwconf import ReadWriteConfFile
from src.base.baseAdb import BaseAdb
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import duser
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}

class TestPersion(unittest.TestCase):
    '''个人资料是否显示正常'''
    def __init__(self,driver):
        self.driver = driver

    def testCasePersionMessages(self):
        '''个人资料'''
        try:
            LogAction.print(isReset=True)
            Login(self.driver,user['name'], user['pwd']).login()

            LogAction.print("=>我的")
            self.driver.click(u"uiautomator=>我的")

            LogAction.print("=>个人资料")
            self.driver.click(u"uiautomator=>个人资料")

            LogAction.print("=>【个人头像】")
            self.assertTrue(self.wait_for_message(), "个人资料同步失败！！")

            BaseAdb.adb_back()
            LogAction.save(func = "testCasePersionMessages", status="success", explain=LogAction.print())
            ReadWriteConfFile.value_set_zero("testCasePersionMessages")
        except BaseException :
            ReadWriteConfFile.value_add_one("testCasePersionMessages")

            BaseImage.screenshot(self.driver, "testCasePersionMessages")
            time.sleep(2)
            LogAction.save(func = "testCasePersionMessages", status="fail", explain=LogAction.print())

            if ReadWriteConfFile.get_status_value():
                self.fail("【个人资料】出错")


    def wait_for_message(self):
        '''找到需要的通知栏信息'''

        if self.driver.element_wait(u"uiautomator=>头像",10) == None:
            BaseAdb.adb_back()

        if self.driver.element_wait(u"uiautomator=>头像",2) == None:
            print('找不到了')
            return False
        else:
            return True

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestPersion('testCasePersionMessages'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)