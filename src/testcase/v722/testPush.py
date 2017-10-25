# urs/bin/python
# encoding:utf-8

import os,time,unittest
from src.aserver.AppiumServer import AppiumServer2
from src.base.baseAdb import BaseAdb
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v722.easycase.login import Login
from src.testcase.v722.easycase.receive import WebReceive
from src.mail.sendEmailSmtp import SendMail
from src.testcase.v722.initData import InitData


# sys.path.append(r"/Users/apple/git/pytest/")

d = InitData().getUsers()
user1 = {"name": d['user1'], 'pwd': d['pwd1']} # 发送者
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
            # time.sleep(10)
            # AppiumServer2().start_server()
            # time.sleep(10)

            BaseAdb.adbIntallUiautmator()
            self.driver = Psam("6.0")
        except BaseException as error:
            print("setUp启动出错！")

        else:
            EmailOperation(user2['name']+"@139.com", user2['pwd']).seen()
            time.sleep(10)


    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()
        print("运行结束")

        time.sleep(5)
        # AppiumServer2().stop_server()

    def testCasePush(self):
        '''推送测试测试'''
        self.Push(user1, user2)



    def Push(self, sender, reveicer):
        '''推送测试测试方法'''

        try:
            print("=>登录")
            Login(self.driver,reveicer['name'], reveicer['pwd']).loginAction()

            print('=>注销账号')
            self.logout()

            print("=>重新登录")
            Login(self.driver,reveicer['name'], reveicer['pwd']).loginAction()


            print("=>点击Home键")
            BaseAdb.adbHome()
            time.sleep(5)

            # print("=>Web端发送邮件")
            # self.assertTrue(self.receive(),"邮件发送失败")
            print("=>第三方发送邮件")
            s = SendMail(sender['name'], sender['pwd'], reveicer['name'])
            self.assertTrue(s.sendMail('sendsmtpEmail','测试邮件...'),"邮件发送失败")
            time.sleep(10)

            print("验证点：等待推送信息")
            self.assertTrue(self.waitforNotification(),"接收推送失败")
        except BaseException as error:
            self.fail("【接收邮件推送】出错！")

        else:
            appPackage = "cn.cj.pe"  # 程序的package
            appActivity = "com.mail139.about.LaunchActivity"  # 程序的Activity

            time.sleep(2)
            BaseAdb.adbStartApp(appPackage,appActivity)
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

        print('=>点击 注销账号')
        self.driver.click(u"uiautomator=>注销账号")
        time.sleep(2)

        print('=>点击 确定')
        self.driver.click(u"uiautomator=>确定")
        time.sleep(10)


    # def receive(self):
    #     '''接收邮件'''
    #     r = WebReceive(sender['name'], sender['pwd'], receiver['name'] +'@139.com')
    #     return r.sendEmail()

    def waitforNotification(self):
        '''找到需要的通知栏信息'''
        for i in range(3):
            print("检查通知栏信息")
            if BaseAdb.dumpsysNotification("新邮件") == True :
                print('找到了')
                return True
            time.sleep(20)
        print('找不到了')
        return False



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestPush('testCasePush'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)