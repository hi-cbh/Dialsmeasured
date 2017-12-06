# urs/bin/python
# encoding:utf-8
import os,time,unittest,sys
import configparser as cparser
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam
from src.testcase.v732.easycase.login import Login


# sys.path.append(r"/Users/apple/git/pytest/")

# ======== Reading user_db.ini setting ===========
base_dir = str((os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
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






class InitData(unittest.TestCase):

    def setUp(self):

        # AppiumServer2().start_server()
        time.sleep(10)

        BaseAdb.adbIntallUiautmator()
        self.driver = Psam()
        # 点击允许
        self.driver.click(u"uiautomator=>允许")
        time.sleep(4)


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")
        time.sleep(5)
        # AppiumServer2().stop_server()


    def testCase(self):

        network = BaseAdb.getNetworkType()
        print('当前网络状态：%s' %network)

        runtimes = 2

        for x in range(1,runtimes):

            print('当前运行次数为：%r' %(str(x)))

            try:
                stat = u'开始登录时延测试'
                login=Login(self.driver,username, pwd)
                login.loginAction(firstLogin=True)

            except BaseException as be:
                print("运行到：%s 运行出错" %stat)
                print(be)

        BaseAdb.adbHome()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(InitData('testCase'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)