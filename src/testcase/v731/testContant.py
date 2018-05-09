# urs/bin/python
# encoding:utf-8

import os,time,unittest,sys
from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam
from src.testcase.v731.easycase.login import Login
from src.readwriteconf.initData import InitData
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save
from src.base.baseLog import LogAction

d = InitData().get_users()
user = {"name": d['user2'], 'pwd': d['pwd2']}



class TestContant(unittest.TestCase):

    def setUp(self):
        try:

            # BaseAdb.adb_intall_uiautmator()
            self.driver = Psam(version="5.1")
        except BaseException:
            print("setUp启动出错！")
            self.driver.quit()
            LogAction.save(func = "TestContant", status="Fail", explain="Psam 启动出错")
            self.fail("setUp启动出错！")


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)

    def testCaseCheckAddressList(self):
        '''测试通讯录是否同步成功'''
        try:
            # self.assertTrue(False, "测试错误")
            LogAction.print(isReset=True)

            login=Login(self.driver,user['name'], user['pwd'])
            login.login_action(is_save=False)

            time.sleep(5)

            LogAction.print("【验证点：页面是否存在联系人字段】")
            self.assertTrue(self.driver.get_element(u"uiautomator=>联系人") !=None, "页面找不到联系人字段")

            LogAction.print("=>点击联系人")
            self.driver.click(u"uiautomator=>联系人")
            start = time.time()

            LogAction.print("【验证点：是否获取通知栏信息】")
            self.assertTrue(self.waitfor_notification(), "通讯录同步失败！！")

            print('=>记录当前时间，时间差')
            value_time = str(round((time.time() - start), 2))
            print('[联系人同步]: %r'  %value_time)
            save.save("联系人同步:%s" %value_time)
            LogAction.save(func = "testCaseCheckAddressList", status="success", explain="value_time:%s" %value_time)
        except BaseException :
            BaseImage.screenshot(self.driver, "CheckAddressListError")
            time.sleep(5)
            LogAction.save(func = "testCaseCheckAddressList", status="Fail", explain=LogAction.print())
            self.fail("【联系人同步】出错")




    def waitfor_notification(self):
        '''找到需要的通知栏信息'''
        for i in range(5):
            print("下拉通讯录列表")
            self.driver.swipe_down()
            print("检查通知栏信息")
            if BaseAdb.dumpsys_notification("同步网络联系人完成"):
                return True
            time.sleep(1)
        else:
            return False


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestContant('testCaseCheckAddressList'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)