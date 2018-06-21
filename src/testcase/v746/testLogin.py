# urs/bin/python
# encoding:utf-8
import datetime
import time,unittest

from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import InitData, duser
from src.base.baseLog import LogAction

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}


filename = InitData().get_file()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(user["name"], filename)


class TestLogin(unittest.TestCase):
    '''登录是否成功'''
    def __init__(self,driver):
        self.driver = driver
    # def setUp(self):
    #     stat = ""
    #     try:
    #         # BaseAdb.adb_intall_uiautmator()
    #         stat = "Psam启动出错"
    #         self.driver = Psam(version= "6.0")
    #
    #     except BaseException:
    #         print("setUp启动出错！")
    #         self.driver.quit()
    #         LogAction.save(func = "TestLogin", status="fail", explain=stat)
    #         self.fail("setUp启动出错！")
    #
    #
    # #释放实例,释放资源
    # def tearDown(self):
    #     self.driver.quit()
    #     print("运行结束")
    #
    #     time.sleep(5)


    def testCaseLogin(self):
        '''账号登录'''
        Login(self.driver,user["name"], user["pwd"]).login_action()


    def testCaseOnBtnLogin(self):
        '''一键登录'''
        Login(self.driver,user["name"], user["pwd"]).one_btn_Login()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    suite.addTest(TestLogin('testCaseLogin'))
    runner.run(suite)