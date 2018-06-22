# urs/bin/python
# encoding:utf-8
import datetime
import time,unittest,random

from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v731.easycase.login import Login
from src.testcase.v731.easycase.send import Send
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

receiver = {'name':username, 'pwd':pwd}
sender = {'name':username2, 'pwd':pwd2}

filename = InitData().get_file()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(username, filename)


class TestSend(unittest.TestCase):
    '''邮件发送或转发是否成功'''
    def setUp(self):
        stat = ""
        try:
            BaseAdb.adb_intall_uiautmator()
            stat="Psam初始化出错"
            self.driver = Psam(version="6.0")
        except BaseException :
            self.driver.quit()
            LogAction.save(func = "TestSend", status="Fail", explain=stat)
            self.fail("setUp启动出错！")
        else:
            EmailOperation(username+"@139.com", pwd).clear_forlder(['INBOX'])
            Login(self.driver,username, pwd).login_action(is_save=False)


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")
        time.sleep(5)

    def testCaseSend(self):
        '''发送邮件'''

        Send(self.driver,username+'@139.com').send_action()

    def testCaseFwdSend(self):
        '''云端转发'''
        Send(self.driver,username+'@139.com').send_fwd()


    def testCaseReply(self):
        '''回复邮件'''
        Send(self.driver,username+'@139.com').reply(receiver,sender)

    def testCaseForward(self):
        '''SMTP转发附件'''
        Send(self.driver,username+'@139.com').forward(receiver,sender)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSend('testCaseSend'))
    suite.addTest(TestSend('testCaseFwdSend'))
    suite.addTest(TestSend('testCaseReply'))
    suite.addTest(TestSend('testCaseForward'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)