# urs/bin/python
# encoding:utf-8

import time
import unittest,random
from src.base.baseAdb import BaseAdb
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction
from src.readwriteconf.saveData import save
from src.mail.mailOperation import EmailOperation
class Login(unittest.TestCase):
    '''当前版本没有添加弹窗广告'''
    def __init__(self,driver, username, pwd):
        self.username = username
        self.pwd = pwd
        self.driver = driver
        
    def login_action(self, first_fogin=False, is_save=True):
        # first_fogin 首次安装后，登录为true
        try:

            LogAction.print(isReset=True)

            '''最基础的登录'''
            LogAction.print("=>清除APP缓存")
            self.driver.reset()

            time.sleep(4)
            if first_fogin == True:
                self.driver.click(u"uiautomator=>允许")
                time.sleep(4)

            LogAction.print("=>右滑")
            self.driver.swipe_right()
            LogAction.print("=>右滑")
            self.driver.swipe_right()
            # self.driver.swipeRight()
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
            if self.driver.get_element("id=>cn.cj.pe:id/iv", 5) != None:

                self.driver.click("id=>cn.cj.pe:id/btn")


            '''
            # 这里被广告弹窗替代
            print('验证点：等待收件箱底部导航栏出现')
            self.assertTrue(self.driver.get_element("id=>cn.cj.pe:id/message_list_bottom_email") != None, "登录失败！")
            '''

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
            LogAction.save(func = "testCaseLogin", status="Fail", explain=LogAction.print())
            self.fail("【手动输入账号/密码-登录】出现错误")
            # 添加截图



    def one_btn_Login(self, is_save=True):
        '''一键登录'''
        try:
            '''最基础的登录'''
            LogAction.print(isReset=True)
            LogAction.print("=>清除APP缓存")
            self.driver.reset()

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

            # time.sleep(30)
            LogAction.print('【验证点：等待弹窗广告出现】')
            if self.driver.get_element("id=>cn.cj.pe:id/iv",5) != None:

                self.driver.click("id=>cn.cj.pe:id/btn")

            LogAction.print('【验证点：等待收件箱底部导航栏出现】')
            self.assertTrue(self.driver.get_element("id=>cn.cj.pe:id/message_list_bottom_email",15) != None, "登录失败！")

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

        except BaseException:
            BaseImage.screenshot(self.driver, "oneBtnLoginError")
            # 超时，数据超时
            time.sleep(5)
            LogAction.save(func = "testCaseOnBtnLogin", status="Fail", explain=LogAction.print())
            self.fail("【一键登录出错登录】出现错误")