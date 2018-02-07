# urs/bin/python
# encoding:utf-8

import os,time,unittest
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v731.easycase.login import Login
from src.testcase.v731.easycase.receive import WebReceive
from src.mail.sendEmailSmtp import SendMail
from src.readwriteconf.initData import InitData
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save

# sys.path.append(r"/Users/apple/git/pytest/")

d = InitData().get_users()
user1 = {"name": d['user3'], 'pwd': d['pwd3']} # 发送者
user2 = {"name": d['user2'], 'pwd': d['pwd2']} # 接收者

'''
用户没有做到参数化

'''

class TestPush(unittest.TestCase):
    '''
    错误后重跑，使用两个账号
    '''
    def setUp(self):
        try:
            # BaseAdb.adb_intall_uiautmator()
            self.driver = Psam(version="5.1")
        except BaseException :
            print("setUp启动出错！")
            self.driver.quit()
            self.fail("setUp启动出错！")
        else:
            EmailOperation(user2['name']+"@139.com", user2['pwd']).seen()
            time.sleep(10)


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)

    def testCasePush(self):
        '''推送测试测试'''
        self.push_action(user1, user2)



    def push_action(self, sender, reveicer):
        '''推送测试测试方法'''

        try:
            # self.assertTrue(False,"测试")
            print("=>登录")
            Login(self.driver,reveicer['name'], reveicer['pwd']).login_action(is_save=False)

            print('=>注销账号')
            self.logout()

            print("=>重新登录")
            Login(self.driver,reveicer['name'], reveicer['pwd']).login_action(is_save=False)


            print("=>点击Home键")
            BaseAdb.adb_home()
            time.sleep(5)

            print("=>第三方发送邮件")
            s = SendMail(sender['name'], sender['pwd'], reveicer['name'])
            self.assertTrue(s.send_mail_test('sendsmtpEmail','测试邮件...'),"邮件发送失败")
            start = time.time()
            # time.sleep(10)

            print("验证点：等待推送信息")
            self.assertTrue(self.wait_for_notification(), "接收推送失败")

            print('=>记录当前时间，时间差')
            value_time = str(round((time.time() - start), 2))
            print('[接收推送]: %r'  %value_time)
            save.save("接收推送:%s" %value_time)



        except BaseException:
            BaseImage.screenshot(self.driver, "PushError")
            time.sleep(5)

            self.fail("【接收邮件推送】出错！")

        else:
            app_package = "cn.cj.pe"  # 程序的package
            app_activity = "com.mail139.about.LaunchActivity"  # 程序的Activity

            time.sleep(2)
            BaseAdb.adb_start_app(app_package, app_activity)
            time.sleep(5)




    def logout(self):
        '''注销账户'''
        time.sleep(2)
        print('=>点击 我的')
        self.driver.click(u"uiautomator=>我的")
        time.sleep(2)
        print('=>点击 设置')
        self.driver.click(u"uiautomator=>设置")
        time.sleep(2)

        print('=>点击 账号')
        self.driver.click(r"id=>cn.cj.pe:id/account_name")
        time.sleep(2)

        print('=>点击 退出账号')
        self.driver.click(u"uiautomator=>退出账号")
        time.sleep(2)

        print('=>点击 确定')
        self.driver.click(u"uiautomator=>确定")
        time.sleep(10)


    def wait_for_notification(self):
        '''找到需要的通知栏信息'''
        for i in range(10):
            print("检查通知栏信息")
            if BaseAdb.dumpsys_notification("新邮件") == True :
                print('找到了')
                return True
            time.sleep(10)
        print('找不到了')
        return False



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestPush('testCasePush'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)