# urs/bin/python
# encoding:utf-8

import time
import unittest
from src.base.baseAdb import BaseAdb
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save

class Login(unittest.TestCase):
    
    def __init__(self,driver, username, pwd):
        self.username = username
        self.pwd = pwd
        self.driver = driver
        
    def loginAction(self, firstLogin=False, isSave=True):
        # firstLogin 首次安装后，登录为true
        try:
            '''最基础的登录'''
            self.driver.reset()

            time.sleep(4)
            if firstLogin == True:
                self.driver.click(u"uiautomator=>允许")
                time.sleep(4)

            self.driver.swipeRight()
            self.driver.swipeRight()
            self.driver.swipeRight()
            # self.driver.swipeRight()
            print("点击坐标")
            # BaseAdb.adbTap(700, 2200)  # vivo 1603  w * 0.5, h * 0.885

            w = self.driver.get_window_size()['width']
            h = self.driver.get_window_size()['height']

            BaseAdb.adbTap(w/2, int(h * 0.885))
            # BaseAdb.adbTap(500, 1700) #其他手机需要调试

            time.sleep(4)

            print('=>选择139邮箱')
            self.driver.click(r"xpath=>//android.widget.ImageView[@index='0']")


            # 输入
            els = self.driver.get_elements("id=>cn.cj.pe:id/input")

            print("验证点：是否进入登录界面")
            self.assertTrue(els != None, "没有进入登录 页面")

            print('=>输入用户名')
            # els[0].send_keys(self.username) # appium 1.4
            els[0].set_value(self.username)


            print('=>输入密码')
            # els[1].send_keys(self.pwd) # appium 1.4
            els[1].set_value(self.pwd)   # appium 1.6

            print('=>点击登录')
            loginbtn = self.driver.get_element("id=>cn.cj.pe:id/login")

            print('=>记录当前时间、点击登录')
            start = time.time()
            loginbtn.click()


            if firstLogin == True:
                self.driver.click(u"uiautomator=>允许")
                time.sleep(1)

            print('验证点：等待收件箱底部导航栏出现')
            self.assertTrue(self.driver.get_element("id=>cn.cj.pe:id/message_list_bottom_email") != None, "登录失败！")

            print('=>记录当前时间，')
            valueTime = str(round((time.time() - start), 2))
            print('[登录时延]: %r'  %valueTime)
            # 运行正确才记录数据
            # 这里添加判断，是否记录时间
            if isSave:
                save.save("账号登录:%s" %valueTime)

        except BaseException as error:
            BaseImage.screenshot(self.driver, "LoginError")
            # 超时，数据超时
            time.sleep(5)
            self.fail("【手动输入账号/密码-登录】出现错误")
            # 添加截图

        # else:
        #     self. 添加OK写入操作

        # 用于记录时延的登录操作
    def loginActionTime(self):
        
        logintime = self.loginAction()   
        
        # 下拉
        time.sleep(4)
        self.driver.swipeDown()
        time.sleep(4)
        
        # 邮件设置
        self.setEmailOption(False, True)
    
        time.sleep(2)
        
        
        return logintime
         
        # 用于记录CPU、内存峰值
    def loginActionPeakValue(self):    
                
        self.loginAction()   
        
        # 邮件设置
        self.setEmailOption(True, False)
    
        time.sleep(2)
        
    def loginActionLoginFlow(self):    
        '''用于首次登录流量'''        
        self.loginAction()  
        
    
    def setEmailOption(self, isNotice, isSetting):
        '''邮件设置'''
        # 点击我的
        print('=>点击我的')
        self.driver.click("id=>cn.cj.pe:id/message_list_bottom_mine")
        
        # 点击设置
        print('=>点击设置')
        # self.driver.click(u"name=>设置") # appium 1.4
        self.driver.click(u"uiautomator=>设置") # appium 1.6
        
        
        
        if isNotice:
            print('==>通知设置')
            self.setEmailNotice()
        
        
        if isSetting:
            print('==>下载图片设置')
            self.setEmailSetting()          
        
        print('=>返回设置页面')
        BaseAdb.adbBack()
#         time.sleep(2)
        print('=>返回收件箱')
        self.driver.click("id=>cn.cj.pe:id/message_list_bottom_email")
        
        #设置邮件提示设置
    def setEmailNotice(self):
        # time.sleep(1) appium 1.4
        # self.driver.click(u"name=>邮件提示设置")
        # time.sleep(1)
        # self.driver.click(u"name=>显示邮件发送页")
        # time.sleep(1)
        # self.driver.click(u"name=>显示邮件通知")
#         time.sleep(1)
        time.sleep(1)
        self.driver.click(u"uiautomator=>邮件提示设置")
        #         time.sleep(1)
        self.driver.click(u"uiautomator=>显示邮件发送页")
        #         time.sleep(1)
        self.driver.click(u"uiautomator=>显示邮件通知")
        #         time.sleep(1)
        BaseAdb.adbBack()  
        
        
        # 开启收邮件设置：自动下载邮件图片
    def setEmailSetting(self):
#         time.sleep(1) appium 1.4
#         self.driver.click(u"name=>收取邮件设置")
# #         time.sleep(1)
#         self.driver.click(u"name=>数据网络下自动下载邮件图片")
# #         time.sleep(1)
        time.sleep(1)
        self.driver.click(u"uiautomator=>收取邮件设置")
#         time.sleep(1)
        self.driver.click(u"uiautomator=>数据网络下自动下载邮件图片")
#         time.sleep(1)
        self.driver.click(r"id=>cn.cj.pe:id/hjl_headicon")
        time.sleep(2)     