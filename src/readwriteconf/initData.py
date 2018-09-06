# urs/bin/python
# encoding:utf-8

import os
import configparser as cparser

import datetime

# 读取项目内的配置文件，非/var目录下的文件
file_path = str(os.path.dirname(os.path.dirname(__file__))) + "/user_db.ini"
print(file_path)
cf = cparser.ConfigParser()
cf.read(file_path)

class InitData():

    def get_users(self):
        return dict(cf.items("users"))

    def get_sql(self):
        return dict(cf.items("mysqlconf"))


    def get_file(self):
        # print(cf.items("userconf"))
        return dict(cf.items("userconf"))


    def get_sys_path(self):
        return dict(cf.items("sysconf"))

class duser(object):
    '''单例模式，只获取一次用户名字典'''
    __species = None
    __first_init = True

    def __new__(cls, *args, **kwargs):
        if cls.__species == None:
            cls.__species = object.__new__(cls)
        return cls.__species

    def __init__(self):
        if self.__first_init:
            print("赋值......")
            self.users = self.__getusers()
            self.__class__.__first_init = False
            # 相当于Animal.__first_init = False

    def __getusers(self):
        '''获取值'''
        print("__getusers.........")
        d = InitData().get_users()

        # # 调试账号
        # username = "13533218540"
        # pwd = "hy12345678"


        # 主账号
        # 在早上6-7点，使用性能号码
        if datetime.datetime.now().hour in [6,7]:
            username = d['user1']
            pwd = d['pwd1']
        elif datetime.datetime.now().hour%2 == 0:
            username = d['user3']
            pwd = d['pwd3']
        else:
            username = d['user4']
            pwd = d['pwd4']

        username2 = d['user2']
        pwd2 = d['pwd2']

        users = {"name": username, 'pwd': pwd,"name2":username2,"pwd2":pwd2}
        print(users)
        print(type(users))
        return users


    def getuser(self):
        return self.users



if __name__ == "__main__":
    print(InitData().get_file())
