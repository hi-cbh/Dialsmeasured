# urs/bin/python
# encoding:utf-8

import os,time,unittest
from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam
from src.readwriteconf.initData import InitData
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction

d= InitData().get_users()
print(d)
user = {"name": d['user2'], 'pwd': d['pwd2']}

print(user)

class TestSpeed(unittest.TestCase):

    def setUp(self):
        try:
            time.sleep(10)
            BaseAdb.adb_clear('org.zwanoo.android.speedtest')
            time.sleep(5)
            BaseAdb.adb_intall_uiautmator()
            self.driver = Psam(version='5.1',app_pkg="org.zwanoo.android.speedtest",app_activity="com.ookla.speedtest.softfacade.MainActivity")
        except BaseException:
            print("setUp启动出错！")
            self.driver.quit()
            LogAction.save(func = "TestSpeed", status="Fail", explain="setUp error")
            self.fail("setUp启动出错！")


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)
        # AppiumServer2().stop_server()


    def testCase(self):
        '''网络测速'''

        try:
            network = BaseAdb.get_network_type()


            for i in range(1,5):
                print("重置app")
                self.driver.reset()
                time.sleep(10)

                print("重启测试工具")
                if self.driver.get_display("xpath=>//android.widget.TextView[contains(@text,'Begin Test')]") == False:
                    continue

                self.driver.click("xpath=>//android.widget.TextView[contains(@text,'Begin Test')]")
                time.sleep(30)


                if self.driver.get_display("id=>org.zwanoo.android.speedtest:id/downloadSpeed") == False:
                    continue


                load = self.driver.get_element('id=>org.zwanoo.android.speedtest:id/downloadSpeed',10).get_attribute('text')


                if self.driver.get_display("id=>org.zwanoo.android.speedtest:id/downloadSpeed") == False:
                    continue

                down = self.driver.get_element('id=>org.zwanoo.android.speedtest:id/uploadSpeed',10).get_attribute('text')


                print('上传: %s ' %load)
                print('下载: %s ' %down)

                time.sleep(3)
                return network +'状态，网速测试结果如下，上传 ' + load + ' , 下载 ' + down

        except BaseException as error:
            BaseImage.screenshot(self.driver, "testSeep")
            time.sleep(5)
            LogAction.save(func = "TestSpeed", status="Fail", explain="testSeep error")
            self.fail("【网络测速】出错！")
        finally:
            BaseAdb.adb_home()
            BaseAdb.adb_clear('org.zwanoo.android.speedtest')





if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSpeed('testCase'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

