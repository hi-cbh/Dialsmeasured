# urs/bin/python
# encoding:utf-8

import os
import configparser as cparser


base_dir = str(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
file_path = base_dir + "/user_db.ini"

cf = cparser.ConfigParser()
cf.read(file_path)

class InitData():

    def getUsers(self):

        return dict(conf.items("users"))

    def getSql(self):
        return dict(conf.item("mysqlconf"))


    def getFile(self):
        print(conf.items("userconf"))
        return dict(conf.items("userconf"))


conf=cparser.ConfigParser() #生成conf对象
conf.read(file_path)   #读取ini配置文件
def readConfigFile():
    """
    sections:配置文件中[]中的值
    options:每组中的键
    items:键-值的列表形式
    """
    # 获取每组类型中的section值
    sections = conf.sections()  # 获取所有sections
    print("---conf.ini文件中的section内容有：%s" %sections)

    # 获取每行数据的键即指定section的所有option
    print("---userconf 的所有键为：%s"  %conf.options("userconf"))
    print("---mysqlconf 的所有键为：%s"  %conf.options("mysqlconf"))

    # 获取指定section的所有键值对
    print("---userconf 的所有键-值为：%s" %conf.items("userconf"))

    # 指定section，option读取具体值
    print("---userconf 组的 user1 值为：%s" %conf.get("userconf", "user1"))


    # for k,v in conf.items("userconf"):
    #     print(k,v)

    print(dict(conf.items("userconf")))

if __name__ == "__main__":
    print(InitData().getFile())
