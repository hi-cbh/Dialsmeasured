# urs/bin/python
# encoding:utf-8

import os
import time
import subprocess
import traceback
import tempfile

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class BaseAdb(object):
    
    def __init__(self):
        # print('BaseAdb init')
        # self.path = "/Users/apple/autoTest/android-sdk-macosx/platform-tools/"
        self.path=""
    
    def adbStop(self, cmd):
        '''杀进程'''
        self.adbShell(self.path+'adb shell am force-stop %s' %cmd)

    def adbIntallUiautmator(self):
        '''调用以及导入的jar包，运行uiautmator辅助工具'''
        self.adbShell(self.path+"adb shell uiautomator runtest installApk.jar --nohup -c com.uitest.testdemo.installApk")

    def adbIntallUiautmator37(self):
        '''调用以及导入的jar包，运行uiautmator辅助工具'''
        self.adbShell(self.path+"adb shell uiautomator runtest installApkVivo.jar --nohup -c com.uitest.testdemo.installApkVivo")


    def adbWakeUp(self):
        '''手机进行唤醒并解锁'''
        self.adbShell(self.path+"adb shell uiautomator runtest powerOffAndOn.jar --nohup -c com.uitest.testdemo.powerOffAndOn")

    def adbSleep(self):
        '''手机进行休眠状态'''
        self.adbShell(self.path+"adb shell uiautomator runtest powerSleep.jar --nohup -c com.uitest.testdemo.powerSleep")

    def adbTap(self, x,y):
        '''通过坐标，点击屏幕'''
        self.adbShell(self.path+"adb shell input tap %s %s " %(str(x), str(y)))    
    
    def adbBack(self):
        '''通过命令行，点击返回'''
        self.adbShell(self.path+'adb shell input keyevent 4')
        time.sleep(2)
    
    def adbInputText(self,txt):
        '''通过命令行，输入字段'''
        self.adbShell(self.path+'adb shell input text %s' %txt)
    
    def adbHome(self):
        '''通过命令行，点击返回'''
        self.adbShell(self.path+'adb shell input keyevent 3')
        time.sleep(1)
    
    def adbentry(self):
        '''通过命令行，发送接邮件的广播'''
        self.adbShell(self.path+'adb shell am broadcast -a mybroadcast')
    
    def adbStartApp(self, pag, activity):
        '''通过命令行，启动应用'''
        self.adbShell(self.path+'adb shell am start -n %s/%s' %(pag, activity))
    

            
    def adbGetWifi_on(self):
        '''获取当前的wifi状态，开启返回True'''
        value = os.popen(self.path+"adb shell settings get global wifi_on","r")
#         print(value.readline())
        if not '0' in value.readline() :
            return True
        else:
            return False

    def getNetworkType(self):
        '''读取手机网络'''
        if(self.adbGetWifi_on() != True):
            print("4G")
            return '4G'
        else:
            print("CMCC")
            return 'CMCC'   
    
    
    def adbGetApkVersion(self, pkg):
        '''获取apk版本'''
        command_result=""
        results = os.popen(self.path+"adb shell dumpsys package %s | findstr versionName" %pkg)
#         results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()

        command_result = command_result.split('=')[1]
        
        print(command_result)
        return command_result
        
    
            
    def adbShell(self, cmd):
        try:
            os.popen(cmd)
            # self.testsubprocess(cmd)
        except BaseException:
            print('命令调用出错')
            pass
    
    def adbClear(self, pkgname):
        '''清除缓存'''
        os.popen(self.path+"adb shell pm clear %s"  %pkgname)
    
    def adbBroadcast(self):
        '''发送自定义广播'''
        os.popen(self.path+"adb shell am broadcast -a mybroadcast")
    
    
#===================以下是GT基本操作==========

    def adbStartGT(self):
        '''启动GT'''
        results = os.popen("adb shell am start -W -n com.tencent.wstt.gt/com.tencent.wstt.gt.activity.GTMainActivity")

        for line in results.readlines():                          #依次读取每行  
            line = line.strip()                             #去掉每行头尾空白  
            if not len(line):       #判断是否是空行或注释行  
                continue
            if 'ok' in line:
#                 print('true')
                return True
        else:
