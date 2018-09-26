# urs/bin/python
# encoding:utf-8

import os
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class BaseAdb(object):
    
    def __init__(self):
        self.path=""

    def adb_version(self):
        '''获取版本号'''
        try:
            result = os.popen("adb shell dumpsys package cn.cj.pe |grep versionName")

            return result.readline().split("=")[1]
        except BaseException:
            return "1.1.1"


    def adb_stop(self, cmd):
        '''杀进程'''
        self.adb_shell(self.path + 'adb shell am force-stop %s' % cmd)


    def adb_devicename(self):
        '''设备名称'''
        value = os.popen("adb shell getprop ro.product.model")
        return  value.readline()


    def add_pressmission(self):
        '''添加权限'''
        pre = {
            "WRITE_EXTERNAL_STORAGE":"android.permission.WRITE_EXTERNAL_STORAGE",
            "READ_EXTERNAL_STORAGE":"android.permission.READ_EXTERNAL_STORAGE",
            "READ_PHONE_STATE":"cn.cj.pe android.permission.READ_PHONE_STATE",
            "READ_CONTACTS":"android.permission.READ_CONTACTS",
            "RECEIVE_SMS":"android.permission.RECEIVE_SMS",
            "READ_SMS":"android.permission.READ_SMS",
            "SEND_SMS":"cn.cj.pe android.permission.SEND_SMS",
            "CALL_PHONE":"android.permission.CALL_PHONE"
        }

        for _,v in pre.items():
            self.adb_shell("adb shell pm grant " + v)

    def adb_intall_uiautmator(self):
        '''调用以及导入的jar包，运行uiautmator辅助工具'''
        self.adb_shell(self.path + "adb shell uiautomator runtest installApk.jar --nohup -c com.uitest.testdemo.installApk")

    def adb_intall_uiautmator37(self):
        '''调用以及导入的jar包，运行uiautmator辅助工具'''
        self.adb_shell(self.path + "adb shell uiautomator runtest installApkVivo.jar --nohup -c com.uitest.testdemo.installApkVivo")


    def adb_wake_up(self):
        '''手机进行唤醒并解锁'''
        self.adb_shell(self.path + "adb shell uiautomator runtest powerOffAndOn.jar --nohup -c com.uitest.testdemo.powerOffAndOn")

    def adb_sleep(self):
        '''手机进行休眠状态'''
        self.adb_shell(self.path + "adb shell uiautomator runtest powerSleep.jar --nohup -c com.uitest.testdemo.powerSleep")

    def adb_tap(self, x, y):
        '''通过坐标，点击屏幕'''
        self.adb_shell(self.path + "adb shell input tap %s %s " % (str(x), str(y)))
    
    def adb_back(self):
        '''通过命令行，点击返回'''
        self.adb_shell(self.path + 'adb shell input keyevent 4')
        time.sleep(2)
    
    def adb_input_text(self, txt):
        '''通过命令行，输入字段'''
        self.adb_shell(self.path + 'adb shell input text %s' % txt)
    
    def adb_home(self):
        '''通过命令行，点击返回'''
        self.adb_shell(self.path + 'adb shell input keyevent 3')
        time.sleep(1)
    
    def adb_entry(self):
        '''通过命令行，发送接邮件的广播'''
        self.adb_shell(self.path + 'adb shell am broadcast -a mybroadcast')


    def adb_start_app(self, pag, activity):
        '''通过命令行，启动应用'''
        self.adb_shell(self.path + 'adb shell am start -n %s/%s' % (pag, activity))
    
    def adb_broadcast_sms(self, name):
        '''通过命令，发送广播，传递错误用例'''
        self.adb_start_app("com.hy.sms.androidtestsms",".MainActivity")
        time.sleep(5)
        self.adb_home()
        time.sleep(5)
        self.adb_shell(self.path + 'adb shell am broadcast -a hy.smsbroadcast --es name %s' %name)
            
    def adb_get_wifi_on(self):
        '''获取当前的wifi状态，开启返回True'''
        value = os.popen(self.path+"adb shell settings get global wifi_on","r")
#         print(value.readline())
        if not '0' in value.readline() :
            return True
        else:
            return False

    def get_network_type(self):
        '''读取手机网络'''
        if(self.adb_get_wifi_on() != True):
            print("4G")
            return '4G'
        else:
            print("CMCC")
            return 'CMCC'   
    
    
    def adb_get_apk_version(self, pkg):
        '''获取apk版本'''
        command_result=""
        results = os.popen(self.path+"adb shell dumpsys package %s | findstr versionName" %pkg)
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()

        command_result = command_result.split('=')[1]
        
        print(command_result)
        return command_result
        
    
            
    def adb_shell(self, cmd):
        try:
            print(cmd)
            os.popen(cmd)
            # self.testsubprocess(cmd)
        except BaseException:
            print('命令调用出错')

    def adb_clear(self, pkgname):
        '''清除缓存'''
        os.popen(self.path+"adb shell pm clear %s"  %pkgname)
    
    def adb_broadcast(self):
        '''发送自定义广播'''
        os.popen(self.path+"adb shell am broadcast -a mybroadcast")


    # 拉数据到本地
    def adb_pull(self, remote, local):
        print("adb pull %s %s"  %(remote, local))
        result=os.popen("adb pull %s %s"  %(remote, local))
        print(result.readline())

    def adb_apk_exist(self, pkg):
        '''第三方包是否安装'''
        results = os.popen("adb shell pm list package -3")
        for line in results.readlines():                          #依次读取每行
            line = line.strip()                             #去掉每行头尾空白
            if not line:       #判断是否是空行或注释行
                continue
            if pkg in line:
                # print('true')
                return True
        else:
            # print('False')
            return False



    def install_app(self, p):
        '''安装APK'''
        os.popen("adb wait-for-device")
        os.popen("adb install %s" %p)
        time.sleep(5)
        os.popen("adb shell uiautomator runtest installApk2.jar --nohup -c com.uitest.testdemo.installApk2#testEmail")
        print("install %s successes." %p)
        time.sleep(8)

    def uninstall_app(self, pkgname):
        '''删除APK'''
        os.popen("adb wait-for-device")
        os.popen("adb uninstall %s" %pkgname)
        print("remove %s successes." %pkgname)
        time.sleep(2)


    def dumpsys_notification(self, contain_text):
        '''获取通知信息'''
        results = os.popen("adb shell dumpsys notification | grep tickerText")
        for line in results.readlines():                          #依次读取每行
            line = line.strip()                             #去掉每行头尾空白
            print(line)
            if not len(line):       #判断是否是空行或注释行
                continue
            if contain_text in line:
                print('true')
                return True

        print('False')
        return False

# 方便其他类调用
BaseAdb = BaseAdb()    


if __name__ == '__main__':
    print(BaseAdb.add_pressmission())