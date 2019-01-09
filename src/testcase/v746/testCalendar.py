# urs/bin/python
# encoding:utf-8

import time,unittest

from src.readwriteconf.rwconf import ReadWriteConfFile
from src.base.baseAdb import BaseAdb
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import  duser
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}

class TestCalendar(unittest.TestCase):
    '''日历是否能打开'''

    def __init__(self,driver):
        self.driver = driver

    def testCaseCalendar(self):
        '''日历'''
        try:
            LogAction.print(isReset=True)
            Login(self.driver,user['name'], user['pwd']).login()

            # 这里添加埋点，是否登录成功

            LogAction.print("=>我的")
            self.driver.click(u"uiautomator=>我的")

            LogAction.print("=>日历")
            self.driver.click(u"uiautomator=>日历")

            # 这里添加埋点

            # LogAction.print("=>【创建日程】")
            # self.assertTrue(self.driver.element_wait("uiautomator=>创建日程提醒",10)!=None, "日历同步失败！！")

            BaseAdb.adb_back()
            LogAction.save(func = "testCaseCalendar", status="success", explain=LogAction.print())
            ReadWriteConfFile.value_set_zero("testCaseCalendar")
        except BaseException :
            ReadWriteConfFile.value_add_one("testCaseCalendar")
            ReadWriteConfFile.value_error_add_one("testCaseCalendar")
            ReadWriteConfFile.value_hourerror_add_one("testCaseCalendar")
            BaseImage.screenshot(self.driver, "testCaseCalendar")
            time.sleep(2)
            LogAction.save(func = "testCaseCalendar", status="fail", explain=LogAction.print())
            if ReadWriteConfFile.get_status_value():
                self.fail("【日历】出错")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCalendar('testCaseCalendar'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)