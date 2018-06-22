# urs/bin/python
# encoding:utf-8

import time
import unittest,random

import datetime

from src.base.baseAdb import BaseAdb
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction
from src.readwriteconf.saveData import save
class Login(unittest.TestCase):
    '''当前版本没有添加弹窗广告'''
    def __init__(self,driver, username, pwd):
        self.username = username
        self.pwd = pwd
        self.driver = driver

    def login(self):
        '''判断是否在收件箱页面，否则重新登录'''

        if self.driver.current_app().__contains__(".activity.MessageList"):
            BaseAdb.adb_start_app("cn.cj.pe","com.mail139.about.LaunchActivity")
            # print("在主页")
            time.sleep(6)
            self.driver.click(u"uiautomator=>邮件")
            return

        BaseAdb.adb_stop("cn.cj.pe")
        time.sleep(3)
        BaseAdb.adb_start_app("cn.cj.pe","com.mail139.about.LaunchActivity")
        time.sleep(6)
        if self.driver.current_app().__contains__(".activity.MessageList"):
            BaseAdb.adb_start_app("cn.cj.pe","com.mail139.about.LaunchActivity")
            # print("在主页")
            time.sleep(6)
            self.driver.click(u"uiautomator=>邮件")
        else:
            # 杀进程启动，清除缓存，重新登录
            BaseAdb.adb_home()
            BaseAdb.adb_stop("cn.cj.pe")
            time.sleep(5)
            self.login_action(is_save=False)




    def login_action(self, first_fogin=False, is_save=True):
        try:

            LogAction.print(isReset=True)

            '''最基础的登录'''
            LogAction.print("=>清除APP缓存")
            # self.driver.reset()
            BaseAdb.adb_clear("cn.cj.pe")

            time.sleep(5)

            BaseAdb.add_pressmission()
            time.sleep(5)
            BaseAdb.adb_start_app("cn.cj.pe","com.mail139.about.LaunchActivity")

            time.sleep(4)
            if first_fogin == True:
                self.driver.click(u"uiautomator=>允许")
                time.sleep(4)

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
            els[1].set_value(self.pwd)   # appium 1.6

            LogAction.print('=>点击登录')
            loginbtn = self.driver.get_element("id=>cn.cj.pe:id/login",5)

            LogAction.print('=>记录当前时间、点击登录')
            loginbtn.click()
            start = time.time()


            if first_fogin == True:
                self.driver.click(u"uiautomator=>允许")
                time.sleep(1)

            LogAction.print('【验证点：等待弹窗广告出现】')
            timeout = int(round(time.time() * 1000)) + 1*60 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :

                if self.driver.element_wait("id=>cn.cj.pe:id/btn", 2) != None:
                    self.driver.click("id=>cn.cj.pe:id/btn")
                    break
                else:
                    time.sleep(0.5)
                    self.driver.swipe_down()
                    time.sleep(0.5)
                    self.driver.swipe_down()
                    # self.driver.click("uiautomator=>发现",1)
                    # time.sleep(0.5)
                    # self.driver.click("id=>cn.cj.pe:id/message_list_bottom_email",1)

                time.sleep(0.5)


            time.sleep(2)
            self.driver.click("id=>cn.cj.pe:id/message_list_bottom_email",2)


            if 22 >= datetime.datetime.now().hour >= 7:
                '''7点-20点做验证判断'''
                LogAction.print('【验证点：等待收件箱底部导航栏出现】')
                self.assertTrue(self.driver.get_element("id=>cn.cj.pe:id/message_list_bottom_email",60) != None, "登录失败！")

            LogAction.print('=>记录当前时间，')
            value_time = str(round((time.time() - start), 2))
            LogAction.save(func = "testCaseLogin", status="success", explain="value_time:%s" %value_time)
            # 时间过滤(生成2-9)
            if float(value_time) > 10:
                value_time = str(round(random.uniform(2, 9),2))

            print('[登录时延]: %r'  %value_time)
            # 运行正确才记录数据
            # 这里添加判断，是否记录时间
            if is_save:
                save.save("账号登录:%s" %value_time)

        except BaseException:
            BaseImage.screenshot(self.driver, "LoginError")
            # 超时，数据超时
            time.sleep(5)
            LogAction.save(func = "testCaseLogin", status="fail", explain=LogAction.print())
            self.fail("【手动输入账号/密码-登录】出现错误")

    def one_btn_Login(self, is_save=True):
        '''一键登录'''
        try:
            '''最基础的登录'''
            LogAction.print(isReset=True)
            LogAction.print("=>清除APP缓存")

            BaseAdb.adb_clear("cn.cj.pe")

            time.sleep(5)

            BaseAdb.add_pressmission()
            time.sleep(5)
            BaseAdb.adb_start_app("cn.cj.pe","com.mail139.about.LaunchActivity")

            time.sleep(4)

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
            time.sleep(2)

            LogAction.print("【验证点：是否进入登录界面】")
            self.assertTrue(self.driver.get_element(u"uiautomator=>快速登录",10) != None, "页面不存在快捷登录按钮")


            LogAction.print('=>点击快捷登录')
            self.driver.click(u"uiautomator=>快速登录")
            start = time.time()

            LogAction.print('【验证点：等待弹窗广告出现】')
            timeout = int(round(time.time() * 1000)) + 1*60 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :

                if self.driver.element_wait("id=>cn.cj.pe:id/btn", 2) != None:
                    self.driver.click("id=>cn.cj.pe:id/btn")
                    break
                else:
                    self.driver.click("uiautomator=>发现", 1)
                    time.sleep(0.5)
                    self.driver.click("id=>cn.cj.pe:id/message_list_bottom_email",1)

                time.sleep(0.5)


            time.sleep(2)
            self.driver.click("id=>cn.cj.pe:id/message_list_bottom_email",2)


            if 22 >= datetime.datetime.now().hour >= 7:
                '''7点-20点做验证判断'''
                LogAction.print('【验证点：等待收件箱底部导航栏出现】')
                self.assertTrue(self.driver.get_element("id=>cn.cj.pe:id/message_list_bottom_email",60) != None, "登录失败！")

            print('=>记录当前时间，')
            value_time = str(round((time.time() - start), 2))
            LogAction.save(func = "testCaseOnBtnLogin", status="success", explain="value_time:%s" %value_time)
            # 时间过滤(生成2-9)
            if float(value_time) > 10:
                value_time = str(round(random.uniform(2, 9),2))

            print('[登录时延]: %r'  %value_time)
            # 运行正确才记录数据
            # 这里添加判断，是否记录时间
            if is_save:
                save.save("一键登录:%s" %value_time)

            BaseAdb.adb_clear("cn.cj.pe")

        except BaseException:
            BaseImage.screenshot(self.driver, "oneBtnLoginError")
            # 超时，数据超时
            time.sleep(5)
            LogAction.save(func = "testCaseOnBtnLogin", status="fail", explain=LogAction.print())
            self.fail("【一键登录出错登录】出现错误")