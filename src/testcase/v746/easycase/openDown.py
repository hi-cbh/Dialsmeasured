# urs/bin/python
# encoding:utf-8

import time
import unittest

from src.readwriteconf.rwconf import ReadWriteConfFile
from src.base.baseAdb import BaseAdb
from src.base.baseFile import BaseFile
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction


class OpenDown(unittest.TestCase):
    
    def __init__(self,driver, path, filename):
        self.driver = driver
        self.path = path
        self.filename = filename

    def down_action(self, subject):
        '''下载文件时延'''
        try:

            # LogAction.print(isReset=True)

            # 点击第一封
            LogAction.print('=>点击 %s' %subject)
            self.driver.click("uiautomator=>%s" %subject)

            LogAction.print('=>【邮件详情页】')
            self.assertTrue(self.driver.element_wait(r"id=>cn.cj.pe:id/circular_progress_container",10) != None , "测试邮件不存在!")

            # 清除
            LogAction.print('=>清除下载')
            if BaseFile.adb_find_file(self.path, self.filename):
                BaseFile.adb_del_file(self.path, self.filename)
                 
            time.sleep(3)
             
            # 点击全部下载
            LogAction.print('=>【附件按钮】')
            self.assertTrue(self.driver.get_element(r"id=>cn.cj.pe:id/message_detail_attachment_download",10),'没有下载按钮')
            LogAction.print('=>点击全部下载')
            self.driver.click(r"id=>cn.cj.pe:id/message_detail_attachment_download")

            # 等待文件出现
            LogAction.print('=>【文件下载】')
            self.assertTrue(BaseFile.wait_for_file(self.path, self.filename, 15), '下载附件出错')

            LogAction.print('=>返回收件箱')
            time.sleep(2)
            BaseAdb.adb_back()
            BaseAdb.adb_back()
            LogAction.save(func = "testDownFile", status="success", explain=LogAction.print())
            ReadWriteConfFile.value_set_zero("testDownFile")
        except BaseException:
            ReadWriteConfFile.value_add_one("testDownFile")
            BaseImage.screenshot(self.driver, "DownFileError")
            time.sleep(5)
            LogAction.save(func = "testDownFile", status="fail", explain=LogAction.print())
            self.fail('【下载附件】出错')
