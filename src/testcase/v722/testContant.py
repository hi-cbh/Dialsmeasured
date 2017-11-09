# urs/bin/python
# encoding:utf-8

import os,time,unittest,sys
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam
from src.testcase.v722.easycase.login import Login
from src.testcase.v722.initData import InitData
from src.base.baseImage import BaseImage
# sys.path.append(r"/Users/apple/git/pytest/")

d = InitData().getUsers()
user = {"name": d['user2'], 'pwd': d['pwd2']}



class TestContant(unittest.TestCase):

    def setUp(self):
        try:
            # time.sleep(10)
            # AppiumServer2().start_server()
            # time.sleep(10)

            BaseAdb.adbIntallUiautmator()
            self.driver = Psam()
        except BaseException as error:
            print("setUp启动出错！")
            self.driver.quit()
            self.fail("setUp启动出错！")


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)
        # AppiumServer2().stop_server()


    def testCaseCheckAddressList(self):
        '''测试通讯录是否同步成功'''
        try:
            # self.assertTrue(False, "测试错误")

            login=Login(self.driver,user['name'], user['pwd'])
            login.loginAction()

            time.sleep(5)

            print("验证点：页面是否存在联系人字段")
            self.assertTrue(self.driver.get_element(u"uiautomator=>联系人") !=None, "页面找不到联系人字段")

            print("=>点击联系人")
            self.driver.click(u"uiautomator=>联系人")

            print("验证点：是否获取通知栏信息")
            self.assertTrue(self.waitforNotification(),"通讯录同步失败！！")
        except BaseException :
            BaseImage.screenshot(self.driver, "CheckAddressListError")
            time.sleep(5)

            self.fail("【联系人同步】出错")




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