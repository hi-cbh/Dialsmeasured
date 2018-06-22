# urs/bin/python
# encoding:utf-8
import unittest

from src.base.baseAdb import BaseAdb
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import InitData, duser
from src.testcase.v746.easycase.openDown import OpenDown


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
        Login(self.driver,user['name'], user['pwd']).login()
        # 打开附件
        od = OpenDown(self.driver, path, filename)
        # 下载附件
        od.down_action("SendAttach")
        BaseAdb.adb_back()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestDownFile('testDownFile'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)