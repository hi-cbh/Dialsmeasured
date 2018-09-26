# urs/bin/python
# encoding:utf-8
import unittest
import time
from base.baseAdb import BaseAdb
from psam.psam import Psam
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import InitData, duser

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}


filename = InitData().get_file()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(user["name"], filename)


class TestLogin(unittest.TestCase):
    '''登录是否成功'''

    # def setUp(self):
    #     try:
    #         # BaseAdb.adb_intall_uiautmator()
    #         self.driver = Psam(version= "6.0")
    #
    #     except BaseException:
    #         print("setUp启动出错！")
    #         self.driver.quit()


    def __init__(self,driver):
        self.driver = driver

    def testCaseLogin(self):
        '''账号登录'''
        Login(self.driver,user["name"], user["pwd"]).login_action()


    def testCaseOnBtnLogin(self):
        '''一键登录'''
        Login(self.driver,user["name"], user["pwd"]).one_btn_Login()

    # def testcase(self):
    #     print("sleep")
    #     time.sleep(10)
    #     print(self.driver.current_app())


if __name__ == "__main__":
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    suite.addTest(TestLogin('testcase'))
    runner.run(suite)