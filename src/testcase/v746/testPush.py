# urs/bin/python
# encoding:utf-8
import time,unittest

from src.readwriteconf.rwconf import ReadWriteConfFile
from src.base.baseAdb import BaseAdb
from src.testcase.v746.easycase.login import Login
from src.mail.sendEmailSmtp import SendMail
from src.readwriteconf.initData import duser
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}
sender = {"name": users['name2'], 'pwd': users['pwd2']} # 接收者，改为发送者
is_status=ReadWriteConfFile.get_status_value()
'''
用户没有做到参数化

'''

class TestPush(unittest.TestCase):
    '''推送测试'''
    def __init__(self,driver):
        self.driver = driver

    def testCasePush(self):
        '''推送'''
        try:
            LogAction.print(isReset=True)
            Login(self.driver,user['name'], user['pwd']).login()
            LogAction.print("=>点击Home键")
            BaseAdb.adb_home()
            time.sleep(2)

            LogAction.print("=>第三方发送邮件")
            s = SendMail(sender['name'], sender['pwd'], user['name'])

            LogAction.print("=>【邮件发送】")
            self.assertTrue(s.send_mail_test('sendsmtpEmail','测试邮件...'),"邮件发送失败")
            time.sleep(5)
            LogAction.print("=>邮件成功")
            time.sleep(5)
            LogAction.print("=>【等待推送】")
            self.assertTrue(self.wait_for_notification(), "接收推送失败")

            app_package = "cn.cj.pe"  # 程序的package
            app_activity = "com.mail139.about.LaunchActivity"  # 程序的Activity

            time.sleep(2)
            BaseAdb.adb_start_app(app_package, app_activity)
            time.sleep(5)
            LogAction.save(func = "testCasePush", status="success", explain=LogAction.print())
            ReadWriteConfFile.value_set_zero("testCasePush")
        except BaseException:
            ReadWriteConfFile.value_add_one("testCasePush")
            BaseImage.screenshot(self.driver, "PushError")
            time.sleep(2)
            LogAction.save(func = "testCasePush", status="fail", explain=LogAction.print())

            if is_status:
                self.fail("【接收邮件推送】出错！")



    def logout(self):
        '''注销账户'''
        time.sleep(2)
        LogAction.print('=>点击 我的')
        self.driver.click(u"uiautomator=>我的")
        time.sleep(2)
        LogAction.print('=>点击 设置')
        self.driver.click(u"uiautomator=>设置")
        time.sleep(2)

        LogAction.print('=>点击 账号')
        self.driver.click(r"id=>cn.cj.pe:id/account_name")
        time.sleep(2)

        LogAction.print('=>点击 退出账号')
        self.driver.click(u"uiautomator=>退出账号")
        time.sleep(2)

        LogAction.print('=>点击 确定')
        self.driver.click(u"uiautomator=>确定")
        time.sleep(5)


    def wait_for_notification(self):
        '''找到需要的通知栏信息'''
        for i in range(10):
            print("检查通知栏信息")
            if BaseAdb.dumpsys_notification("新邮件") == True :
                print('找到了')
                return True
            time.sleep(9)
        print('找不到了')
        return False

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestPush('testCasePush'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)