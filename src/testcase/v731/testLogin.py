# urs/bin/python
# encoding:utf-8

import os,time,unittest
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v731.easycase.login import Login
from src.testcase.v731.easycase.send import Send
from src.readwriteconf.initData import InitData

# sys.path.append(r"/Users/apple/git/pytest/")

d = InitData().get_users()

username = d['user3']
pwd = d['pwd3']
username2 = d['user2']
pwd2 = d['pwd2']

filename = InitData().get_file()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(username, filename)


class TestLogin(unittest.TestCase):

    def setUp(self):
        try:
            # BaseAdb.adb_intall_uiautmator()
            self.driver = Psam(version= "5.1")
        except BaseException as error:
            print("setUp启动出错！")
            self.driver.quit()
            self.fail("setUp启动出错！")

        else:
            EmailOperation(username+"@139.com", pwd).clear_forlder(['INBOX'])
            time.sleep(10)





    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)
        # AppiumServer2().stop_server()


    def testCaseLogin(self):
        '''开始登录时延测试'''
        Login(self.driver,username, pwd).login_action()


    def testCaseOnBtnLogin(self):
        '''一键登录'''
        Login(self.driver,username, pwd).one_btn_Login()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)