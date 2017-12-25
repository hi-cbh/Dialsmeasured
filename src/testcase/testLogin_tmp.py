# urs/bin/python
# encoding:utf-8

import os,time,unittest,sys

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("path: %s" %p)
sys.path.append(p+"/")

from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam



class TestLogin(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = Psam(version="5.0")
        except BaseException:
            print("setUp启动出错！")


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")


    def testCaseLogin(self):
        '''开始登录时延测试'''
        try:
            '''最基础的登录'''
            self.driver.reset()

            time.sleep(4)

            self.driver.click(r"uiautomator=>开始使用")
            time.sleep(2)
            self.driver.swipe_right()
            self.driver.swipe_right()
            self.driver.swipe_right()
            print("点击坐标")
            w = self.driver.get_window_size()['width']
            h = self.driver.get_window_size()['height']
            print(h)
            # BaseAdb.adb_tap(w / 2, int(h * 0.899))
            BaseAdb.adb_tap(w / 2, int(h * 0.92))
            # BaseAdb.adbTap(500, 1700) #其他手机需要调试
            time.sleep(4)

            print('=>选择139邮箱')
            self.driver.click(r"xpath=>//android.widget.ImageView[@index='0']")

            self.driver.click(r"id=>cn.cj.pe:id/sm_login")

            print('验证点：等待收件箱底部导航栏出现')
            self.assertTrue(self.driver.get_element("id=>cn.cj.pe:id/message_list_bottom_email") != None, "登录失败！")


        except BaseException as error:
            # 超时，数据超时
            time.sleep(5)



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('testCaseLogin'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    print("end")