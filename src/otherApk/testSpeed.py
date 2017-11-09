# urs/bin/python
# encoding:utf-8

import os,time,unittest
import configparser as cparser
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v722.easycase.login import Login
from src.testcase.v722.initData import InitData
from src.base.baseImage import BaseImage

# sys.path.append(r"/Users/apple/git/pytest/")

d= InitData().getUsers()
print(d)
user = {"name": d['user2'], 'pwd': d['pwd2']}

print(user)

class TestSpeed(unittest.TestCase):

    def setUp(self):
        try:
            # time.sleep(10)
            # AppiumServer2().start_server()
            # time.sleep(10)

            BaseAdb.adbIntallUiautmator()
            self.driver = Psam("org.zwanoo.android.speedtest","com.ookla.speedtest.softfacade.MainActivity")
        except BaseException as error:
            print("setUp启动出错！")


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)
        # AppiumServer2().stop_server()


    def testCase(self):
        '''网络测速'''

        try:
            network = BaseAdb.getNetworkType()

            self.driver.click("xpath=>//android.widget.TextView[contains(@text,'Begin Test')]")
            time.sleep(30)

            load = self.driver.get_element('id=>org.zwanoo.android.speedtest:id/downloadSpeed').get_attribute('text')
            down = self.driver.get_element('id=>org.zwanoo.android.speedtest:id/uploadSpeed').get_attribute('text')


            print('上传: %s ' %load)
            print('下载: %s ' %down)

            time.sleep(3)

        except BaseException as error:
            BaseImage.screenshot(self.driver, "testSeep")
            time.sleep(5)
            self.fail("【网络测速】出错！")


        else:
            BaseAdb.adbHome()
            return network +'状态，网速测试结果如下，上传 ' + load + ' , 下载 ' + down


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSpeed('testCase'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

