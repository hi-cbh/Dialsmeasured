#!/usr/bin/python  
# -*- coding: utf-8 -*-  


import smtplib,time
from email.mime.text import MIMEText  
from email.header import Header
from email.utils import parseaddr, formataddr

'''
自动发送邮件
pip3 install pyzmail  # 邮件

'''

class SendMail():
    '''单个接收者'''
    def __init__(self, username, pwd, receive):
        self.username = username
        self.pwd = pwd
        self.receive = receive


    def _format_addr(self, s):
        '''格式化地址'''
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))


    def send_mail_str(self, subject, message=""):
        '''发送邮件，固定格式'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd

        areceiver = self.receive


        body = []
        body.append(message)
        body=''.join(body)

        # print("邮件正式发送内容： %s" %body)
        print('邮件正式发送')

        msg = MIMEText(body, 'html', 'utf-8')
        # Header对中文进行转码
        msg['From'] = self._format_addr(u"拨测账号 <%s>" % from_mail)
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

    s = SendMail("发送者账号","发送者密码","接收者"+ '@139.com')

    for i in range(1):

        s.send_mail_str("主题"," 正文")
        time.sleep(5)
