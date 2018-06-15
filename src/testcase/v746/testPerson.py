# urs/bin/python
# encoding:utf-8
import datetime
import time,unittest,random
from src.base.baseAdb import BaseAdb
from src.psam.psam import Psam
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import InitData
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save
from src.base.baseLog import LogAction

d = InitData().get_users()

# 主账号
if datetime.datetime.now().hour%2 == 0:
    user = {"name": d['user3'], 'pwd': d['pwd3']}
else:
    user = {"name": d['user4'], 'pwd': d['pwd4']}



class TestPersion(unittest.TestCase):
    '''个人资料是否显示正常'''
    def __init__(self,driver):
        self.driver = driver
    # def setUp(self):
    #     try:
    #         BaseAdb.adb_intall_uiautmator()
    #         self.driver = Psam(version="6.0")
    #     except BaseException:
    #         print("setUp启动出错！")
    #         self.driver.quit()
    #         LogAction.save(func = "TestPersion", status="fail", explain="Psam 启动出错")
    #         self.fail("setUp启动出错！")
    #
    #
    # #释放实例,释放资源
    # def tearDown(self):
    #     self.driver.quit()
    #     print("运行结束")
    #     time.sleep(5)

    def testCasePersionMessages(self):
        '''个人资料'''
        try:
            LogAction.print(isReset=True)

            login=Login(self.driver,user['name'], user['pwd'])
            login.login_action(is_save=False)

            LogAction.print("【验证点：页面是否存在联系人字段】")
            self.assertTrue(self.driver.get_element(u"uiautomator=>我的",10) !=None, "页面找不到联系人字段")

            LogAction.print("=>我的")
            self.driver.click(u"uiautomator=>我的")

            LogAction.print("=>个人资料")
            self.driver.click(u"uiautomator=>个人资料")


            start = time.time()
            LogAction.print("【验证点：是否获页面头像字段】")
            self.assertTrue(self.wait_for_message(), "个人资料同步失败！！")

            print('=>记录当前时间，时间差')
            value_time = str(round((time.time() - start), 2))
            print('[个人资料]: %r'  %value_time)
            save.save("个人资料:%s" %value_time)
            LogAction.save(func = "testCasePersionMessages", status="success", explain="value_time:%s" %value_time)
        except BaseException :
            BaseImage.screenshot(self.driver, "testCasePersionMessages")
            time.sleep(5)
            LogAction.save(func = "testCasePersionMessages", status="fail", explain=LogAction.print())
            self.fail("【个人资料】出错")


    def wait_for_message(self):
        '''找到需要的通知栏信息'''

        if self.driver.element_wait(u"uiautomator=>头像",10) == None:
            BaseAdb.adb_back()


        if self.driver.element_wait(u"uiautomator=>头像",2) == None:
            print('找不到了')
            return False
        else:
            return True



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestPersion('testCasePersionMessages'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)