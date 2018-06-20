# urs/bin/python
# encoding:utf-8
import datetime
import time,unittest

from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam
from src.testcase.v731.easycase.login import Login
from src.readwriteconf.initData import InitData
from src.base.baseLog import LogAction

d = InitData().get_users()

# 主账号
if datetime.datetime.now().hour%2 == 0:
    username = d['user3']
    pwd = d['pwd3']
else:
    username = d['user4']
    pwd = d['pwd4']

username2 = d['user2']
pwd2 = d['pwd2']

filename = InitData().get_file()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(username, filename)


class TestLogin(unittest.TestCase):
    '''登录是否成功'''
    def setUp(self):
        stat = ""
        try:
            BaseAdb.adb_intall_uiautmator()
            stat = "Psam启动出错"
            self.driver = Psam(version= "6.0")

        except BaseException:
            print("setUp启动出错！")
            self.driver.quit()
            LogAction.save(func = "TestLogin", status="fail", explain=stat)
            self.fail("setUp启动出错！")


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)


    def testCaseLogin(self):
        '''账号登录'''
        Login(self.driver,username, pwd).login_action()


    def testCaseOnBtnLogin(self):
        '''一键登录'''
        Login(self.driver,username, pwd).one_btn_Login()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    suite.addTest(TestLogin('testCaseLogin'))
    runner.run(suite)