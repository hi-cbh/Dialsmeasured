# urs/bin/python
# encoding:utf-8
import datetime
import time,unittest

from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import InitData, duser
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save
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

            LogAction.print("【彩云网盘】")
            self.assertTrue(self.driver.element_wait("uiautomator=>手机图片",60)!=None, "彩云网盘同步失败！！")
            BaseAdb.adb_back()
            LogAction.save(func = "testCaseSkyDrive", status="success", explain=LogAction.print())
        except BaseException :
            BaseImage.screenshot(self.driver, "testCaseSkyDrive")
            time.sleep(5)
            LogAction.save(func = "testCaseSkyDrive", status="fail", explain=LogAction.print())
            self.fail("【彩云网盘】出错")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSkyDrive('testCaseSkyDrive'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)