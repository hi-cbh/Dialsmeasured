from src.mail.sendEmailSmtp import  SendMail
import time, datetime
import copy
from src.base.baseTime import BaseTime
from src.readwriteconf.rwconf import ReadWriteConfFile as rwc
from src.readwriteconf.initData import InitData
from src.readwriteconf.saveData import save
from src.readwriteconf.calcSucPer import CalcSuccess
from collections import Counter

logPath = InitData().getsysPath()["savepath"]+"/logs/"
logfileName= BaseTime.getDateHour() + '.log'

# 原始记录
orgFilePath = logPath + 'org_'+logfileName
# 原始记录待样式
htmlFilePath = logPath + 'html_'+logfileName
# 真实数据
tsaveFilePath = logPath + 'savet_'+logfileName
# 真实数据带样式
thtmlFilePath = logPath + 'true_'+logfileName
# 假数据
fsaveFilePath = logPath + 'savef_'+logfileName
# 假数据带样式
fhtmlFilePath = logPath + 'false_'+logfileName


class ReportClass(object):

    # 每一轮的错误次数
    _errortimes= 0
    # 错误用例列表
    _errorList = []
    # 统计用例结果字典
    _result = {}
    # 传入发送邮件结果列表
    _testcaselist = []


    def __init__(self, failReport={},caseresult=[], speed="",nowtime=""):
        '''获取报告的返回结果'''
        self.failReport = failReport # 结果
        self.caseresult = dict(caseresult) # 测试用例
        self.speed = speed # 当前上传下载网速
        self.nowtime = nowtime
        self.caseorg = copy.deepcopy(self.caseresult) # 深度拷贝


    def _getErrorCase(self):
        '''筛选错误的结果'''
        for case, reason in self.failReport:
            print("case：%s" % case)
            ReportClass._errorList.append(str(case))

    def _useCaseResults(self):
        '''统计用例结果字典'''
        # 中文与英文对应字典
        for k, v in self.caseresult.items():
            ReportClass._testcaselist.append(k) # 用例名加入列表
            ReportClass._result[v] = "Success"  # 创建字典

    def _sortFail(self):
        '''标识错误用例，筛选错误次数'''
        for k, v in ReportClass._result.items():
            for line in ReportClass._errorList:
                if line.find(k) != -1:
                    ReportClass._result[k] = 'Fail'
        print("_sortFail: %s" %ReportClass._result)


        rwc.addSection('caseconf')
        smax = int(rwc.getSectionValue("sendconf","maxtimes"))

        # 将caseconf的值，大于maxtimes的值，拷贝到reportconf
        '''
        caseconf 运行过程中出现连续错误case记录
        reportconf 出现了超过最大次数，时将caseconf记录到reportconf对应的用例中，若有，累计上一次出现的数组
        
        '''
        for k,v in ReportClass._result.items():
            rwc.addSection('caseconf')# 切换conf
            value = int(rwc.getSectionValue('caseconf',k))
            if v == "Success" and value >= smax :
                rwc.addSection('reportconf')# 切换
                tmp = int(rwc.getSectionValue("reportconf",k)) + value
                rwc.setSectionValue( 'reportconf',k,str(tmp))

        time.sleep(2)
        # 用于非连续错误用例清0
        rwc.addSection('caseconf')
        for k,v in ReportClass._result.items():
            if v == "Success" and int(rwc.getSectionValue('caseconf',k)) !=0 :
                rwc.setSectionValue( 'caseconf',k,"0")

        time.sleep(2)
        # 记录连续错误的用例
        for k,v in ReportClass._result.items():
            if v == "Fail":
                x = rwc.getSectionValue('caseconf',k)
                x = int(x) + 1
                rwc.setSectionValue( 'caseconf',k,str(x))



    def _mergeict(self):
        '''两个字典合并'''
        # 用例中文-英文替换
        for k1, v1 in ReportClass._result.items():
            for k2, v2 in self.caseresult.items():
                if k1 == v2:
                    self.caseresult[k2] = ReportClass._result[k1]

    def _saveDate(self):
        '''保存每一轮的数据，分为带样式和无样式'''
        # 获取用例对应的时延
        demotime=save.getValue()
        print("时延：%s" %demotime)

        resulttxt = [] # 写入日志
        resulttxt.append('\n'+"====="+self.nowtime +"====="+'\n')
        resulttxt.append(self.speed +'\n')

        sendresult = [] # 邮件发送正文
        sendresult.append('\n'+"====="+self.nowtime +"====="+'\n')
        sendresult.append(self.speed+'\n')

        # 写入文件，并添加发送邮件格式
        for case, reason in self.caseresult.items():
            # 含有时延的用例
            if case in demotime:
                resulttxt.append('case：%s , 时延：%s, result：%s \n' %(case,demotime[case], reason ))
                if reason == 'Fail':
                    # 用例错误
                    sendresult.append('case：<font size="3" color="blue"> %s </font> ,result：<font size="4" color="red"> %s </font>\n' %(case, reason) )
                else:
                    # 用例Success
                    sendresult.append('case：<font size="3" color="blue"> %s </font> , 时延：%s,  result：<font size="3" color="green"> %s </font>\n' %(case,demotime[case], reason) )
            # 不含时延的用例
            else:
                resulttxt.append('case：%s , result：%s \n' %(case, reason))
                if reason == 'Fail':
                    # 用例错误
                    sendresult.append('case：<font size="3" color="blue"> %s </font> , result：<font size="4" color="red"> %s </font>\n' %(case, reason) )
                else:
                    # 用例success
                    sendresult.append('case：<font size="3" color="blue"> %s </font> , result：<font size="3" color="green"> %s </font>\n' %(case, reason) )


        # print("过滤日志，写入日志：%s" %resulttxt)
        # print("过滤日志，写入日志：%s" %sendresult)


        #每天的测试记录
        for line in resulttxt:
            with open(orgFilePath,'a+') as fn:
                fn.write(line)

        #每天的测试记录(邮件内容)
        for line in sendresult:
            with open(htmlFilePath,'a+') as fs:
                fs.write(line)

    def _readCaseConf(self,max):
        '''读取caseconf用例连续错误次数记录最大值用例'''
        errl = []
        rwc.addSection('caseconf')
        for k,v in ReportClass._result.items():
            tmp = int(rwc.getSectionValue('caseconf',k))
            if tmp >= max and tmp % max == 0: # 最大值的倍数才加入列表
                errl.append(k)


        # print("_readCaseConf: %s" %errl)
        # print("self.caseorg: %s" %self.caseorg)
        tmpl = []
        # 筛选出用例名称
        for line in errl:
            # print("line: %s" %line)
            for k, v in self.caseorg.items():
                if line == v:
                    tmpl.append(k)


        # print("_readCaseConf2: %s" %tmpl)

        return tmpl

    def _getReportConf(self):
        '''返回：{用例：连续错误次数}，读取reportconf'''
        # print("self.caseorg: %s" %self.caseorg)
        errl = {}
        rwc.addSection('sendconf')
        smax = int(rwc.getSectionValue("sendconf","maxtimes"))

        rwc.addSection('reportconf')
        for k,v in self.caseorg.items():
            tmpvalue = int(rwc.getSectionValue('reportconf',v))
            if tmpvalue>=smax:
                errl[k] = tmpvalue

        # print("_getReportConf: %s" %errl)

        return errl


    def _getCaseConf(self):
        '''返回：{用例：连续错误次数}，读取caseconf'''
        # print("self.caseorg: %s" %self.caseorg)
        errl = {}
        rwc.addSection('sendconf')
        smax = int(rwc.getSectionValue("sendconf","maxtimes"))

        rwc.addSection('caseconf')
        for k,v in self.caseorg.items():
            tmpvalue = int(rwc.getSectionValue('caseconf',v))
            if tmpvalue>=smax:
                errl[k] = tmpvalue

        # print("_getCaseConf: %s" %errl)

        return errl

    def _getAddConf(self):
        '''读取caseconf与reportconf两个的和，两个字典相加'''
        return dict(Counter(self._getCaseConf())+Counter(self._getReportConf()))


    def _setCaseConf(self):
        '''各个用例复位'''
        rwc.addSection('caseconf')
        for k,v in ReportClass._result.items():
            rwc.setSectionValue('caseconf',k,"0")

        rwc.addSection('reportconf')
        for k,v in ReportClass._result.items():
            rwc.setSectionValue('reportconf',k,"0")


    def saveTrueAndFailLog(self):
        '''存储每天的记录，包括统计，并做数据处理（连续出现错误，不纳入计算）'''
        # 清空数据
        with open(thtmlFilePath,'w') as fq:
            fq.write("")
        with open(tsaveFilePath,'w') as fq:
            fq.write("")
        # 假数据
        with open(fhtmlFilePath,'w') as fq:
            fq.write("")
        with open(fsaveFilePath,'w') as fq:
            fq.write("")

        # 中文用例名：连续错误次数
        caselt = self._getAddConf()
        print("连续错误次数：%s" %caselt)
        time.sleep(5)
        # 计算成功率
        cs = CalcSuccess(ReportClass._testcaselist,orgFilePath)

        writeTime = "====="+BaseTime.getCurrentTime()+"  当天运行记录结果汇总===== \n"
        writeLine = "\n注意：若出现连续出错的功能时，该错误次数不纳入计算范围 \n=====详细结果如下====="

        # 真实数据
        # 写入成功率
        print("写入html文件")
        with open(thtmlFilePath,'a+') as fq, open(htmlFilePath,'r') as fp:
            # 写入创建时间
            fq.write(writeTime)
            # 写入成功率及时延
            for cline in cs.getSuccessercentage(caselt):
                fq.write(cline)
            # 说明
            fq.write(writeLine)

            # 读取详细文件，拷贝到其他文件
            for line in fp:
                fq.write(line)

        time.sleep(3)

        # 写入成功率
        print("写入org文件")
        with open(tsaveFilePath,'a+') as fq, open(orgFilePath,'r') as fp:
            fq.write(writeTime)
            # 写入成功率及时延<无样式>
            for cline in cs.getSuccessercentageNotType(caselt):
                fq.write(cline)
            fq.write(writeLine)

            # 读取详细文件，拷贝到其他文件
            for line in fp:
                fq.write(line)


        # 写入成功率--> 假数据(需要修改成功率)
        print("写入成功率--> 假数据(需要修改成功率)")
        with open(fhtmlFilePath,'a+') as fq, open(htmlFilePath,'r') as fp:
            fq.write(writeTime)
            for cline in cs.getSuccessercentageFail(caselt):
                fq.write(cline)
            fq.write(writeLine)

            # 错误数量：{caseName:[总数，错误数量]}
            failcnt = cs._sortData()
            # 获取一个字典，第一个总数量
            cnt = sorted(failcnt.items())[0][1][0]

            '''
            测试用例总数35为分界点，
            低于35，全部用例错误的标为success
            高于35，各个用例数量，最多只显示一个错误
            '''
            if cnt < 35:

                # 读取详细文件，拷贝到其他文件
                for line in fp:
                    # 这里过滤fail
                    if line.find("Fail") != -1:
                        line = line.replace("Fail", "Success")
                        line = line.replace("red","green")
                    fq.write(line)
            else:
                # 读取详细文件，拷贝到其他文件
                for line in fp:
                    for caseName, value in failcnt.items():
                        if caseName in line and line.find("Fail") != -1 and value[1] >=2 :
                            line = line.replace("Fail", "Success")
                            line = line.replace("red","green")
                            value[1] = value[1] - 1
                    fq.write(line)

        print("写入成功率--> 假数据(需要修改成功率)")
        with open(fsaveFilePath,'a+') as fq, open(orgFilePath,'r') as fp:
            fq.write(writeTime)
            for cline in cs.getSuccessercentageFailNotType(caselt):
                fq.write(cline)
            fq.write(writeLine)

            # 错误数量：{caseName:[总数，错误数量]}
            failcnt = cs._sortData()
            # 获取一个字典，第一个总数量
            cnt = sorted(failcnt.items())[0][1][0]
            print("总数量：%s" %cnt)
            if cnt < 35:

                # 读取详细文件，拷贝到其他文件
                for line in fp:
                    # 这里过滤fail
                    print("line: %s" %line)
                    if line.find("Fail") != -1:
                        # print("替换前 line: %s" %line)
                        line = line.replace("Fail", "Success")
                        # print("替换后 line: %s" %line)
                    fq.write(line)
            else:
                # 读取详细文件，拷贝到其他文件
                for line in fp:
                    for caseName, value in failcnt.items():
                        if caseName in line and line.find("Fail") != -1 and value[1] >=2 :
                            line = line.replace("Fail", "Success")
                            value[1] = value[1] - 1
                    fq.write(line)




    def send(self):
        '''
        1、连续出现N次错误，发送邮件，邮件为一句话。
        2、出现错误的结果不纳入计算范围内
        :return:
        '''

        rwc.addSection( 'sendconf')
        changetime = rwc.getSectionValue('sendconf','changetime')
        changetime = int (changetime)


        print('当前时间：%s ' %datetime.datetime.now().hour)
        print('对比时间：%s ' %changetime)
        # 当前是否在固定时间内 [18,19] 下午 6-7点
        if datetime.datetime.now().hour in  [changetime]:
        # if datetime.datetime.now().hour in  [14,15]:

            # 是否发送
            sendOrNot = rwc.getSectionValue('sendconf','send')
            print('sendOrNot %s' %sendOrNot)
            if sendOrNot == 'False':
                print('到点发送邮件')

                # 读取
                self.saveTrueAndFailLog()

                time.sleep(5)
                with open(logPath + 'true_'+logfileName,'r') as fq:
                    allSendtxt = fq.readlines()

                time.sleep(5)
                with open(logPath + 'false_'+logfileName,'r') as fq:
                    falseTxt = fq.readlines()


                #==============发送内容读取=========


                print("预备发送 %s：" %allSendtxt)

                s = SendMail("13580491603","chinasoft123","13697485262")
                # 发送假数据
                s.sendMailMan('139Android客户端V722版本_功能拨测_汇总<发给移动>',falseTxt)
                time.sleep(10)
                # 发送真数据
                s.sendMailMan('139Android客户端V722版本_功能拨测_汇总<内部邮件>',allSendtxt)
                rwc.setSectionValue('sendconf','send','True')
                # #发送后，用例是否复位
                self._setCaseConf()

        else:
            if rwc.getSectionValue("sendconf","send") == "True":
                rwc.setSectionValue('sendconf','send','False')

            maxtimes = rwc.getSectionValue('sendconf','maxtimes')
            err = self._readCaseConf(int(maxtimes))
            # 错误次数
            if len(err) != 0:
                errstr = ','.join(err) + "到目前为止，以上提及的功能出现多次错误，请及时查证"
                s = SendMail("13580491603","chinasoft123","13697485262")
                s.sendMailMan2Str('139Android客户端V722版本_功能拨测_出现错误<内部邮件>',errstr)


        print('运行结束')
        time.sleep(15)



    def all(self):
        self._getErrorCase()
        self._useCaseResults()
        self._sortFail()
        self._mergeict()
        self._saveDate()
        self.send()
