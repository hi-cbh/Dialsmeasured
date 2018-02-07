# urs/bin/python
# encoding:utf-8

import time,unittest
from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v731.easycase.login import Login
from src.testcase.v731.easycase.send import Send
from src.readwriteconf.initData import InitData
from src.testcase.v731.easycase.openDown import OpenDown


d = InitData().get_users()

username = d['user3']
pwd = d['pwd3']
username2 = d['user2']
pwd2 = d['pwd2']

receiver = {'name':username, 'pwd':pwd}
sender = {'name':username2, 'pwd':pwd2}

filename = InitData().get_file()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(username, filename)


class TestDownFile(unittest.TestCase):

    def setUp(self):
        try:
            # BaseAdb.adb_intall_uiautmator()
            self.driver = Psam(version="5.1")
        except BaseException :
            print("setUp启动出错！")
            self.driver.quit()
            self.fail("setUp启动出错！")

        else:
            EmailOperation(username+"@139.com", pwd).clear_forlder(['INBOX'])
            time.sleep(10)

            Login(self.driver,username, pwd).login_action(is_save=False)




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
        send.send_action()

        # 打开附件
        od = OpenDown(self.driver, path, filename)
        # 打开附件
        od.open_action()
        # 下载附件
        od.down_action()





if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestDownFile('testDownFile'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)