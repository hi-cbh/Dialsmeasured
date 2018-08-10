# urs/bin/python
# encoding:utf-8
import unittest,os,sys,time



p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("all53 path: %s" %p)
sys.path.append(p+"/")

# 添加环境路径，脚本
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
from src.testcase.HTMLTestRunner import HTMLTestRunner
from src.reportlib.reportclass import ReportClass
from src.base.baseAdb import BaseAdb
from src.readwriteconf.rwconf import ReadWriteConfFile
from src.sql.sql import DB
from src.base.baseTime import BaseTime
from src.sql.docker_mysql import DockerDB
from src.readwriteconf.changehourerror import HourError
localPath = "/var/appiumRunLog"
# 信息存储路径
reportPath = localPath + "/report/"

users = duser().getuser()
user = {"name": users['name'], 'pwd': users['pwd']}

'''
1、账号统一；
2、用例使用一个文件中
'''
class TestCase(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(self):
        BaseAdb.adb_wake_up()
        time.sleep(10)

        devicename = BaseAdb.adb_devicename()
        if devicename.__contains__("vivo"):
            BaseAdb.adb_intall_uiautmator()

        self.driver = Psam(version="6.0")
        EmailOperation(user["name"]+"@139.com", user["pwd"]).clear_forlder(['INBOX'])

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("运行结束")
        time.sleep(5)

    def testCaseOnBtnLogin(self):
        '''一键登录'''
        TestLogin(self.driver).testCaseOnBtnLogin()

    def testCaseLogin(self):
        '''账号登录'''
        TestLogin(self.driver).testCaseLogin()

    def testCaseSendNoAttach(self):
        '''发送邮件，无附件'''
        TestSend(self.driver).testCaseSendNoAttach()

    def testCaseSendAttach(self):
        '''发送邮件，带附件'''
        TestSend(self.driver).testCaseSendAttach()

    def testCaseFwdSend(self):
        '''云端转发'''
        TestSend(self.driver).testCaseFwdSend()

    def testCaseReply(self):
        '''回复邮件'''
        TestSend(self.driver).testCaseReply()

    def testCaseForward(self):
        '''SMTP转发附件'''
        TestSend(self.driver).testCaseForward()

    def testDownFile(self):
        '''下载附件'''
        TestDownFile(self.driver).testDownFile()

    def testCaseCalendar(self):
        '''日历'''
        TestCalendar(self.driver).testCaseCalendar()

    def testCaseDiscover(self):
        '''发现主页'''
        TestDiscover(self.driver).testCaseDiscover()

    def testCasePersionMessages(self):
        '''个人资料'''
        TestPersion(self.driver).testCasePersionMessages()

    def testCaseCheckAddressList(self):
        '''联系人同步'''
        TestContant(self.driver).testCaseCheckAddressList()

    def testCaseSelected(self):
        '''收件箱列表139精选'''
        TestSelect(self.driver).testCaseSelected()

    def testCaseSkyDrive(self):
        '''彩云网盘'''
        TestSkyDrive(self.driver).testCaseSkyDrive()

    def testCasePush(self):
        '''推送'''
        TestPush(self.driver).testCasePush()


# 创建一个返回字典的方法
def get_dict(data_dict = {}, case_list=[]):

    new_dict = {}
    for k,v in data_dict.items():
        if k in case_list:
            new_dict[k] = int(v)

    new_dict["times"] = BaseTime.get_current_time()

    return new_dict


if __name__ == "__main__":

    print("=================更新到数据库=================")
    l = ['testcaseonbtnlogin', 'testcaselogin', 'testcasesendnoattach', 'testcasesendattach', 'testcasefwdsend', 'testcaseforward', 'testcasereply', 'testdownfile', 'testcasecheckaddresslist', 'testcaseselected', 'testcasepush', 'testcasecalendar', 'testcasediscover', 'testcasepersionmessages', 'testcaseskydrive']

    new_dict2 = get_dict(dict(ReadWriteConfFile.read_section_all("caseconf")),l)

    print(new_dict2)

    # ------------- 更新汇总数据库------------
    error_dict2 = get_dict(dict(ReadWriteConfFile.read_section_all("errorconf")),l)
    print(error_dict2)
    # 更新本地数据库
    DB().update("test_data",new_dict2)

    # 更新到阿里云
    DockerDB().update("sign_case",new_dict2)
    DockerDB().update("sign_error",error_dict2)

    ReadWriteConfFile.value_set_true_false(True)

    try:
        hour_dict = get_dict(dict(ReadWriteConfFile.read_section_all("errorhourconf")),l)
        HourError().setData(hour_dict)
    except BaseException as e:
        print(e)
        print("每小时更新数据库，错误")




    print('=================中文-英文对应测试用例=================')
    testtxt = []
    testtxt.append(('一键登录',"testCaseOnBtnLogin"))
    testtxt.append(('账号登录',"testCaseLogin"))
    testtxt.append(('发送邮件无附件',"testCaseSendNoAttach"))
    testtxt.append(('发送邮件带附件',"testCaseSendAttach"))
    testtxt.append(('云端转发',"testCaseFwdSend"))
    testtxt.append(('回复邮件',"testCaseReply"))
    testtxt.append(('SMTP转发',"testCaseForward"))
    testtxt.append(('日历',"testCaseCalendar"))
    testtxt.append(('发现主页',"testCaseDiscover"))
    testtxt.append(('个人资料',"testCasePersionMessages"))
    testtxt.append(('彩云网盘',"testCaseSkyDrive"))
    testtxt.append(('附件下载',"testDownFile"))
    testtxt.append(('联系人同步',"testCaseCheckAddressList"))
    testtxt.append(('收件箱列表中精选',"testCaseSelected"))
    testtxt.append(('接收推送',"testCasePush"))

    print('=================测试用例加入测试套件=================')
    suite = unittest.TestSuite()
    suite.addTest(TestCase('testCaseOnBtnLogin'))
    suite.addTest(TestCase('testCaseLogin'))
    suite.addTest(TestCase('testCaseSendNoAttach'))
    suite.addTest(TestCase('testCaseSendAttach'))
    suite.addTest(TestCase('testCaseFwdSend'))
    suite.addTest(TestCase('testCaseForward'))
    suite.addTest(TestCase('testCaseReply'))
    suite.addTest(TestCase('testCaseDiscover'))
    suite.addTest(TestCase('testCaseCalendar'))
    suite.addTest(TestCase('testCasePersionMessages'))
    suite.addTest(TestCase('testCaseSkyDrive'))
    suite.addTest(TestCase('testDownFile'))
    suite.addTest(TestCase('testCaseCheckAddressList'))
    suite.addTest(TestCase('testCaseSelected'))
    suite.addTest(TestCase('testCasePush'))
    runner = unittest.TextTestRunner()




    print('=================运行测试=================')
    # 生成html
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    fp = open(reportPath + now + '_result.html', 'wb')
    runner = HTMLTestRunner(stream=fp,title='Test Report', description='DialsMeasured with: ')
    testResultReport = runner.run(suite)
    fp.close()
    print('=================运行结束=================')

    print("=================更新到数据库=================")
    l = ['testcaseonbtnlogin', 'testcaselogin', 'testcasesendnoattach', 'testcasesendattach', 'testcasefwdsend', 'testcaseforward', 'testcasereply', 'testdownfile', 'testcasecheckaddresslist', 'testcaseselected', 'testcasepush', 'testcasecalendar', 'testcasediscover', 'testcasepersionmessages', 'testcaseskydrive']

    new_dict = get_dict(dict(ReadWriteConfFile.read_section_all("caseconf")),l)
    print(new_dict)

    DB().update("test_data",new_dict)

    DockerDB().update("sign_case",new_dict)

    try:
        hour_dict = get_dict(dict(ReadWriteConfFile.read_section_all("errorhourconf")),l)
        HourError().setData(hour_dict)
    except BaseException as e:
        print(e)
        print("每小时更新数据库，错误")


    # 休眠状态
    BaseAdb.adb_sleep()
    time.sleep(5)
    print('=================处理测试结果=================')
    ReportClass(testResultReport.failures,testtxt,"",now).all()
    print("=================结束=================")