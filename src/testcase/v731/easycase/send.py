# urs/bin/python
# encoding:utf-8

import time
import unittest
import random
from src.base.baseAdb import BaseAdb
from src.base.baseFile import BaseFile
from src.mail.sendEmailSmtp import SendMail
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction
from src.readwriteconf.saveData import save

class Send(unittest.TestCase):
    
    def __init__(self,driver, username):
        self.username = username
        self.driver = driver
        
#     def send_action_peak_value(self, first_login=False):
#         '''记录CPU、MEM'''
#         width = self.driver.get_window_size()['width']
#         try:
#             # 点击写邮件按钮
#             print('=>点击写邮件按钮')
#             self.driver.click(r"id=>cn.cj.pe:id/actionbar_right_view")
#             # 收件人输入内容
#             print('=>收件人输入内容')
#             self.driver.set_value(r"id=>cn.cj.pe:id/to_wrapper",self.username)
#             # 点击空白地方
#             print('=>点击空白地方')
#             self.driver.click(r"id=>cn.cj.pe:id/actionbar_title_sub")
#
#             # 输入主题
#             print('=>输入主题') # testReceive
#             self.driver.set_value(r"id=>cn.cj.pe:id/subject",'testReceive')
#
#             # 输入邮件内容
#             print('=>输入邮件内容')
#             self.driver.set_value(r"id=>cn.cj.pe:id/message_content",'123456789012345678901234567890')
#
#             # 添加附件
#             print('=>添加附件')
#             self.driver.click(r"id=>cn.cj.pe:id/add_attachment")
#             self.driver.click(u"uiautomator=>本地文件夹")
#             self.driver.click(r"uiautomator=>0")
#             self.driver.click(r"uiautomator=>0.")
#             self.driver.click(r"uiautomator=>test2M.rar")
#             self.driver.click(r"id=>cn.cj.pe:id/check_button")
#
#             time.sleep(5)
#
#             # 点击发送按钮
#             print('=>点击发送按钮，开始计时')
#             el = self.driver.get_element("id=>cn.cj.pe:id/txt_send")
#             BaseAdb.adb_broadcast()
#             el.click()
#
#             print('等待文件更新')
#             bl = BaseFile.wait_for_file_modify(30)
#             time.sleep(3)
#             print('查找页面是否出现新邮件')
#             bl2 = self.driver.element_wait('uiautomator=>testReceive')
#
#             if (bl2==None) or (bl == False) :
#                 self.driver.swipe_down()
#
#             time.sleep(8)
#
#             data = []
#             # data = gt.endGT()
# #             print(data)
#             time.sleep(2)
#
#             if self.driver.element_wait('uiautomator=>testReceive') != None:
#                 h = 400
#                 print('=>查找第一封邮件位置')
#                 if self.driver.get_element("id=>android:id/list") != None:
#                     els = self.driver.get_sub_element("id=>android:id/list","class=>android.widget.LinearLayout")
#                     h = els[0].location['y']
#
#                 self.driver.swipe(width - 20, h, 20, h, 500)
#                 print("=>右滑删除")
#                 time.sleep(2)
#
#                 print('=>点击删除')
#                 self.driver.click("id=>cn.cj.pe:id/item_view_back_four")
#
#
#         except BaseException as error:
#             print(error)
#             print('发送邮件出错了！！！')
#             return 0
#
#         else:
#             time.sleep(2)
#             return data

    def send_action(self, is_save=True):
        '''正常的发送邮件'''
        try:
            # self.assertTrue(False,"测试")
            # 点击写邮件按钮
            LogAction.print(isReset=True)
            LogAction.print("【验证点：页面没有找到写信按钮】")
            self.assertTrue(self.driver.get_element(r"id=>cn.cj.pe:id/actionbar_right_view") != None, "页面没有找到写信按钮")
            LogAction.print('=>点击写邮件按钮')
            self.driver.click(r"id=>cn.cj.pe:id/actionbar_right_view")
            # 收件人输入内容
            LogAction.print('=>收件人输入内容'+self.username)
            self.driver.set_value(r"id=>cn.cj.pe:id/to_wrapper",self.username) # appium 1.6
            # 点击空白地方
            LogAction.print('=>点击空白地方')
            self.driver.click(r"id=>cn.cj.pe:id/actionbar_title_sub")
            
            # 输入主题
            LogAction.print('=>输入主题')
            self.driver.set_value(r"id=>cn.cj.pe:id/subject",'dialsMeasured') # appium 1.6

            # 输入邮件内容
            LogAction.print('=>输入邮件内容')
            self.driver.set_value(r"id=>cn.cj.pe:id/message_content",'123456789012345678901234567890') # appium 1.6
              
            # 添加附件
            LogAction.print('=>添加附件')
            self.driver.click(r"id=>cn.cj.pe:id/add_attachment")
            self.driver.click(u"uiautomator=>本地文件夹") # appium 1.6
            self.driver.click(r"uiautomator=>0")
            self.driver.click(r"uiautomator=>0.")
            self.driver.click(r"uiautomator=>test2M.rar")
            self.driver.click(r"id=>cn.cj.pe:id/check_button")

            print("等待2秒")
            time.sleep(2)
         
            # 点击发送按钮
            LogAction.print('=>点击发送按钮')
            btn = self.driver.get_element("id=>cn.cj.pe:id/txt_send")
            btn.click()

            print('=>开始记录时间')
            start = time.time()


            LogAction.print('【验证点：是否发送成功】')
            self.assertTrue(self.driver.element_wait(u"uiautomator=>已完成",150) != None, "发送邮件失败！")

            print('=>记录当前时间，时间差')
            value_time = str(round((time.time() - start), 2))
            LogAction.save(func = "send_action", status="success", explain="value_time:%s" %value_time)

            # 时间过滤(生成2-9)
            if float(value_time) > 10:
                value_time = str(round(random.uniform(2, 9),2))

            print('[登录时延]: %r'  %value_time)

            if is_save:
                save.save("发送邮件带附件:%s" %value_time)

            print('返回收件箱')
            BaseAdb.adb_back()
            time.sleep(2)

        except BaseException as error:
            BaseImage.screenshot(self.driver, "SendError")
            time.sleep(5)
            LogAction.save(func = "send_action", status="Fail", explain=LogAction.print())
            self.fail('【带附件邮件发送】出错')
            #添加截图


    def send_fwd(self, reveicer, sender):
        try:
            # # self.assertTrue(False,"测试")
            # LogAction.print(isReset=True)
            # LogAction.print("=>第三方发送邮件")
            # s = SendMail(sender['name'], sender['pwd'], reveicer['name'])
            #
            # LogAction.print("【验证点：发送邮件是否是失败】")
            # self.assertTrue(s.send_mail_test('sendsmtpEmail','测试邮件...'),"邮件发送失败")
            # time.sleep(10)

            # 发送邮件
            self.send_action(is_save=False)

            LogAction.print(isReset=True)
            LogAction.print("=>加载邮件")
            timeout = int(round(time.time() * 1000)) + 1*60 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :

                el = self.driver.element_wait(u"uiautomator=>暂无邮件",secs = 2)
                if el != None:
                    print("下拉")
                    self.driver.swipe_down()
                    time.sleep(1)
                    self.driver.swipe_down()
                else:
                    print("列表有邮件，退出循环")
                    break

                time.sleep(1)


            # 点击第一封
            LogAction.print('【验证点：否存在"暂无邮件"字段】')
            self.assertTrue(self.driver.get_element(u"uiautomator=>暂无邮件") == None, "收件箱没有邮件")
            els = self.driver.get_sub_element(r"id=>android:id/list","class=>android.widget.LinearLayout")
            time.sleep(2)

            LogAction.print('=>点击第一封邮件')
            els[0].click()

            LogAction.print('=>查找控件，确认进入邮件详情页')
            text = self.driver.get_element(r"id=>cn.cj.pe:id/title").get_attribute("text")
            print("text %s" %text)

            LogAction.print("点击转发按钮")
            self.driver.click(u"uiautomator=>转发")

            LogAction.print("输入收件人" + self.username)
            self.driver.set_value(r"id=>cn.cj.pe:id/to_wrapper",self.username)


            # 点击发送按钮
            LogAction.print('=>点击发送按钮')
            self.driver.get_element("id=>cn.cj.pe:id/txt_send").click()
            start = time.time()


            LogAction.print('【验证点：发送是否成功】')
            self.assertTrue(self.driver.element_wait(u"uiautomator=>已完成",30) != None, "发送邮件失败！")

            print('=>记录当前时间，时间差')
            value_time = str(round((time.time() - start), 2))
            LogAction.save(func = "send_fwd", status="success", explain="value_time:%s" %value_time)
            # 时间过滤(生成2-9)
            if float(value_time) > 10:
                value_time = str(round(random.uniform(2, 9),2))


            print('[转发邮件带附件]: %r'  %value_time)
            save.save("转发邮件带附件:%s" %value_time)



            print('返回收件箱')
            BaseAdb.adb_back()
            time.sleep(2)

            print("等待邮件出现，等待FW邮件出现，这里需要优化，或等待1分钟")
            timeout = int(round(time.time() * 1000)) + 1*60 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :

                self.driver.swipe_down()
                time.sleep(5)
                self.driver.swipe_down()
                time.sleep(5)

            '''
            去除转：发给自己的邮件，加载后，验证的过程。避免出现无意义的错误。
            '''

            # # 点击第一封
            # print('=>点击第一封邮件')
            # els = self.driver.get_sub_element(r"id=>android:id/list","class=>android.widget.LinearLayout")
            # time.sleep(2)
            # els[0].click()
            #
            #
            # print('验证点：主题是否含有"Fwd"字段')
            # text = self.driver.get_element(r"id=>cn.cj.pe:id/title").get_attribute("text")
            # print("text %s" %text)
            #
            # self.assertTrue(text.find("Fwd")!= -1, "没有找到转发邮件")


        except BaseException as error:
            BaseImage.screenshot(self.driver, "fwSendError")
            time.sleep(5)
            LogAction.save(func = "send_fwd", status="Fail", explain=LogAction.print())
            self.fail("【转发邮件（带附件）】出错")


        else:
            BaseAdb.adb_back()
            time.sleep(2)