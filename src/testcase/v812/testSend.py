# urs/bin/python
# encoding:utf-8
import unittest

from src.base.baseLog import LogAction
from src.testcase.v746.easycase.login import Login
from src.testcase.v746.easycase.send import Send
from src.readwriteconf.initData import InitData, duser

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}
sender = {'name':users["name2"], 'pwd':users["pwd2"]}


filename = InitData().get_file()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(user["name"], filename)


class TestSend(unittest.TestCase):
    '''邮件发送或转发是否成功'''
    def __init__(self,driver):
        self.driver = driver

    def testCaseSendNoAttach(self):
        '''发送邮件，无附件'''
        LogAction.print(isReset=True)
        Login(self.driver,user['name'], user['pwd']).login()
        Send(self.driver,user["name"]+'@139.com').send(subject="NoAttach",is_add=False)


    def testCaseSendAttach(self):
        '''发送邮件，带附件'''
        LogAction.print(isReset=True)
        Login(self.driver,user['name'], user['pwd']).login()
        Send(self.driver,user["name"]+'@139.com').send_action(subject="SendAttach")

    def testCaseFwdSend(self):
        '''云端转发'''
        LogAction.print(isReset=True)
        Login(self.driver,user['name'], user['pwd']).login()
        Send(self.driver,user["name"]+'@139.com').send_fwd(subject="SendAttach")


    def testCaseReply(self):
        '''回复邮件'''
        LogAction.print(isReset=True)
        Login(self.driver,user['name'], user['pwd']).login()
        Send(self.driver,user["name"]+'@139.com').reply(subject="NoAttach")

    def testCaseForward(self):
        '''SMTP转发附件'''
        LogAction.print(isReset=True)
        Login(self.driver,user['name'], user['pwd']).login()
        Send(self.driver,user["name"]+'@139.com').forward(subject="NoAttach")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSend('testCaseSend'))
    suite.addTest(TestSend('testCaseFwdSend'))
    suite.addTest(TestSend('testCaseReply'))
    suite.addTest(TestSend('testCaseForward'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)