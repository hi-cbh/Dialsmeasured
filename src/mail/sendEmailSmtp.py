#!/usr/bin/python  
# -*- coding: utf-8 -*-  
import smtplib  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
from email.mime.multipart import MIMEMultipart  
from email.header import Header  
from email.utils import parseaddr, formataddr  
# 格式化邮件地址


class SendMail():
    '''单个接收者'''
    def __init__(self, username, pwd, receive):
        self.username = username
        self.pwd = pwd
        self.receive = receive


    def _formatAddr(self, s):
        '''格式化地址'''
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def sendMail(self, subject, body):
        '''发送邮件'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd
        to_mail = self.receive + '@139.com'
        msg = MIMEText(body, 'plain', 'utf-8')
        # Header对中文进行转码
        msg['From'] = self._formatAddr(u"拨测账号 <%s>" %from_mail)
        msg['To'] = self._formatAddr(u"接收者 <%s>" %to_mail)
        msg['Subject'] = Header(subject, 'utf-8')

        try:
            s = smtplib.SMTP()
            s.connect(smtp_server, "25")
            s.login(from_mail, mail_pass)
            s.sendmail(from_mail, to_mail, msg.as_string())
            s.quit()
            print("发送成功")
        except smtplib.SMTPException as e:
            print("Error: %s" % e)
            return False
        else:
            return True




    def sendMailLog(self, subject, message=[]):
        '''发送邮件'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd
        to_mail = self.receive + '@139.com'

        body = []
        for ts in message:
            for txt in ts:
                if len(txt) > 2 :
                    txt = txt[:-1]
                    txt = "<p>"+ txt +"</p>"
                    body.append(txt)
                    # print(txt)


        body=''.join(body)

        msg = MIMEText(body, 'html', 'utf-8')
        # Header对中文进行转码
        msg['From'] = self._formatAddr(u"拨测账号 <%s>" %from_mail)
        msg['To'] = self._formatAddr(u"接收者 <%s>" %to_mail)
        msg['Subject'] = Header(subject, 'utf-8')

        try:
            s = smtplib.SMTP()
            s.connect(smtp_server, "25")
            s.login(from_mail, mail_pass)
            s.sendmail(from_mail, to_mail, msg.as_string())
            s.quit()
            print("发送成功")
        except smtplib.SMTPException as e:
            print("Error: %s" % e)
            return False
        else:
            return True


    def sendMailMan(self, subject, message=[]):
        '''发送邮件'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd
        # to_mail = self.receive + '@139.com'
        areceiver = '13533348571@139.com,13790383896@139.com,18022340679@139.com'
        # areceiver = '13533348571@139.com'

        body = []
        for txt in message:
            if len(txt) > 2 :
                txt = txt[:-1]
                txt = "<p>"+ txt +"</p>"
                body.append(txt)
                # print(txt)


        body=''.join(body)

        # print("邮件正式发送内容： %s" %body)


        msg = MIMEText(body, 'html', 'utf-8')
        # Header对中文进行转码
        msg['From'] = self._formatAddr(u"拨测账号 <%s>" %from_mail)
        # msg['To'] = self._formatAddr(u"接收者 <%s>" %to_mail)
        msg['To'] = areceiver
        msg['Subject'] = Header(subject, 'utf-8')

        try:
            s = smtplib.SMTP()
            s.connect(smtp_server, "25")
            s.login(from_mail, mail_pass)
            s.sendmail(from_mail, areceiver.split(','), msg.as_string())
            s.quit()
            print("发送成功")
        except smtplib.SMTPException as e:
            print("Error: %s" % e)
            return False
        else:
            return True

    def sendMailMan2(self, subject, message=[]):
        '''发送邮件，固定格式'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd
        # to_mail = self.receive + '@139.com'
        # areceiver = '13533348571@139.com,13501538531@139.com,wujun11121@163.com'
        areceiver = '13533348571@139.com'

        body = []
        for txt in message:
            if len(txt) > 2 :
                # txt = txt[:-1] # 含有换行符才需要
                txt = "<p>"+ txt +"</p>"
                body.append(txt)
                # print(txt)


        body=''.join(body)

        # print("邮件正式发送内容： %s" %body)
        print('邮件正式发送')

        msg = MIMEText(body, 'html', 'utf-8')
        # Header对中文进行转码
        msg['From'] = self._formatAddr(u"拨测账号 <%s>" %from_mail)
        # msg['To'] = self._formatAddr(u"接收者 <%s>" %to_mail)
        msg['To'] = areceiver
        msg['Subject'] = Header(subject, 'utf-8')

        try:
            s = smtplib.SMTP()
            s.connect(smtp_server, "25")
            s.login(from_mail, mail_pass)
            s.sendmail(from_mail, areceiver.split(','), msg.as_string())
            s.quit()
            print("发送成功")
        except smtplib.SMTPException as e:
            print("Error: %s" % e)
            return False
        else:
            return True

    def sendMailMan2Str(self, subject, message=""):
        '''发送邮件，固定格式'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd
        # to_mail = self.receive + '@139.com'
        areceiver = '13533348571@139.com,13790383896@139.com,18022340679@139.com'
        # areceiver = '13533348571@139.com'

        body = []
        body.append(message)
        body=''.join(body)

        # print("邮件正式发送内容： %s" %body)
        print('邮件正式发送')

        msg = MIMEText(body, 'html', 'utf-8')
        # Header对中文进行转码
        msg['From'] = self._formatAddr(u"拨测账号 <%s>" %from_mail)
        # msg['To'] = self._formatAddr(u"接收者 <%s>" %to_mail)
        msg['To'] = areceiver
        msg['Subject'] = Header(subject, 'utf-8')

        try:
            s = smtplib.SMTP()
            s.connect(smtp_server, "25")
            s.login(from_mail, mail_pass)
            s.sendmail(from_mail, areceiver.split(','), msg.as_string())
            s.quit()
            print("发送成功")
        except smtplib.SMTPException as e:
            print("Error: %s" % e)
            return False
        else:
            return True

    def sendMailManStr(self, subject, message=""):
        '''发送邮件，固定格式'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd
        # to_mail = self.receive + '@139.com'
        # areceiver = '13533348571@139.com,13790383896@139.com,18022340679@139.com'
        areceiver = '13533348571@139.com'

        body = []
        body.append(message)
        body=''.join(body)

        # print("邮件正式发送内容： %s" %body)
        print('邮件正式发送')

        msg = MIMEText(body, 'html', 'utf-8')
        # Header对中文进行转码
        msg['From'] = self._formatAddr(u"拨测账号 <%s>" %from_mail)
        # msg['To'] = self._formatAddr(u"接收者 <%s>" %to_mail)
        msg['To'] = areceiver
        msg['Subject'] = Header(subject, 'utf-8')

        try:
            s = smtplib.SMTP()
            s.connect(smtp_server, "25")
            s.login(from_mail, mail_pass)
            s.sendmail(from_mail, areceiver.split(','), msg.as_string())
            s.quit()
            print("发送成功")
        except smtplib.SMTPException as e:
            print("Error: %s" % e)
            return False
        else:
            return True
if __name__ == "__main__":

    s = SendMail("13580491603","chinasoft123","13697485262")
    # s.sendMail('testEmail','Python 邮件发送测试...')

    line = ["testemail"]
    # with open("/Users/apple/autoTest/workspace/DialsMeasured/logs/run.log",'r') as fn:
    #     line.append(fn.readlines())

    # print(line)

    s.sendMailMan('测试,是否收到邮件',line)
