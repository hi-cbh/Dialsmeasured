# urs/bin/python
# encoding:utf-8
import datetime
import time,unittest,random

from src.base.baseAdb import BaseAdb
from src.base.baseLog import LogAction
from src.psam.psam import Psam
from src.testcase.v746.easycase.login import Login
from src.testcase.v746.easycase.send import Send
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
    # def setUp(self):
    #     stat=""
    #     try:
    #         BaseAdb.adb_intall_uiautmator()
    #         stat="Pasm初始化出错"
    #         self.driver = Psam(version="6.0")
    #
    #         stat = "账号登录出错"
    #         Login(self.driver,username, pwd).login_action(is_save=False)
    #
    #     except BaseException :
    #         print("setUp启动出错！")
    #         self.driver.quit()
    #         LogAction.save(func = "TestDownFile", status="fail", explain=stat)
    #         self.fail("setUp启动出错！")
    #
    #
    # #释放实例,释放资源
    # def tearDown(self):
    #     self.driver.quit()
    #     print("运行结束")
    #
    #     time.sleep(5)

    def testDownFile(self):
        '''下载附件'''
        # 发送带附件邮件
        # send = Send(self.driver,username+'@139.com')
        # send.send_action()
        Login(self.driver,user['name'], user['pwd']).login()
        # 打开附件
        od = OpenDown(self.driver, path, filename)
        # 下载附件
        od.down_action("SendAttach")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestDownFile('testDownFile'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)