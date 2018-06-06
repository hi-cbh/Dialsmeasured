# urs/bin/python
# encoding:utf-8
import datetime
import time,unittest,random

from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam
from src.testcase.v731.easycase.login import Login
from src.readwriteconf.initData import InitData
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save
from src.base.baseLog import LogAction

d = InitData().get_users()


# 主账号
if datetime.datetime.now().hour%2 == 0:
    user = {"name": d['user3'], 'pwd': d['pwd3']}
else:
    user = {"name": d['user4'], 'pwd': d['pwd4']}


class TestCalendar(unittest.TestCase):
    '''日历是否能打开'''
    def setUp(self):
        try:
            BaseAdb.adb_intall_uiautmator()
            self.driver = Psam(version="6.0")
        except BaseException:
            print("setUp启动出错！")
            self.driver.quit()
            LogAction.save(func = "TestCalendar", status="fail", explain="Psam 启动出错")
            self.fail("setUp启动出错！")


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")
        time.sleep(5)

    def testCaseCalendar(self):
        '''日历'''
        try:
            LogAction.print(isReset=True)

            login=Login(self.driver,user['name'], user['pwd'])
            login.login_action(is_save=False)

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
            LogAction.save(func = "testCaseCalendar", status="success", explain="value_time:%s" %value_time)
        except BaseException :
            BaseImage.screenshot(self.driver, "testCaseCalendar")
            time.sleep(5)
            LogAction.save(func = "testCaseCalendar", status="fail", explain=LogAction.print())
            self.fail("【日历】出错")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCalendar('testCaseCalendar'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)