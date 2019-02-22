# # urs/bin/python
# # encoding:utf-8
#
# import unittest,os,sys,time
#
#
# # 添加环境路径，脚本
# p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print("path: %s" %p)
# sys.path.append(p+"/")
# # sys.path.append("/Users/apple/autoTest/workspace/DialsMeasured/")
# from src.readwriteconf.rwconf import ReadWriteConfFile
#
# localPath = "/var/appiumRunLog"
# # 信息存储路径
# reportPath = localPath + "/report/"
#
#
#
#
# from src.testcase.v731.testSend import TestSend
# from src.testcase.v731.testContant import TestContant
# from src.testcase.v731.test139Selected import TestSelect
# from src.testcase.v731.testPush import TestPush
# from src.testcase.HTMLTestRunner import HTMLTestRunner
# from src.testcase.v731.testLogin import TestLogin
# from src.testcase.v731.testDownFile import TestDownFile
# from src.testcase.v731.testCalendar import TestCalendar
# from src.testcase.v731.testDiscover import TestDiscover
# from src.testcase.v731.testPerson import TestPersion
# from src.testcase.v731.testSkyDrive import TestSkyDrive
# from src.reportlib.reportclass import ReportClass
# from src.base.baseAdb import BaseAdb
#
# '''
# 优化测试结果：
# 1、成功是每天晚上8点发送邮件。
# 2、失败次数达到N次后，发送邮件。
# 将代码有，封装成类，方便理解
# '''
#
#
# if __name__ == "__main__":
#     BaseAdb.adb_wake_up()
#     time.sleep(5)
#     # 获取当前网速
#     # ts = TestSpeed()
#     # ts.setUp()
#     # speed = ts.testCase()
#     # ts.tearDown()
#
#     # print("speed: %s" %speed)
#     speed=""
#
#     print('需要运行的脚本')
#     testtxt = []
#
#     _run = 5
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseLogin')) <=_run :
#         testtxt.append(('账号登录',"testCaseLogin"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseOnBtnLogin'))<=_run :
#         testtxt.append(('一键登录',"testCaseOnBtnLogin"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSend'))<=_run :
#         testtxt.append(('发送邮件带附件',"testCaseSend"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseFwdSend'))<=_run :
#         testtxt.append(('云端转发',"testCaseFwdSend"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseReply'))<=_run :
#         testtxt.append(('回复邮件',"testCaseReply"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseForward'))<=_run :
#         testtxt.append(('SMTP转发',"testCaseForward"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseCalendar'))<=_run :
#         testtxt.append(('日历',"testCaseCalendar"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseDiscover'))<=_run :
#         testtxt.append(('发现主页',"testCaseDiscover"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCasePersionMessages'))<=_run :
#         testtxt.append(('个人资料',"testCasePersionMessages"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSkyDrive'))<=_run :
#         testtxt.append(('彩云网盘',"testCaseSkyDrive"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testDownFile'))<=_run :
#         testtxt.append(('附件下载',"testDownFile"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseCheckAddressList'))<=_run :
#         testtxt.append(('联系人同步',"testCaseCheckAddressList"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSelected'))<=_run :
#         testtxt.append(('收件箱列表中精选',"testCaseSelected"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCasePush'))<=_run :
#         testtxt.append(('接收推送',"testCasePush"))
#
#
#     suite = unittest.TestSuite()
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseOnBtnLogin'))<=_run :
#         suite.addTest(TestLogin('testCaseOnBtnLogin'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseLogin'))<=_run :
#         suite.addTest(TestLogin('testCaseLogin'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSend'))<=_run :
#         suite.addTest(TestSend('testCaseSend'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseFwdSend'))<= 5 :
#         suite.addTest(TestSend('testCaseFwdSend'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseForward'))<=_run :
#         suite.addTest(TestSend('testCaseForward'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseReply'))<=_run :
#         suite.addTest(TestSend('testCaseReply'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseCalendar'))<=_run :
#         suite.addTest(TestCalendar('testCaseCalendar'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseDiscover'))<=_run :
#         suite.addTest(TestDiscover('testCaseDiscover'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCasePersionMessages'))<=_run :
#         suite.addTest(TestPersion('testCasePersionMessages'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSkyDrive'))<=_run :
#         suite.addTest(TestSkyDrive('testCaseSkyDrive'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testDownFile'))<=_run :
#         suite.addTest(TestDownFile('testDownFile'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseCheckAddressList'))<=_run :
#         suite.addTest(TestContant('testCaseCheckAddressList'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSelected'))<=_run :
#         suite.addTest(TestSelect('testCaseSelected'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCasePush'))<=_run :
#         suite.addTest(TestPush('testCasePush'))
#
#     runner = unittest.TextTestRunner()
#
#
#
#     # 生成html
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     filename_now = time.strftime("%Y_%m_%d_%H_%M_%S")
#     filename = reportPath + now + '_result.html'
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(stream=fp,title='Test Report', description='DialsMeasured with: ')
#     testResultReport = runner.run(suite)
#     fp.close()
#
#
#
#     ReportClass(testResultReport.failures,testtxt,speed,now).all()
#
#     time.sleep(5)
#     # 休眠状态
#     BaseAdb.adb_sleep()
#
#     time.sleep(5)# urs/bin/python
# # encoding:utf-8
#
# import unittest,os,sys,time
#
#
# # 添加环境路径，脚本
# p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print("path: %s" %p)
# sys.path.append(p+"/")
# # sys.path.append("/Users/apple/autoTest/workspace/DialsMeasured/")
# from src.readwriteconf.rwconf import ReadWriteConfFile
#
# localPath = "/var/appiumRunLog"
# # 信息存储路径
# reportPath = localPath + "/report/"
#
#
#
#
# from src.testcase.v731.testSend import TestSend
# from src.testcase.v731.testContant import TestContant
# from src.testcase.v731.test139Selected import TestSelect
# from src.testcase.v731.testPush import TestPush
# from src.testcase.HTMLTestRunner import HTMLTestRunner
# from src.testcase.v731.testLogin import TestLogin
# from src.testcase.v731.testDownFile import TestDownFile
# from src.testcase.v731.testCalendar import TestCalendar
# from src.testcase.v731.testDiscover import TestDiscover
# from src.testcase.v731.testPerson import TestPersion
# from src.testcase.v731.testSkyDrive import TestSkyDrive
# from src.reportlib.reportclass import ReportClass
# from src.base.baseAdb import BaseAdb
#
# '''
# 优化测试结果：
# 1、成功是每天晚上8点发送邮件。
# 2、失败次数达到N次后，发送邮件。
# 将代码有，封装成类，方便理解
# '''
#
#
# if __name__ == "__main__":
#     BaseAdb.adb_wake_up()
#     time.sleep(5)
#     # 获取当前网速
#     # ts = TestSpeed()
#     # ts.setUp()
#     # speed = ts.testCase()
#     # ts.tearDown()
#
#     # print("speed: %s" %speed)
#     speed=""
#
#     print('需要运行的脚本')
#     testtxt = []
#
#     _run = 5
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseLogin')) <=_run :
#         testtxt.append(('账号登录',"testCaseLogin"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseOnBtnLogin'))<=_run :
#         testtxt.append(('一键登录',"testCaseOnBtnLogin"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSend'))<=_run :
#         testtxt.append(('发送邮件带附件',"testCaseSend"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseFwdSend'))<=_run :
#         testtxt.append(('云端转发',"testCaseFwdSend"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseReply'))<=_run :
#         testtxt.append(('回复邮件',"testCaseReply"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseForward'))<=_run :
#         testtxt.append(('SMTP转发',"testCaseForward"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseCalendar'))<=_run :
#         testtxt.append(('日历',"testCaseCalendar"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseDiscover'))<=_run :
#         testtxt.append(('发现主页',"testCaseDiscover"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCasePersionMessages'))<=_run :
#         testtxt.append(('个人资料',"testCasePersionMessages"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSkyDrive'))<=_run :
#         testtxt.append(('彩云网盘',"testCaseSkyDrive"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testDownFile'))<=_run :
#         testtxt.append(('附件下载',"testDownFile"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseCheckAddressList'))<=_run :
#         testtxt.append(('联系人同步',"testCaseCheckAddressList"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSelected'))<=_run :
#         testtxt.append(('收件箱列表中精选',"testCaseSelected"))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCasePush'))<=_run :
#         testtxt.append(('接收推送',"testCasePush"))
#
#
#     suite = unittest.TestSuite()
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseOnBtnLogin'))<=_run :
#         suite.addTest(TestLogin('testCaseOnBtnLogin'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseLogin'))<=_run :
#         suite.addTest(TestLogin('testCaseLogin'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSend'))<=_run :
#         suite.addTest(TestSend('testCaseSend'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseFwdSend'))<= 5 :
#         suite.addTest(TestSend('testCaseFwdSend'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseForward'))<=_run :
#         suite.addTest(TestSend('testCaseForward'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseReply'))<=_run :
#         suite.addTest(TestSend('testCaseReply'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseCalendar'))<=_run :
#         suite.addTest(TestCalendar('testCaseCalendar'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseDiscover'))<=_run :
#         suite.addTest(TestDiscover('testCaseDiscover'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCasePersionMessages'))<=_run :
#         suite.addTest(TestPersion('testCasePersionMessages'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSkyDrive'))<=_run :
#         suite.addTest(TestSkyDrive('testCaseSkyDrive'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testDownFile'))<=_run :
#         suite.addTest(TestDownFile('testDownFile'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseCheckAddressList'))<=_run :
#         suite.addTest(TestContant('testCaseCheckAddressList'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCaseSelected'))<=_run :
#         suite.addTest(TestSelect('testCaseSelected'))
#
#     if int(ReadWriteConfFile.get_section_value('caseconf', 'testCasePush'))<=_run :
#         suite.addTest(TestPush('testCasePush'))
#
#     runner = unittest.TextTestRunner()
#
#
#
#     # 生成html
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     filename_now = time.strftime("%Y_%m_%d_%H_%M_%S")
#     filename = reportPath + now + '_result.html'
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(stream=fp,title='Test Report', description='DialsMeasured with: ')
#     testResultReport = runner.run(suite)
#     fp.close()
#
#
#
#     ReportClass(testResultReport.failures,testtxt,speed,now).all()
#
#     time.sleep(5)
#     # 休眠状态
#     BaseAdb.adb_sleep()
#
#     time.sleep(5)