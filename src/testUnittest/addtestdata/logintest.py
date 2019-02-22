# urs/bin/python
# encoding:utf-8

import unittest
from src.base.baseLog import LogAction

class Login(unittest.TestCase):
    '''当前版本没有添加弹窗广告'''

    def login_action(self):
        '''账号登录'''
        try:
            LogAction.print(isReset=True)
            LogAction.print("=>清除APP缓存，添加权限，启动139")
            LogAction.print("=>右滑 * 2")
            LogAction.print("=>点击体验")
            LogAction.print('=>选择139邮箱')
            LogAction.print("=>【进入登录界面】")
            LogAction.print('=>输入用户名')
            LogAction.print('=>输入密码')
            LogAction.print("勾选条款")
            LogAction.print('=>点击登录')
            LogAction.print('=>等待弹窗广告')
            LogAction.print('=>判断是否升级')
            LogAction.print("=>点击邮件")
            LogAction.print('=>【收件箱底部导航栏】')
            self.assertTrue(False, "test")
        except BaseException:

            LogAction.save(func = "testCaseLogin", status="fail", explain=LogAction.print())
            LogAction.sendLog("error_testCaseLogin")


    def one_btn_Login(self):
        '''一键登录'''
        try:
            LogAction.print(isReset=True)
            LogAction.print("=>清除APP缓存，添加权限，启动139")
            LogAction.print("=>右滑 * 2")
            LogAction.print("=>点击立即体验")
            LogAction.print("=>【进入登录界面】")
            LogAction.print('=>选择139邮箱')
            LogAction.print("勾选条款")
            LogAction.print('=>点击本机号码快速登录')
            LogAction.print('=>等待收件箱')
            LogAction.print('=>等待弹窗广告')
            LogAction.print('=>判断是否升级')
            LogAction.print('=>点击底部导航栏')
            LogAction.print('=>【收件箱底部导航栏】')
            LogAction.print('=>杀进程，清除缓存')
        except BaseException:
            LogAction.save(func = "testCaseLogin", status="fail", explain=LogAction.print())



if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(TestCase('testCaseToken'))
    # suite.addTest(TestCase('testCaseOnBtnLogin'))
    suite.addTest(Login('login_action'))
    # suite.addTest(Login('one_btn_Login'))
    unittest.TextTestRunner().run(suite)