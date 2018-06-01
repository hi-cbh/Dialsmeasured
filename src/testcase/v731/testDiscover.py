# urs/bin/python
# encoding:utf-8
import datetime
import random,time,unittest
from src.psam.psam import Psam
from src.testcase.v731.easycase.login import Login
from src.readwriteconf.initData import InitData
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save
from src.base.baseLog import LogAction

d= InitData().get_users()
print(d)


# 主账号
if datetime.datetime.now().hour%2 == 0:
    user = {"name": d['user3'], 'pwd': d['pwd3']}
else:
    user = {"name": d['user4'], 'pwd': d['pwd4']}
print(user)

class TestDiscover(unittest.TestCase):
    '''发现页面是否显示正常'''
    def setUp(self):
        try:
            # BaseAdb.adb_intall_uiautmator()
            self.driver = Psam(version="5.1")
        except BaseException:
            print("setUp启动出错！")
            LogAction.save(func = "TestDiscover", status="Fail", explain="Psam 启动出错")
            self.fail("setUp启动出错！")


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)

    def testCaseDiscover(self):
        '''发现主页'''

        try:
            LogAction.print(isReset=True)
            LogAction.print("=>账号登录")
            Login(self.driver,user['name'], user['pwd']).login_action(is_save=False)

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