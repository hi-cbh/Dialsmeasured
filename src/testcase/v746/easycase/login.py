# urs/bin/python
# encoding:utf-8

from time import sleep,time
import unittest
from src.base.baseAdb import BaseAdb
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction
class Login(unittest.TestCase):
    '''当前版本没有添加弹窗广告'''
    def __init__(self,driver, username, pwd):
        self.username = username
        self.pwd = pwd
        self.driver = driver

    def login(self):
        '''判断是否在收件箱页面，否则重新登录'''
        # 判断是否在收件箱页面
        if self.driver.current_app().__contains__(".activity.MessageList"):
            BaseAdb.adb_start_app("cn.cj.pe","com.mail139.about.LaunchActivity")
            # print("在主页")
            sleep(6)
            self.driver.click(u"uiautomator=>邮件")
            return

        # 杀进程，重启
        BaseAdb.adb_stop("cn.cj.pe")
        sleep(3)
        BaseAdb.adb_start_app("cn.cj.pe","com.mail139.about.LaunchActivity")
        sleep(6)

        # 如果页面不在收集箱页面，清除缓存登录
        if self.driver.current_app().__contains__(".activity.MessageList"):
            BaseAdb.adb_start_app("cn.cj.pe","com.mail139.about.LaunchActivity")
            # print("在主页")
            sleep(6)
            self.driver.click(u"uiautomator=>邮件")
        else:
            # 杀进程启动，清除缓存，重新登录
            BaseAdb.adb_home()
            BaseAdb.adb_stop("cn.cj.pe")
            sleep(5)
            self.login_action()




    def login_action(self, first_fogin=False):
        '''账号登录'''
        try:
            LogAction.print(isReset=True)
            LogAction.print("=>清除APP缓存")
            BaseAdb.adb_clear("cn.cj.pe")
            sleep(5)
            BaseAdb.add_pressmission()
            sleep(5)
            BaseAdb.adb_start_app("cn.cj.pe","com.mail139.about.LaunchActivity")

            sleep(4)
            if first_fogin == True:
                self.driver.click(u"uiautomator=>允许")
                sleep(4)

            LogAction.print("=>右滑")
            self.driver.swipe_right()
            LogAction.print("=>右滑")
            self.driver.swipe_right()
            print("点击坐标")
            # BaseAdb.adbTap(700, 2300)  # vivo 1603  w * 0.5, h * 0.899

            w = self.driver.get_window_size()['width']
            h = self.driver.get_window_size()['height']
            LogAction.print("=>点击坐标体验")
            BaseAdb.adb_tap(w / 2, int(h * 0.899))
            # BaseAdb.adbTap(500, 1700) #其他手机需要调试

            LogAction.print('=>选择139邮箱')
            self.driver.click(r"xpath=>//android.widget.ImageView[@index='0']")

            # 输入
            els = self.driver.get_elements("id=>cn.cj.pe:id/input",5)

            LogAction.print("【验证点：是否进入登录界面】")
            self.assertTrue(els != None, "没有进入登录 页面")

            LogAction.print('=>输入用户名' + self.username)
            els[0].set_value(self.username)


            LogAction.print('=>输入密码')
            els[1].set_value(self.pwd)

            LogAction.print('=>点击登录')
            self.driver.click("id=>cn.cj.pe:id/login",5)


            if first_fogin == True:
                self.driver.click(u"uiautomator=>允许")
                sleep(1)

            LogAction.print('【验证点：等待弹窗广告出现】')
            timeout = int(round(time() * 1000)) + 1*60 * 1000
            # 找到邮件结束
            while int(round(time() * 1000)) < timeout :

                if self.driver.element_wait("id=>cn.cj.pe:id/btn", 2) != None:
                    self.driver.click("id=>cn.cj.pe:id/btn")
                    break
                else:
                    sleep(0.5)
                    self.driver.swipe_down()
                    sleep(0.5)
                    self.driver.swipe_down()

                sleep(0.5)


            sleep(2)
            self.driver.click("id=>cn.cj.pe:id/message_list_bottom_email",2)

            LogAction.print('【验证点：等待收件箱底部导航栏出现】')
            self.assertTrue(self.driver.get_element("id=>cn.cj.pe:id/message_list_bottom_email",60) != None, "登录失败！")

        except BaseException:
            BaseImage.screenshot(self.driver, "LoginError")
            sleep(5)
            LogAction.save(func = "testCaseLogin", status="fail", explain=LogAction.print())
            self.fail("【手动输入账号/密码-登录】出现错误")

    def one_btn_Login(self):
        '''一键登录'''
        try:
            LogAction.print(isReset=True)
            sleep(5)
            BaseAdb.adb_clear("cn.cj.pe")
            sleep(5)
            BaseAdb.add_pressmission()
            sleep(5)
            BaseAdb.adb_start_app("cn.cj.pe","com.mail139.about.LaunchActivity")

            sleep(5)

            LogAction.print("=>右滑")
            self.driver.swipe_right()
            LogAction.print("=>右滑")
            self.driver.swipe_right()
            print("点击坐标")
            # BaseAdb.adbTap(700, 2300)  # vivo 1603  w * 0.5, h * 0.899
            #
            w = self.driver.get_window_size()['width']
            h = self.driver.get_window_size()['height']

            LogAction.print("=>点击立即体验")
            BaseAdb.adb_tap(w / 2, int(h * 0.899))

            # BaseAdb.adbTap(500, 1700) #其他手机需要调试
            sleep(2)

            LogAction.print("【验证点：是否进入登录界面】")
            self.assertTrue(self.driver.get_element(u"uiautomator=>快速登录",10) != None, "页面不存在快捷登录按钮")


            LogAction.print('=>点击快捷登录')
            self.driver.click(u"uiautomator=>快速登录")

            LogAction.print('等待收件箱出现')
            self.driver.element_wait(u"uiautomator=>收件箱",10)

            LogAction.print('【验证点：等待弹窗广告出现】')
            timeout = int(round(time() * 1000)) + 1*60 * 1000
            # 找到邮件结束
            while int(round(time() * 1000)) < timeout :

                if self.driver.element_wait("id=>cn.cj.pe:id/btn", 2) != None:
                    self.driver.click("id=>cn.cj.pe:id/btn")
                    break
                else:
                    sleep(0.5)
                    self.driver.swipe_down()
                    sleep(0.5)
                    self.driver.swipe_down()

                sleep(0.5)


            sleep(2)
            self.driver.click("id=>cn.cj.pe:id/message_list_bottom_email",2)


            LogAction.print('【验证点：等待收件箱底部导航栏出现】')
            self.assertTrue(self.driver.get_element("id=>cn.cj.pe:id/message_list_bottom_email",60) != None, "登录失败！")

            BaseAdb.adb_stop("cn.cj.pe")
            BaseAdb.adb_clear("cn.cj.pe")

        except BaseException:
            BaseImage.screenshot(self.driver, "oneBtnLoginError")
            sleep(5)
            LogAction.save(func = "testCaseOnBtnLogin", status="fail", explain=LogAction.print())
            self.fail("【一键登录出错登录】出现错误")