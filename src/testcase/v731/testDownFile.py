# urs/bin/python
# encoding:utf-8
import datetime
import time,unittest,random
from src.base.baseLog import LogAction
from src.psam.psam import Psam
from src.testcase.v731.easycase.login import Login
from src.testcase.v731.easycase.send import Send
from src.readwriteconf.initData import InitData
from src.testcase.v731.easycase.openDown import OpenDown


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


class TestDownFile(unittest.TestCase):
    '''下载附件是否成功'''
    def setUp(self):
        stat=""
        try:
            # BaseAdb.adb_intall_uiautmator()
            stat="Pasm初始化出错"
            self.driver = Psam(version="5.1")

            stat = "账号登录出错"
            Login(self.driver,username, pwd).login_action(is_save=False)

        except BaseException :
            print("setUp启动出错！")
            self.driver.quit()
            LogAction.save(func = "TestDownFile", status="Fail", explain=stat)
            self.fail("setUp启动出错！")





    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)

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