# urs/bin/python
# encoding:utf-8

import time
import unittest

from src.readwriteconf.rwconf import ReadWriteConfFile
from src.base.baseAdb import BaseAdb
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction

is_status=ReadWriteConfFile.get_status_value()

class Send(unittest.TestCase):
    
    def __init__(self,driver, username):
        self.username = username
        self.driver = driver

    def send(self,subject, is_add = True):
        '''发送邮件'''
        try:
            # 点击写邮件按钮
            LogAction.print('=>点击写邮件')
            self.driver.click(r"id=>cn.cj.pe:id/actionbar_right_view")
            # 收件人输入内容
            LogAction.print('=>收件人'+self.username)
            self.driver.set_value(r"id=>cn.cj.pe:id/to_wrapper",self.username) # appium 1.6
            # 点击空白地方
            LogAction.print('=>点击空白地方')
            self.driver.click(r"id=>cn.cj.pe:id/actionbar_title_sub")

            # 输入主题
            LogAction.print('=>输入主题')
            self.driver.set_value(r"id=>cn.cj.pe:id/subject",subject) # appium 1.6

            if is_add:
                # 添加附件
                LogAction.print('=>添加附件')
                self.driver.click(r"id=>cn.cj.pe:id/add_attachment")
                self.driver.click(u"uiautomator=>本地文件夹") # appium 1.6
                self.driver.click(r"uiautomator=>0")
                self.driver.click(r"uiautomator=>0.")
                self.driver.click(r"uiautomator=>test2M.rar")
                self.driver.click(r"id=>cn.cj.pe:id/check_button")


            # 点击发送按钮
            LogAction.print('=>点击发送')
            btn = self.driver.get_element("id=>cn.cj.pe:id/txt_send",5)
            btn.click()

            LogAction.print('=>【已完成】')
            self.assertTrue(self.driver.element_wait(u"uiautomator=>已完成",40) != None, "发送邮件失败！")

            print('返回收件箱')
            BaseAdb.adb_back()

            LogAction.print("=>等待邮件")
            timeout = int(round(time.time() * 1000)) + 1*40 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :
                if self.driver.element_wait(u"uiautomator=>%s" %subject,2) == None:
                    self.driver.swipe_down()
                    time.sleep(2)
                    self.driver.swipe_down()
                    time.sleep(2)
                else:
                    break

            LogAction.save(func = "send", status="success", explain=LogAction.print())
            ReadWriteConfFile.value_set_zero("testCaseSendNoAttach")
        except BaseException:
            ReadWriteConfFile.value_add_one("testCaseSendNoAttach")
            time.sleep(2)
            LogAction.save(func = "send", status="fail", explain=LogAction.print())

            if is_status:
                self.fail('【邮件发送】出错')


    def send_action(self,subject):
        '''正常的发送邮件，添加附件'''
        try:
            # 点击写邮件按钮
            LogAction.print('=>点击写邮件')
            self.driver.click(r"id=>cn.cj.pe:id/actionbar_right_view")
            # 收件人输入内容
            LogAction.print('=>收件人输入'+self.username)
            self.driver.set_value(r"id=>cn.cj.pe:id/to_wrapper",self.username) # appium 1.6
            # 点击空白地方
            LogAction.print('=>点击空白地方')
            self.driver.click(r"id=>cn.cj.pe:id/actionbar_title_sub")
            
            # 输入主题
            LogAction.print('=>输入主题')
            self.driver.set_value(r"id=>cn.cj.pe:id/subject",subject) # appium 1.6

            # 添加附件
            LogAction.print('=>添加附件')
            self.driver.click(r"id=>cn.cj.pe:id/add_attachment")
            self.driver.click(u"uiautomator=>本地文件夹") # appium 1.6
            self.driver.click(r"uiautomator=>0")
            self.driver.click(r"uiautomator=>0.")
            self.driver.click(r"uiautomator=>test2M.rar")
            self.driver.click(r"id=>cn.cj.pe:id/check_button")

            # 点击发送按钮
            LogAction.print('=>点击发送')
            btn = self.driver.get_element("id=>cn.cj.pe:id/txt_send",5)
            btn.click()

            LogAction.print('=>【已完成】')
            self.assertTrue(self.driver.element_wait(u"uiautomator=>已完成",40) != None, "发送邮件失败！")

            print('返回收件箱')
            BaseAdb.adb_back()

            LogAction.print("=>等待FW邮件")
            timeout = int(round(time.time() * 1000)) + 1*40 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :
                if self.driver.element_wait(u"uiautomator=>%s" %subject,2) == None:
                    self.driver.swipe_down()
                    time.sleep(2)
                    self.driver.swipe_down()
                    time.sleep(2)
                else:
                    break
            LogAction.save(func = "send_action", status="success", explain=LogAction.print())
            ReadWriteConfFile.value_set_zero("testCaseSendAttach")
        except BaseException:
            ReadWriteConfFile.value_add_one("testCaseSendAttach")
            BaseImage.screenshot(self.driver, "SendError")
            time.sleep(2)
            LogAction.save(func = "send_action", status="fail", explain=LogAction.print())
            time.sleep(2)
            if is_status:
                self.fail('【带附件邮件发送】出错')

    def send_fwd(self, subject):
        '''云端转发：带有的邮件，进行转发'''
        try:

            print("判断是否存在邮件")
            if self.driver.element_wait("uiautomator=>%s" %subject) == None:
                self.send_action(subject=subject)


            LogAction.print('=>点击 %s' %subject)
            self.driver.click("uiautomator=>%s" %subject)

            LogAction.print('=>邮件详情页')
            text = self.driver.get_element(r"id=>cn.cj.pe:id/title").get_attribute("text")
            print("text %s" %text)

            LogAction.print("=>点击转发")
            self.driver.click(u"uiautomator=>转发")

            LogAction.print("=>输入收件人" + self.username)
            self.driver.set_value(r"id=>cn.cj.pe:id/to_wrapper",self.username)

            # 点击发送按钮
            LogAction.print('=>点击发送')
            self.driver.get_element("id=>cn.cj.pe:id/txt_send").click()

            LogAction.print('=>【发已完成】')
            self.assertTrue(self.driver.element_wait(u"uiautomator=>已完成",80) != None, "发送邮件失败！")

            LogAction.print('=>返回收件箱')
            BaseAdb.adb_back()

            LogAction.print("=>等待FW邮件")
            timeout = int(round(time.time() * 1000)) + 1*40 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :
                if self.driver.element_wait(u"uiautomator=>Fwd: %s" %subject,2) == None:
                    self.driver.swipe_down()
                    time.sleep(2)
                    self.driver.swipe_down()
                    time.sleep(2)
                else:
                    break
            LogAction.save(func = "testCaseFwdSend", status="success", explain=LogAction.print())
            ReadWriteConfFile.value_set_zero("testCaseFwdSend")
        except BaseException:
            ReadWriteConfFile.value_add_one("testCaseFwdSend")
            BaseImage.screenshot(self.driver, "fwSendError")
            time.sleep(2)
            LogAction.save(func = "testCaseFwdSend", status="fail", explain=LogAction.print())
            time.sleep(3)

            if is_status:
                self.fail("【云端转发】出错")

    def forward(self,subject):
        '''stmp转发：本地无附件的邮件，添加附件后，转发'''
        try:

            print("判断是否存在邮件")
            if self.driver.element_wait("uiautomator=>%s" %subject) == None:
                self.send(subject=subject)

            LogAction.print('=>点击 %s' %subject)
            self.driver.click("uiautomator=>%s" %subject)

            LogAction.print('=>进入邮件详情页')
            text = self.driver.get_element(r"id=>cn.cj.pe:id/title").get_attribute("text")
            print("text %s" %text)

            LogAction.print("=>点击转发")
            self.driver.click(u"uiautomator=>转发")

            LogAction.print("=>收件人" + self.username)
            self.driver.set_value(r"id=>cn.cj.pe:id/to_wrapper",self.username)

            time.sleep(1)

            # 添加附件
            LogAction.print('=>添加附件')
            self.driver.click(r"id=>cn.cj.pe:id/add_attachment")
            self.driver.click(u"uiautomator=>本地文件夹") # appium 1.6
            self.driver.click(r"uiautomator=>0")
            self.driver.click(r"uiautomator=>0.")
            self.driver.click(r"uiautomator=>test2M.rar")
            self.driver.click(r"id=>cn.cj.pe:id/check_button")


            # 点击发送按钮
            LogAction.print('=>点击发送')
            self.driver.get_element("id=>cn.cj.pe:id/txt_send").click()

            LogAction.print('=>【已完成】')
            self.assertTrue(self.driver.element_wait(u"uiautomator=>已完成",60) != None, "发送邮件失败！")

            print('返回收件箱')
            BaseAdb.adb_back()

            LogAction.print("=>等待FW邮件")
            timeout = int(round(time.time() * 1000)) + 1*20 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :
                if self.driver.element_wait(u"uiautomator=>Fwd: %s" %subject,2) == None:
                    self.driver.swipe_down()
                    time.sleep(2)
                    self.driver.swipe_down()
                    time.sleep(2)
                else:
                    break
            LogAction.save(func = "testCaseForward", explain=LogAction.print())
            ReadWriteConfFile.value_set_zero("testCaseForward")
        except BaseException:
            ReadWriteConfFile.value_add_one("testCaseForward")
            BaseImage.screenshot(self.driver, "forwardError")
            time.sleep(2)
            LogAction.save(func = "testCaseForward", status="fail", explain=LogAction.print())
            time.sleep(2)
            if is_status:
                self.fail("【smtp转发】出错")



    def reply(self,subject):
        '''回复邮件-无附件'''
        try:
            print("判断是否存在邮件")
            if self.driver.element_wait("uiautomator=>%s" %subject) == None:
                self.send(subject=subject)

            # 点击第一封
            LogAction.print('=>点击 %s' %subject)
            self.driver.click("uiautomator=>%s" %subject)

            LogAction.print('=>进入邮件详情页')
            text = self.driver.get_element(r"id=>cn.cj.pe:id/title").get_attribute("text")
            print("text %s" %text)

            LogAction.print("=>点击回复")
            self.driver.click(u"uiautomator=>回复")

            # 点击发送按钮
            LogAction.print('=>点击发送')
            self.driver.get_element("id=>cn.cj.pe:id/txt_send").click()

            # 点击发送按钮
            LogAction.print('=>点击确定')
            self.driver.get_element(u"uiautomator=>确定").click()

            LogAction.print('=>【已完成】')
            self.assertTrue(self.driver.element_wait(u"uiautomator=>已完成",60) != None, "发送邮件失败！")

            print('返回收件箱')
            BaseAdb.adb_back()

            LogAction.print("=>等待Re邮件")
            timeout = int(round(time.time() * 1000)) + 1*20 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :
                if self.driver.element_wait(u"uiautomator=>Re: %s" %subject,2) == None:
                    self.driver.swipe_down()
                    time.sleep(2)
                    self.driver.swipe_down()
                    time.sleep(2)
                else:
                    break
            LogAction.save(func = "testCaseReply", explain=LogAction.print())

            ReadWriteConfFile.value_set_zero("testCaseReply")
        except BaseException:
            ReadWriteConfFile.value_add_one("testCaseReply")
            BaseImage.screenshot(self.driver, "replyError")
            time.sleep(2)
            LogAction.save(func = "testCaseReply", status="fail", explain=LogAction.print())
            time.sleep(2)
            if is_status:
                self.fail("【回复邮件】出错")
