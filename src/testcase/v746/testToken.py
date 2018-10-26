# urs/bin/python
# encoding:utf-8
import unittest
import time
from src.base.baseAdb import BaseAdb
# from src.psam.psam import Psam
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import InitData, duser

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}


filename = InitData().get_file()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(user["name"], filename)


class TestToken(unittest.TestCase):
    '''登录是否成功'''

    # def setUp(self):
    #     try:
    #         BaseAdb.adb_intall_uiautmator()
    #         self.driver = Psam(version= "6.0")
    #
    #     except BaseException:
    #         print("setUp启动出错！")
    #         self.driver.quit()


    def __init__(self,driver):
        self.driver = driver

    def testCaseToken(self):
        '''账号登录'''
        # 删除文件
        time.sleep(3)
        BaseAdb.adb_shell("adb shell rm -rf /mnt/sdcard/cmcc_sso_download")
        BaseAdb.adb_shell("adb shell rm -rf /mnt/sdcard/cmcc_sso_ks")
        BaseAdb.adb_shell("adb shell rm -rf /mnt/sdcard/cmcc_sso_south_log")
        time.sleep(3)
        Login(self.driver,user["name"], user["pwd"]).open_token_info()



if __name__ == "__main__":
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    suite.addTest(TestToken('testCaseToken'))
    runner.run(suite)