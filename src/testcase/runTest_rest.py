# urs/bin/python
# encoding:utf-8

import unittest,os,sys,time



p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("RunAll path: %s" %p)
sys.path.append(p+"/")
from src.readwriteconf.initData import duser
from src.mail.mailOperation import EmailOperation
from src.psam.psam import Psam
from src.testcase.v746.test139Selected import TestSelect
from src.testcase.v746.testCalendar import TestCalendar
from src.testcase.v746.testContant import TestContant
from src.testcase.v746.testDiscover import TestDiscover
from src.testcase.v746.testDownFile import TestDownFile
from src.testcase.v746.testLogin import TestLogin
from src.testcase.v746.testPerson import TestPersion
from src.testcase.v746.testPush import TestPush
from src.testcase.v746.testSend import TestSend
from src.testcase.v746.testSkyDrive import TestSkyDrive
# 添加环境路径，脚本
from src.base.baseAdb import BaseAdb
from src.readwriteconf.rwconf import ReadWriteConfFile

localPath = "/var/appiumRunLog"
# 信息存储路径
reportPath = localPath + "/report/"

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}



'''
全部用例重跑，这里需要优化，逻辑不对
问题：
1、使用调用 TestCase类的方法，出现异常。

替代方法：
1、变相的把case当做方法调用
2、需要处理fail，否则会运行失败
'''

class RunAll(object):

    def run_case(self):
        BaseAdb.adb_wake_up()
        time.sleep(10)
        print("run................")
        ReadWriteConfFile.value_set_true_false(False)
        time.sleep(3)
        devicename = BaseAdb.adb_devicename()
        if devicename.__contains__("vivo"):
            BaseAdb.adb_intall_uiautmator()
        self.driver2 = Psam(version="6.0")
        EmailOperation(user["name"]+"@139.com", user["pwd"]).clear_forlder(['INBOX'])

        print('=================重跑用例=================')

        TestLogin(self.driver2).testCaseLogin()
        '''一键登录'''
        TestLogin(self.driver2).testCaseOnBtnLogin()
        '''账号登录'''
        TestLogin(self.driver2).testCaseLogin()
        '''发送邮件，无附件'''
        TestSend(self.driver2).testCaseSendNoAttach()
        '''发送邮件，带附件'''
        TestSend(self.driver2).testCaseSendAttach()
        '''云端转发'''
        TestSend(self.driver2).testCaseFwdSend()
        '''回复邮件'''
        TestSend(self.driver2).testCaseReply()
        '''SMTP转发附件'''
        TestSend(self.driver2).testCaseForward()
        '''下载附件'''
        TestDownFile(self.driver2).testDownFile()
        '''日历'''
        TestCalendar(self.driver2).testCaseCalendar()
        '''发现主页'''
        TestDiscover(self.driver2).testCaseDiscover()
        '''个人资料'''
        TestPersion(self.driver2).testCasePersionMessages()
        '''联系人同步'''
        TestContant(self.driver2).testCaseCheckAddressList()
        '''收件箱列表139精选'''
        TestSelect(self.driver2).testCaseSelected()
        '''彩云网盘'''
        TestSkyDrive(self.driver2).testCaseSkyDrive()
        '''推送'''
        TestPush(self.driver2).testCasePush()

        self.driver2.quit()
        print("运行结束")
        time.sleep(5)
        print('=================运行结束=================')
        # 休眠状态
        BaseAdb.adb_sleep()
        time.sleep(5)

RunAll=RunAll()


if __name__ == "__main__":
    RunAll.run_case()