# urs/bin/python
# encoding:utf-8

import os,time,unittest,sys
import configparser as cparser
from src.base.baseTime import BaseTime
from src.db.sqlhelper import SQLHelper
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v722.easycase.login import Login
from src.testcase.v722.easycase.openDown import OpenDown
from src.testcase.v722.easycase.receive import Receive
from src.testcase.v722.easycase.send import Send


# sys.path.append(r"/Users/apple/git/pytest/")

# ======== Reading user_db.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
file_path = base_dir + "/user_db.ini"

cf = cparser.ConfigParser()
cf.read(file_path)

username = cf.get("userconf", "user1")
pwd = cf.get("userconf", "pwd1")
username2 = cf.get("userconf", "user2")
pwd2 = cf.get("userconf", "pwd2")
filename = cf.get("userconf", "filename")
path = r'/mnt/sdcard/139PushEmail/download/%s@139.com/*%s.rar'  %(username, filename)

versionID = cf.get("verconf", "versionid")

##====================


class TestContant(unittest.TestCase):

    def setUp(self):
        try:
            # time.sleep(10)
            # AppiumServer2().start_server()
            # time.sleep(10)

            BaseAdb.adbIntallUiautmator()
            self.driver = Psam("6.0")
        except BaseException as error:
            print("setUp启动出错！")


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)
        # AppiumServer2().stop_server()


    def testCaseCheckAddressList(self):
        '''测试通讯录是否同步成功'''
        login=Login(self.driver,username, pwd)
        login.loginAction()

        time.sleep(5)

        print("验证点：页面是否存在联系人字段")
        self.assertTrue(self.driver.get_element(u"uiautomator=>联系人") !=None, "页面找不到联系人字段")

        print("=>点击联系人")
        self.driver.click(u"uiautomator=>联系人")

        print("验证点：是否获取通知栏信息")
        self.assertTrue(self.waitforNotification(),"通讯录同步失败！！")




    def waitforNotification(self):
        '''找到需要的通知栏信息'''
        for i in range(5):
            print("下拉通讯录列表")
            self.driver.swipeDown()
            print("检查通知栏信息")
            if BaseAdb.dumpsysNotification("同步网络联系人完成"):
                return True
            time.sleep(3)
        else:
            return False


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestContant('testCaseCheckAddressList'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)