# urs/bin/python
# encoding:utf-8

import time,unittest

from src.readwriteconf.rwconf import ReadWriteConfFile
from src.base.baseAdb import BaseAdb
from src.testcase.v746.easycase.login import Login
from src.readwriteconf.initData import duser
from src.base.baseImage import BaseImage
from src.base.baseLog import LogAction

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}

class TestSelect(unittest.TestCase):
    '''139精选是否显示正常'''

    def __init__(self,driver):
        self.driver = driver

    def testCaseSelected(self, ):
        '''收件箱列表139精选'''

        try:
            LogAction.print(isReset=True)
            Login(self.driver,user['name'], user['pwd']).login()

            LogAction.print("=>加载本地邮件")
            timeout = int(round(time.time() * 1000)) + 30 * 1000
            # 找到邮件结束
            while int(round(time.time() * 1000)) < timeout :
                if self.driver.element_wait(u'uiautomator=>139精选',2) == None:
                    print("下拉")
                    self.driver.swipe_down()
                    time.sleep(1)
                    self.driver.swipe_down()
                else:
                    break

            LogAction.print("=>【139精选】")
            self.assertTrue(self.driver.get_element(u'uiautomator=>139精选',10),'收件箱列表没有139精选')

            # 经常出现误报
            for i in range(3):
                if self.driver.get_element(u'uiautomator=>139精选',3) != None:
                    LogAction.print('=>点击139精选')
                    self.driver.click(u'uiautomator=>139精选')

            LogAction.print("=>等待30秒")
            # 等待两分钟
            timeout = int(round(time.time() * 1000)) + 60 * 1000
            try:
                while (int(round(time.time() * 1000) < timeout)):

                    if self.driver.page_source().__contains__(u"阅读全文") == True:
                        # print('find it')
                        break
                    time.sleep(1)
                    # print("超时")
            except BaseException as msg:
                print(msg)


            LogAction.print('=>【页面显示】')
            self.assertTrue(self.driver.page_source().__contains__(u"阅读全文"),"页面显示不正常")

            BaseAdb.adb_back()
            LogAction.save(func = "testCaseSelected", status="success", explain=LogAction.print())

            ReadWriteConfFile.value_set_zero("testCaseSelected")
        except BaseException:
            ReadWriteConfFile.value_add_one("testCaseSelected")
            ReadWriteConfFile.value_error_add_one("testCaseSelected")
            BaseImage.screenshot(self.driver, "Case139SelectedError")
            time.sleep(2)
            LogAction.save(func = "testCaseSelected", status="fail", explain=LogAction.print())
            if ReadWriteConfFile.get_status_value():
                self.fail("【139精选】出错！")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSelect('testCaseSelected'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)