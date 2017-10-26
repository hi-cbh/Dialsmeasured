# urs/bin/python
# encoding:utf-8

import time
import unittest
from src.base.baseAdb import BaseAdb
from src.base.baseFile import BaseFile
# from src.otherApk.gt.gtutil import GTTest


class Send(unittest.TestCase):
    
    def __init__(self,driver, username):
        self.username = username
        self.driver = driver
        
    def sendActionPeakValue(self, firstLogin=False):
        '''记录CPU、MEM'''
        width = self.driver.get_window_size()['width']
        try:
            # 点击写邮件按钮
            print('=>点击写邮件按钮')
            self.driver.click(r"id=>cn.cj.pe:id/actionbar_right_view")
            # 收件人输入内容
            print('=>收件人输入内容')
            self.driver.set_value(r"id=>cn.cj.pe:id/to_wrapper",self.username)
            # 点击空白地方
            print('=>点击空白地方')
            self.driver.click(r"id=>cn.cj.pe:id/actionbar_title_sub")
            
            # 输入主题
            print('=>输入主题') # testReceive
            self.driver.set_value(r"id=>cn.cj.pe:id/subject",'testReceive')

            # 输入邮件内容
            print('=>输入邮件内容')
            self.driver.set_value(r"id=>cn.cj.pe:id/message_content",'123456789012345678901234567890')
              
            # 添加附件
            print('=>添加附件')
            self.driver.click(r"id=>cn.cj.pe:id/add_attachment")
            self.driver.click(u"uiautomator=>本地文件夹")
            self.driver.click(r"uiautomator=>0")
            self.driver.click(r"uiautomator=>0.")
            self.driver.click(r"uiautomator=>test2M.rar")
            self.driver.click(r"id=>cn.cj.pe:id/check_button")
         
            time.sleep(5)
            # gt = GTTest("cn.cj.pe")
            # gt.startGT()
         
            # 点击发送按钮
            print('=>点击发送按钮，开始计时')
            el = self.driver.get_element("id=>cn.cj.pe:id/txt_send")
            BaseAdb.adbBroadcast()
            el.click()

            print('等待文件更新')
            bl = BaseFile.waitForFileModify(30)
            time.sleep(3)
            print('查找页面是否出现新邮件')
            bl2 = self.driver.element_wait('uiautomator=>testReceive')

            if (bl2==None) or (bl == False) :
                self.driver.swipeDown()
            
            time.sleep(8)
            
            data = []
            # data = gt.endGT()
#             print(data)
            time.sleep(2)
     
            if self.driver.element_wait('uiautomator=>testReceive') != None:
                h = 400
                print('=>查找第一封邮件位置')
                if self.driver.get_element("id=>android:id/list") != None:
                    els = self.driver.get_sub_element("id=>android:id/list","class=>android.widget.LinearLayout")
                    h = els[0].location['y']
                    
                self.driver.swipe(width - 20, h, 20, h, 500)
                print("=>右滑删除")
                time.sleep(2)
                
                print('=>点击删除')
                self.driver.click("id=>cn.cj.pe:id/item_view_back_four")    
            

        except BaseException as error:
            print(error)
            print('发送邮件出错了！！！')
            return 0

        else:
            time.sleep(2)
            return data

    def sendAction(self):
        '''正常的发送邮件'''
        try:
            # 点击写邮件按钮
            self.assertTrue(self.driver.get_element(r"id=>cn.cj.pe:id/actionbar_right_view") != None, "页面没有找到写信按钮")
            print('=>点击写邮件按钮')
            self.driver.click(r"id=>cn.cj.pe:id/actionbar_right_view")
            # 收件人输入内容
            print('=>收件人输入内容')
            self.driver.set_value(r"id=>cn.cj.pe:id/to_wrapper",self.username) # appium 1.6
            # 点击空白地方
            print('=>点击空白地方')
            self.driver.click(r"id=>cn.cj.pe:id/actionbar_title_sub")
            
            # 输入主题
            print('=>输入主题')
            self.driver.set_value(r"id=>cn.cj.pe:id/subject",'dialsMeasured') # appium 1.6

            # 输入邮件内容
            print('=>输入邮件内容')
            self.driver.set_value(r"id=>cn.cj.pe:id/message_content",'123456789012345678901234567890') # appium 1.6
              
            # 添加附件
            print('=>添加附件')
            self.driver.click(r"id=>cn.cj.pe:id/add_attachment")
            self.driver.click(u"uiautomator=>本地文件夹") # appium 1.6
            self.driver.click(r"uiautomator=>0")
            self.driver.click(r"uiautomator=>0.")
            self.driver.click(r"uiautomator=>test2M.rar")
            self.driver.click(r"id=>cn.cj.pe:id/check_button")
         
         
            # 点击发送按钮
            print('=>点击发送按钮')
            self.driver.get_element("id=>cn.cj.pe:id/txt_send").click()
            
            print('=>等待已完成出现')
            self.assertTrue(self.driver.element_wait(u"uiautomator=>已完成",120) != None, "发送邮件失败！")

            print('返回收件箱')
            BaseAdb.adbBack()
            time.sleep(2)
        except BaseException as error:
            self.fail('【带附件邮件发送】出错')
            #添加截图

    def sendFwd(self):
        try:
            print("加载本地邮件封邮件")
            timeout = int(round(time.time() * 1000)) + 1*60 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :

                el = self.driver.element_wait(u"uiautomator=>暂无邮件",secs = 1)
                if el != None:
                    print("下拉")
                    self.driver.swipeDown();
                    time.sleep(1)
                    self.driver.swipeDown();
                else:
                    print("列表有邮件，退出循环")
                    break;

                time.sleep(1)


            # 点击第一封
            print('=>点击第一封邮件，判断是否存在【暂无邮件】字段')
            self.assertTrue(self.driver.get_element(u"uiautomator=>暂无邮件") == None, "收件箱没有邮件")
            els = self.driver.get_sub_element(r"id=>android:id/list","class=>android.widget.LinearLayout")
            time.sleep(2)
            els[0].click()

            print('=>查找控件，确认进入邮件详情页')
            text = self.driver.get_element(r"id=>cn.cj.pe:id/title").get_attribute("text")
            print("text %s" %text)

            print("点击转发按钮")
            self.driver.click(u"uiautomator=>转发")

            print("输入收件人")
            self.driver.set_value(r"id=>cn.cj.pe:id/to_wrapper",self.username)

            # 点击发送按钮
            print('=>点击发送按钮')
            self.driver.get_element("id=>cn.cj.pe:id/txt_send").click()

            print('验证点：发送是否成功')
            self.assertTrue(self.driver.element_wait(u"uiautomator=>已完成",120) != None, "发送邮件失败！")

            print('返回收件箱')
            BaseAdb.adbBack()
            time.sleep(2)

            print("等待邮件出现")
            self.driver.swipeDown();
            time.sleep(5)
            self.driver.swipeDown();
            time.sleep(5)

            # 点击第一封
            print('=>点击第一封邮件')
            els = self.driver.get_sub_element(r"id=>android:id/list","class=>android.widget.LinearLayout")
            time.sleep(2)
            els[0].click()


            print('验证点：主题是否含有"Fwd"字段')
            text = self.driver.get_element(r"id=>cn.cj.pe:id/title").get_attribute("text")
            print("text %s" %text)

            self.assertTrue(text.find("Fwd")!= -1, "没有找到转发邮件")

        except BaseException as error:
            self.fail("【转发邮件（带附件）】出错")

        else:
            BaseAdb.adbBack()
            time.sleep(2)