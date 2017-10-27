# urs/bin/python
# encoding:utf-8
import os,time,unittest,sys
import configparser as cparser
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam
from src.testcase.v722.easycase.login import Login

from src.base.baseImage import BaseImage

# sys.path.append(r"/Users/apple/git/pytest/")








class InitData(unittest.TestCase):

    def setUp(self):

        BaseAdb.adbIntallUiautmator()
        self.driver = Psam()
        # 点击允许
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
        BaseImage.screenshot(self.driver, "testpic")



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(InitData('testCase'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)