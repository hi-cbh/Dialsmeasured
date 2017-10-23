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
        msg['From'] = self._formatAddr(u"发送者 <%s>" %from_mail)
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


if __name__ == "__main__":

    s = SendMail("13580491603","chinasoft123","13580491603")
    s.sendMail('testEmail','Python 邮件发送测试...')