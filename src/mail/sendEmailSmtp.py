#!/usr/bin/python  
# -*- coding: utf-8 -*-  
import smtplib,time
from email.mime.text import MIMEText  
from email.header import Header
from email.utils import parseaddr, formataddr

# 格式化邮件地址

#单个测试邮件
tester = "13533348571@139.com"
# 多个联系人
mamEmail='13533348571@139.com,18022340679@139.com,13790383896@139.com'
# mamEmail=''
# 发给其他人的
mamEmailOther='13533348571@139.com,18022340679@139.com,13790383896@139.com,13802883234@139.com,wenyaoneng@139.com,13610128827@139.com,13580491687@163.com'

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


    def send_mail_test(self, subject, body):
        '''发送辅助的邮件，使用第三方发送给客户端，验证转发邮件的用例'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd
        to_mail = self.receive + '@139.com'
        msg = MIMEText(body, 'plain', 'utf-8')
        # Header对中文进行转码
        msg['From'] = self._format_addr(u"拨测账号 <%s>" %from_mail)
        msg['To'] = self._format_addr(u"接收者 <%s>" %to_mail)
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



    def send_mail(self, subject, message=[], is_test=False):
        '''发送邮件，固定格式'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd
        if is_test:
            areceiver = tester
        else:
            areceiver = mamEmail

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

    def send_mail_test2(self, subject, message=[], is_test=False):
        '''发送邮件，固定格式'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd
        if is_test:
            areceiver = self.receive + '@139.com'
        else:
            areceiver = mamEmail

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

    def send_mail_out(self, subject, message=[], is_test=False):
        '''发送邮件，固定格式，发送移动'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd
        if is_test:
            areceiver = '13533348571@139.com'
        else:
            areceiver = mamEmailOther

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


    def send_mail_str(self, subject, message="", is_test=False):
        '''发送邮件，固定格式'''
        smtp_server = 'smtp.139.com'
        from_mail = self.username + '@139.com'
        mail_pass = self.pwd
        if is_test:
            areceiver = tester
        else:
            areceiver = mamEmailOther


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

    def send_mail_str_163(self, subject, message="", is_test=False):
        '''发送邮件，固定格式'''
        smtp_server = 'smtp.163.com'
        from_mail = self.username + '@163.com'
        mail_pass = self.pwd

        if is_test:
            areceiver = 'hi_cbh@qq.com'
        else:
            areceiver = "hi_cbh@qq.com,wujun11121@163.com"
            # areceiver = "hi_cbh@qq.com"


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
            # s.connect(smtp_server, "465")
            s.login(from_mail, mail_pass)
            s.sendmail(from_mail, areceiver.split(','), msg.as_string())
            s.quit()
            print("发送成功")
        except smtplib.SMTPException as e:
            print("Error: %s" % e)
            return False
        else:
            return True

    def send_mail_str_163_ssl(self, subject, message="", is_test=False):
        '''发送邮件，固定格式'''
        smtp_server = 'smtp.163.com'
        from_mail = self.username + '@163.com'
        mail_pass = self.pwd

        if is_test:
            # areceiver = 'hi_cbh@qq.com'
            areceiver = '13501538531@139.com'
        else:
            # areceiver = "hi_cbh@qq.com,wujun11121@163.com"
            areceiver = "hi_cbh@qq.com"


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
            s = smtplib.SMTP_SSL(smtp_server, "465") # ssl去除 connect
            s.login(from_mail, mail_pass)
            s.sendmail(from_mail, areceiver.split(','), msg.as_string())
            s.quit()
            print("发送成功")
        except smtplib.SMTPException as e:
            print("Error: %s" % e)
            return False
        else:
            return True

    def send_mail_out_163(self, subject, message=[], is_test=False):
        '''发送邮件，固定格式，发送移动'''
        smtp_server = 'smtp.163.com'
        from_mail = self.username + '@163.com'
        mail_pass = self.pwd
        if is_test:
            areceiver = 'hi_cbh@qq.com'
        else:
            areceiver = mamEmailOther

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

    s = SendMail("13580491603","chinasoft123","13533218540")

    for i in range(1):


        # s.sendMail('testEmail','Python 邮件发送测试...')

        line = ["testemail"]
        s.send_mail_str_163("testEmail"," 邮件发送测试",is_test=True)
        # s.send_mail_out_163("testEmail",["邮件发送测试","test2"],is_test=True)
        time.sleep(5)
