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

class TestSkyDrive(unittest.TestCase):
    '''彩云网盘是否正常打开'''
    def __init__(self,driver):
        self.driver = driver

    def testCaseSkyDrive(self):
        '''彩云网盘'''
        try:
            LogAction.print(isReset=True)
            Login(self.driver,user['name'], user['pwd']).login()

            LogAction.print("=>我的")
            self.driver.click(u"uiautomator=>我的")

            LogAction.print("=>彩云网盘")
            self.driver.click(u"uiautomator=>彩云网盘")

            LogAction.print("=>【彩云网盘】")
            self.assertTrue(self.driver.element_wait("uiautomator=>手机图片",60)!=None, "彩云网盘同步失败！！")
            BaseAdb.adb_back()
            LogAction.save(func = "testCaseSkyDrive", explain=LogAction.print())
            ReadWriteConfFile.value_set_zero("testCaseSkyDrive")
        except BaseException :
            ReadWriteConfFile.value_add_one("testCaseSkyDrive")
            ReadWriteConfFile.value_error_add_one("testCaseSkyDrive")
            BaseImage.screenshot(self.driver, "testCaseSkyDrive")
            time.sleep(5)
            LogAction.save(func = "testCaseSkyDrive", status="fail", explain=LogAction.print())

            if ReadWriteConfFile.get_status_value():
                self.fail("【彩云网盘】出错")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSkyDrive('testCaseSkyDrive'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)