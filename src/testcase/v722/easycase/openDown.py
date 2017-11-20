# urs/bin/python
# encoding:utf-8

import time
import unittest
from src.base.baseAdb import BaseAdb
from src.base.baseFile import BaseFile
from src.base.baseImage import BaseImage
from src.readwriteconf.saveData import save
class OpenDown(unittest.TestCase):
    
    def __init__(self,driver, path, filename):
        self.driver = driver
        self.path = path
        self.filename = filename
        
    def openAction(self):
        '''打开未读邮件时延'''
        try:
            print("加载本地邮件封邮件")
            timeout = int(round(time.time() * 1000)) + 2*60 * 1000
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
            self.assertTrue(self.driver.element_wait(r"id=>cn.cj.pe:id/circular_progress_container") != None , "测试邮件不存在!")
            self.driver.element_wait(r"class=>android.webkit.WebView")


        except BaseException as e:
            BaseImage.screenshot(self.driver, "OpenEmailError")
            time.sleep(5)

            self.fail('【打开未读邮件】出错')
        
        
        
    def downAction(self):
        '''下载文件时延'''
        try:
            # 清除
            print('=>清除下载的旧数据')
            if BaseFile.adbFindFile(self.path, self.filename):
                BaseFile.adbDeleteFile(self.path, self.filename)
                 
            time.sleep(3)
             
            # 点击全部下载
            print('=>点击全部下载')
            self.assertTrue(self.driver.get_element(r"id=>cn.cj.pe:id/message_detail_attachment_download"),'没有下载按钮')
            self.driver.click(r"id=>cn.cj.pe:id/message_detail_attachment_download")


            print('=>记录当前时')
            start = time.time()

            # 等待文件出现
            print('=>等待文件出现')
            self.assertTrue(BaseFile.waitforfile(self.path, self.filename, 300),'下载附件出错')

            print('=>记录当前时间，时间差')
            valueTime = str(round((time.time() - start), 2))
            print('[登录时延]: %r'  %valueTime)
            save.save("附件下载:%s" %valueTime)

            print('=>返回收件箱')
            BaseAdb.adbBack()
            BaseAdb.adbBack()
            time.sleep(2)

        except BaseException:
            BaseImage.screenshot(self.driver, "DownFileError")
            time.sleep(5)

            self.fail('【下载附件】出错')
         
    # 设置收件箱列表的邮件为未读邮件
    def setFirstEmail(self):
        
        width = self.driver.get_window_size()['width']
        
        # 第一封邮件
        print('=>第一封邮件')
        if self.driver.get_element("id=>android:id/list") != None:
            els = self.driver.get_sub_element("id=>android:id/list", "class=>android.widget.LinearLayout") 
            h = els[0].location['y']
            
        time.sleep(2)
        print('=>右滑')
        self.driver.swipe(width - 20, h, 20, h, 500)
        time.sleep(2)
        
        print('=>设置未读')
        if self.driver.get_element(u"uiautomator=>未读") != None:
            self.driver.click(u"uiautomator=>未读")
        else:
            self.driver.swipe(20, h, width - 20, h, 500) 
            
        time.sleep(2)   
            
            
        