#             print('False')
            return False
    
    def adbGTAddPkg(self, pkgName):
        '''使gt可以采集该应用的性能信息；pkgName是包名；verName是版本号（可选参数）'''
        results = os.popen("adb shell am broadcast -a com.tencent.wstt.gt.baseCommand.startTest --es pkgName %s" %pkgName)
        for line in results.readlines():                          #依次读取每行  
            line = line.strip()                             #去掉每行头尾空白  
            if not len(line):       #判断是否是空行或注释行  
                continue
            if 'completed' in line:
#                 print('true')
                return True
        else:
#             print('False')
            return False

    def adbGTbaseCommand(self, name, value):
        '''记录性能项'''
        results = os.popen("adb shell am broadcast -a com.tencent.wstt.gt.baseCommand.sampleData --ei %s %s" %(name,value))
        for line in results.readlines():                          #依次读取每行  
            line = line.strip()                             #去掉每行头尾空白  
            if not len(line):       #判断是否是空行或注释行  
                continue
            if 'completed' in line:
#                 print('true')
                return True
        else:
#             print('False')
            return False     

    def adbGTSave(self, path, filename):
        '''保存数据'''
        results = os.popen("adb shell am broadcast -a com.tencent.wstt.gt.baseCommand.endTest --es saveFolderName %s  --es desc %s" %(path, filename))
        for line in results.readlines():                          #依次读取每行  
            line = line.strip()                             #去掉每行头尾空白  
            if not len(line):       #判断是否是空行或注释行  
                continue
            if 'completed' in line:
#                 print('true')
                return True
        else:
#             print('False')
            return False  

    def adbGTExit(self):
        '''离开GT'''
        results = os.popen("adb shell am broadcast -a com.tencent.wstt.gt.baseCommand.exitGT")
        for line in results.readlines():                          #依次读取每行  
            line = line.strip()                             #去掉每行头尾空白  
            if not len(line):       #判断是否是空行或注释行  
                continue
            if 'completed' in line:
#                 print('true')
                return True
        else:
#             print('False')
            return False 

    # 拉数据到本地
    def adbPull(self, remote, local):
        print("adb pull %s %s"  %(remote, local))
        result=os.popen("adb pull %s %s"  %(remote, local))
        print(result.readline())

    def testsubprocess(self, cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                             stderr=subprocess.PIPE) #, close_fds=True)

        # log.debug('running:%s' % cmd)
        out, err = p.communicate()
        # log.debg(out)
        if p.returncode != 0:
            print("Non zero exit code:%s executing: %s" % (p.returncode, cmd))
            # log.critical("Non zero exit code:%s executing: %s" % (p.returncode, cmd))
        return p.stdout

    def adbApkExist(self, pkg):
        '''第三方包是否安装'''
        results = os.popen("adb shell pm list package -3")
        for line in results.readlines():                          #依次读取每行
            line = line.strip()                             #去掉每行头尾空白
            if not len(line):       #判断是否是空行或注释行
                continue
            if pkg in line:
                # print('true')
                return True
        else:
            # print('False')
            return False



    def installApp(self, p):
        '''安装APK'''
        os.popen("adb wait-for-device")
        os.popen("adb install %s" %p)
        time.sleep(5)
        os.popen("adb shell uiautomator runtest installApk2.jar --nohup -c com.uitest.testdemo.installApk2#testEmail")
        print("install %s successes." %p)
        time.sleep(8)

    def uninstallAPP(self, pkgname):
        '''删除APK'''
        os.popen("adb wait-for-device")
        os.popen("adb uninstall %s" %pkgname)
        print("remove %s successes." %pkgname)
        time.sleep(2)


    def dumpsysNotification(self, containText):
        '''获取通知信息'''
        results = os.popen("adb shell dumpsys notification | grep tickerText")
        for line in results.readlines():                          #依次读取每行
            line = line.strip()                             #去掉每行头尾空白
            print(line)
            if not len(line):       #判断是否是空行或注释行
                continue
            if containText in line:
                print('true')
                return True
        else:
            print('False')
            return False

# 方便其他类调用
BaseAdb = BaseAdb()    


if __name__ == '__main__':
    BaseAdb.dumpsysNotification(u"同步网络联系人完成")