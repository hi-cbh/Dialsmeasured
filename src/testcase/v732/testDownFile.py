# urs/bin/python
# encoding:utf-8

import os,time,unittest
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v732.easycase.login import Login
from src.testcase.v732.easycase.send import Send
from src.readwriteconf.initData import InitData
from src.testcase.v732.easycase.openDown import OpenDown

# sys.path.append(r"/Users/apple/git/pytest/")

d = InitData().getUsers()

username = d['user1']
pwd = d['pwd1']
username2 = d['user2']
pwd2 = d['pwd2']

receiver = {'name':username, 'pwd':pwd}
sender = {'name':username2, 'pwd':pwd2}

filename = InitData().getFile()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(username, filename)


class TestDownFile(unittest.TestCase):

    def setUp(self):
        try:
            # time.sleep(10)
            # AppiumServer2().start_server()
            # time.sleep(10)

            BaseAdb.adbIntallUiautmator()
            self.driver = Psam()
        except BaseException as error:
            print("setUp启动出错！")
            self.driver.quit()
            self.fail("setUp启动出错！")

        else:
            EmailOperation(username+"@139.com", pwd).clearForlder(['INBOX'])
            time.sleep(10)

            login=Login(self.driver,username, pwd)
            login.loginAction()




    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)
        # AppiumServer2().stop_server()

    def testDownFile(self):
        '''下载附件'''
        # 发送带附件邮件
        send = Send(self.driver,username+'@139.com')
        send.sendAction()

        # 打开附件
        od = OpenDown(self.driver, path, filename)
        # 打开附件
        od.openAction()
        # 下载附件
        od.downAction()





if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestDownFile('testDownFile'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)