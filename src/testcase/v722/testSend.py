# urs/bin/python
# encoding:utf-8

import os,time,unittest
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v722.easycase.login import Login
from src.testcase.v722.easycase.send import Send
from src.testcase.v722.initData import InitData

# sys.path.append(r"/Users/apple/git/pytest/")

d = InitData().getUsers()

username = d['user1']
pwd = d['pwd1']
username2 = d['user2']
pwd2 = d['pwd2']

filename = InitData().getFile()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(username, filename)


class TestSend(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        try:
            # time.sleep(10)
            # AppiumServer2().start_server()
            # time.sleep(10)

            BaseAdb.adbIntallUiautmator()
            self.driver = Psam("6.0")
        except BaseException as error:
            print("setUp启动出错！")

        else:
            EmailOperation(username+"@139.com", pwd).clearForlder(['INBOX'])
            time.sleep(10)


    #释放实例,释放资源
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)
        # AppiumServer2().stop_server()


    def testCaseLogin(self):
        '''开始登录时延测试'''
        login=Login(self.driver,username, pwd)
        login.loginAction()


    def testCaseSend(self):
        '''发送邮件测试'''
        send = Send(self.driver,username+'@139.com')
        send.sendAction()

    def testCaseFwdSend(self):
        '''转发邮件测试'''
        send = Send(self.driver,username+'@139.com')
        send.sendFwd()




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSend('testCaseLogin'))
    suite.addTest(TestSend('testCaseSend'))
    suite.addTest(TestSend('testCaseFwdSend'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)