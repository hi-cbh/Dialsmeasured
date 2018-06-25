# urs/bin/python
# encoding:utf-8

import time,unittest

from src.base.baseAdb import BaseAdb
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import  duser
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save
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

            LogAction.print("【验证点：页面是否存在联系人字段】")
            self.assertTrue(self.driver.get_element(u"uiautomator=>我的",10) !=None, "页面找不到联系人字段")

            LogAction.print("=>我的")
            self.driver.click(u"uiautomator=>我的")

            LogAction.print("=>日历")
            self.driver.click(u"uiautomator=>日历")


            start = time.time()
            LogAction.print("【验证点：获页面创建日程提醒字段】")
            self.assertTrue(self.driver.element_wait("uiautomator=>创建日程提醒",10)!=None, "日历同步失败！！")

            print('=>记录当前时间，时间差')
            value_time = str(round((time.time() - start), 2))
            print('[日历]: %r'  %value_time)
            save.save("日历:%s" %value_time)

            BaseAdb.adb_back()
            LogAction.save(func = "testCaseCalendar", status="success", explain="value_time:%s" %value_time)
        except BaseException :
            BaseImage.screenshot(self.driver, "testCaseCalendar")
            time.sleep(2)
            LogAction.save(func = "testCaseCalendar", status="fail", explain=LogAction.print())
            self.fail("【日历】出错")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCalendar('testCaseCalendar'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)