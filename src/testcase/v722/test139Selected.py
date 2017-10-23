# urs/bin/python
# encoding:utf-8

import os,time,unittest
import configparser as cparser
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v722.easycase.login import Login

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

user2 = {"name": username, 'pwd': pwd}
user1 = {"name": username2, 'pwd': pwd2}

##====================


class TestSelect(unittest.TestCase):

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

    def testCaseSelected(self):
        '''测试139精选'''

        try:
            print("=>登录")
            Login(self.driver,user1['name'], user1['pwd']).loginAction()

            time.sleep(10)
            print("首先通过http协议，访问链接是否更改，再运行")

            print("验证页面是饭后存在139精选")
            self.assertTrue(self.driver.get_element(u'uiautomator=>139精选'),'页面没有139精选')

            print('点击 139精选')
            self.driver.click(u'uiautomator=>139精选')

            print("等待10秒")
            time.sleep(10)

            print('验证点：页面是否显示正常')
            self.assertTrue(self.driver.page_source().__contains__(u"阅读全文"),"页面显示不正常")

            # print('=>注销账号')
            # self.logout()


        except BaseException as error:
            self.fail("测试139精选过程中出错！")

    def logout(self):
        '''注销账户'''
        time.sleep(2)
        print('=>点击 我的')
        self.driver.click(u"uiautomator=>我的")
        time.sleep(2)
        print('=>点击 设置')
        self.driver.click(u"uiautomator=>设置")
        time.sleep(2)

        print('=>点击 账号')
        self.driver.click(r"id=>cn.cj.pe:id/account_name")
        time.sleep(2)

        print('=>点击 注销账号')
        self.driver.click(u"uiautomator=>注销账号")
        time.sleep(2)

        print('=>点击 确定')
        self.driver.click(u"uiautomator=>确定")
        time.sleep(10)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSelect('testCaseSelected'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)