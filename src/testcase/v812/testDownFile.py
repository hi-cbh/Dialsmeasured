# urs/bin/python
# encoding:utf-8
import unittest

from src.base.baseLog import LogAction
from src.testcase.v812.easycase.login import Login
from src.readwriteconf.initData import InitData, duser
from src.testcase.v812.easycase.openDown import OpenDown
from src.testcase.v812.easycase.send import Send

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}

filename = InitData().get_file()['filename']

path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(user["name"], filename)


class TestDownFile(unittest.TestCase):
    '''下载附件是否成功'''
    def __init__(self,driver):
        self.driver = driver

    def testDownFile(self):
        '''下载附件'''
        LogAction.print(isReset=True)
        Login(self.driver,user['name'], user['pwd']).login()

        print("判断是否存在邮件")
        if self.driver.element_wait("uiautomator=>SendAttach") == None:
            Send(self.driver,user["name"]+'@139.com').send_action(subject="SendAttach")

        # 打开附件
        od = OpenDown(self.driver, path, filename)
        # 下载附件
        od.down_action("SendAttach")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestDownFile('testDownFile'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)