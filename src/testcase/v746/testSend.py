# urs/bin/python
# encoding:utf-8
import datetime
import time,unittest,random

from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v746.easycase.login import Login
from src.testcase.v746.easycase.send import Send
from src.readwriteconf.initData import InitData, duser
from src.base.baseLog import LogAction

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}
sender = {'name':users["name2"], 'pwd':users["pwd2"]}


filename = InitData().get_file()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(user["name"], filename)


class TestSend(unittest.TestCase):
    '''邮件发送或转发是否成功'''
    def __init__(self,driver):
        self.driver = driver

    # def setUp(self):
    #     stat = ""
    #     try:
    #         BaseAdb.adb_intall_uiautmator()
    #         stat="Psam初始化出错"
    #         self.driver = Psam(version="6.0")
    #     except BaseException :
    #         self.driver.quit()
    #         LogAction.save(func = "TestSend", status="Fail", explain=stat)
    #         self.fail("setUp启动出错！")
    #     else:
    #         EmailOperation(username+"@139.com", pwd).clear_forlder(['INBOX'])
    #         Login(self.driver,username, pwd).login_action(is_save=False)

    #
    # #释放实例,释放资源
    # def tearDown(self):
    #     self.driver.quit()
    #     print("运行结束")
    #     time.sleep(5)

    def testCaseSendNoAttach(self):
        '''发送邮件，无附件'''
        Login(self.driver,user['name'], user['pwd']).login()
        Send(self.driver,user["name"]+'@139.com').send(subject="NoAttach",is_add=False)


    def testCaseSendAttach(self):
        '''发送邮件，带附件'''
        Login(self.driver,user['name'], user['pwd']).login()
        Send(self.driver,user["name"]+'@139.com').send_action(subject="SendAttach")

    def testCaseFwdSend(self):
        '''云端转发'''
        Login(self.driver,user['name'], user['pwd']).login()
        Send(self.driver,user["name"]+'@139.com').send_fwd(subject="SendAttach")


    def testCaseReply(self):
        '''回复邮件'''
        Login(self.driver,user['name'], user['pwd']).login()
        Send(self.driver,user["name"]+'@139.com').reply(subject="NoAttach")

    def testCaseForward(self):
        '''SMTP转发附件'''
        Login(self.driver,user['name'], user['pwd']).login()
        Send(self.driver,user["name"]+'@139.com').forward(subject="NoAttach")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(TestSend('testCaseSend'))
    suite.addTest(TestSend('testCaseFwdSend'))
    # suite.addTest(TestSend('testCaseReply'))
    # suite.addTest(TestSend('testCaseForward'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)