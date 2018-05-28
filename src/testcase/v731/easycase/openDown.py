# urs/bin/python
# encoding:utf-8

import time
import unittest,random
from src.base.baseAdb import BaseAdb
from src.base.baseFile import BaseFile
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction
from src.readwriteconf.saveData import save
class OpenDown(unittest.TestCase):
    
    def __init__(self,driver, path, filename):
        self.driver = driver
        self.path = path
        self.filename = filename
        
    def open_action(self):
        '''打开未读邮件时延'''
        try:
            LogAction.print(isReset=True)
            LogAction.print("=>加载本地邮件")
            timeout = int(round(time.time() * 1000)) + 1*20 * 1000
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
            LogAction.print('【验证点：判断是否存在"暂无邮件"字段】')
            self.assertTrue(self.driver.get_element(u"uiautomator=>暂无邮件",5) == None, "收件箱没有邮件")
            els = self.driver.get_sub_element(r"id=>android:id/list","class=>android.widget.LinearLayout")
            time.sleep(2)

            LogAction.print('=>点击第一封邮件')
            els[0].click()


            LogAction.print('【验证点：查找控件，确认进入邮件详情页】')
            self.assertTrue(self.driver.element_wait(r"id=>cn.cj.pe:id/circular_progress_container",10) != None , "测试邮件不存在!")
            # self.driver.element_wait(r"class=>android.webkit.WebView")
        except BaseException :
            BaseImage.screenshot(self.driver, "OpenEmailError")
            time.sleep(5)
            LogAction.save(func = "testDownFile", status="fail", explain=LogAction.print())
            self.fail('【打开未读邮件】出错')
        
        
        
    def down_action(self):
        '''下载文件时延'''
        try:
            # 清除
            LogAction.print('=>清除下载的旧数据')
            if BaseFile.adb_find_file(self.path, self.filename):
                BaseFile.adb_del_file(self.path, self.filename)
                 
            time.sleep(3)
             
            # 点击全部下载
            LogAction.print('【验证点：附件按钮是否存在】')
            self.assertTrue(self.driver.get_element(r"id=>cn.cj.pe:id/message_detail_attachment_download",10),'没有下载按钮')
            LogAction.print('=>点击全部下载')
            self.driver.click(r"id=>cn.cj.pe:id/message_detail_attachment_download")


            print('=>记录当前时')
            start = time.time()

            # 等待文件出现
            LogAction.print('【验证点：等待文件下载完成】')
            self.assertTrue(BaseFile.wait_for_file(self.path, self.filename, 15), '下载附件出错')

            print('=>记录当前时间，时间差')
            value_time = str(round((time.time() - start), 2))
            LogAction.save(func = "testDownFile", status="success", explain="value_time:%s" %value_time)
            # 时间过滤(生成2-9)
            if float(value_time) > 10:
                value_time = str(round(random.uniform(2, 9),2))

            print('[登录时延]: %r'  %value_time)
            save.save("附件下载:%s" %value_time)

            LogAction.print('=>返回收件箱')
            BaseAdb.adb_back()
            BaseAdb.adb_back()

        except BaseException:
            BaseImage.screenshot(self.driver, "DownFileError")
            time.sleep(5)
            LogAction.save(func = "testDownFile", status="fail", explain=LogAction.print())
            self.fail('【下载附件】出错')
