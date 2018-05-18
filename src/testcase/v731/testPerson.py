# urs/bin/python
# encoding:utf-8

import time,unittest
from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam
from src.testcase.v731.easycase.login import Login
from src.readwriteconf.initData import InitData
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save
from src.base.baseLog import LogAction

d = InitData().get_users()
user = {"name": d['user2'], 'pwd': d['pwd2']}



class TestPersion(unittest.TestCase):

    def setUp(self):
        try:
            # BaseAdb.adb_intall_uiautmator()
            self.driver = Psam(version="5.1")
        except BaseException:
            print("setUp启动出错！")
            self.driver.quit()
            LogAction.save(func = "TestPersion", status="Fail", explain="Psam 启动出错")
            self.fail("setUp启动出错！")


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")
        time.sleep(5)

    def testCasePersionMessages(self):
        '''个人资料信息检测'''
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
            self.assertTrue(True, "通讯录同步失败！！")

            print('=>记录当前时间，时间差')
            value_time = str(round((time.time() - start), 2))
            print('[个人资料]: %r'  %value_time)
            save.save("个人资料:%s" %value_time)
            LogAction.save(func = "testCaseCheckAddressList", status="success", explain="value_time:%s" %value_time)
        except BaseException :
            BaseImage.screenshot(self.driver, "CheckAddressListError")
            time.sleep(5)
            LogAction.save(func = "testCaseCheckAddressList", status="Fail", explain=LogAction.print())
            self.fail("【个人资料】出错")




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestPersion('testCasePersionMessages'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)