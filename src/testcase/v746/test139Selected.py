# urs/bin/python
# encoding:utf-8

import time,unittest
from src.psam.psam import Psam
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import InitData
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save
from src.base.baseLog import LogAction
from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation

d= InitData().get_users()

user = {"name": d['user2'], 'pwd': d['pwd2']}

class TestSelect(unittest.TestCase):
    '''139精选是否显示正常'''

    def __init__(self,driver):
        self.driver = driver
    # def setUp(self):
    #     try:
    #         BaseAdb.adb_intall_uiautmator()
    #         # self.driver = Psam()
    #         self.driver = Psam(version="6.0")
    #     except BaseException:
    #         print("setUp启动出错！")
    #         LogAction.save(func = "TestSelect", status="fail", explain="Psam 启动出错")
    #         self.fail("setUp启动出错！")
    #
    #
    # #释放实例,释放资源
    # def tearDown(self):
    #     self.driver.quit()
    #     print("运行结束")
    #
    #     time.sleep(5)

    def testCaseSelected(self, ):
        '''收件箱列表139精选'''

        try:
            EmailOperation(user['name']+"@139.com", user['pwd']).clear_forlder([u'已删除', u'已发送'])
            EmailOperation(user['name']+"@139.com", user['pwd']).check_inbox()
            EmailOperation(user['name']+"@139.com", user['pwd']).seen()

            LogAction.print(isReset=True)
            LogAction.print("=>账号登录")
            Login(self.driver,user['name'], user['pwd']).login_action(is_save=False)

            LogAction.print("=>加载本地邮件")
            timeout = int(round(time.time() * 1000)) + 30 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :
                if self.driver.element_wait(u'uiautomator=>139精选',2) == None:
                    print("下拉")
                    self.driver.swipe_down()
                    time.sleep(1)
                    self.driver.swipe_down()
                else:
                    break


            LogAction.print("【验证点：页面是否存在139精选】")
            self.assertTrue(self.driver.get_element(u'uiautomator=>139精选',10),'收件箱列表没有139精选')

            # 等待
            time.sleep(5)


            # 经常出现误报
            for i in range(3):
                if self.driver.get_element(u'uiautomator=>139精选',3) != None:
                    LogAction.print('=>点击139精选')
                    self.driver.click(u'uiautomator=>139精选')


            start = time.time()


            LogAction.print("=>等待30秒")
            # 等待两分钟
            timeout = int(round(time.time() * 1000)) + 60 * 1000
            try:
                while (int(round(time.time() * 1000) < timeout)):

                    if self.driver.page_source().__contains__(u"阅读全文") == True:
                        # print('find it')
                        break
                    time.sleep(1)
                    # print("超时")
            except BaseException as msg:
                print(msg)


            LogAction.print('【验证点：页面是否显示正常】')
            self.assertTrue(self.driver.page_source().__contains__(u"阅读全文"),"页面显示不正常")

            print('=>记录当前时间，时间差')
            value_time = str(round((time.time() - start), 2))

            print('[139精选出现时间]: %r'  %value_time)
            save.save("收件箱列表中精选:%s" %value_time)
            LogAction.save(func = "testCaseSelected", status="success", explain="value_time:%s" %value_time)
        except BaseException:
            BaseImage.screenshot(self.driver, "Case139SelectedError")
            time.sleep(5)
            LogAction.save(func = "testCaseSelected", status="fail", explain=LogAction.print())
            self.fail("【139精选】出错！")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSelect('testCaseSelected'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)