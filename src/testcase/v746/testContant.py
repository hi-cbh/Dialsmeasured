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

class TestContant(unittest.TestCase):
    '''联系人同步是否成功'''
    def __init__(self,driver):
        self.driver = driver

    def testCaseCheckAddressList(self):
        '''联系人同步'''
        try:
            LogAction.print(isReset=True)
            Login(self.driver,user['name'], user['pwd']).login()

            LogAction.print("=>点击联系人")
            self.driver.click(u"uiautomator=>联系人")

            LogAction.print("=>【通讯录同步】")
            self.assertTrue(self.waitfor_notification(), "通讯录同步失败！！")
            LogAction.save(func = "CheckAddressListError", status="success", explain=LogAction.print())
            ReadWriteConfFile.value_set_zero("CheckAddressListError")
        except BaseException :
            ReadWriteConfFile.value_add_one("CheckAddressListError")
            ReadWriteConfFile.value_error_add_one("CheckAddressListError")
            BaseImage.screenshot(self.driver, "CheckAddressListError")
            time.sleep(5)
            LogAction.save(func = "testCaseCheckAddressList", status="fail", explain=LogAction.print())

            if ReadWriteConfFile.get_status_value():
                self.fail("【联系人同步】出错")


    def waitfor_notification(self):
        '''找到需要的通知栏信息'''
        for i in range(8):
            print("下拉通讯录列表")
            self.driver.swipe_down()
            print("检查通知栏信息")
            if BaseAdb.dumpsys_notification("同步网络联系人完成"):
                return True
            time.sleep(5)
        else:
            return False


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestContant('testCaseCheckAddressList'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)