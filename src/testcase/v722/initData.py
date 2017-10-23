# urs/bin/python
# encoding:utf-8

import os
import configparser as cparser


base_dir = str(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
file_path = base_dir + "/user_db.ini"

cf = cparser.ConfigParser()
cf.read(file_path)

username = cf.get("userconf", "user1")
pwd = cf.get("userconf", "pwd1")
username2 = cf.get("userconf", "user2")
pwd2 = cf.get("userconf", "pwd2")
filename = cf.get("userconf", "filename")

user2 = {"name": username, 'pwd': pwd}
user1 = {"name": username2, 'pwd': pwd2}


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
    print("---group_a的所有键为：%s"  %conf.options("userconf"))
    print("---group_b的所有键为：%s"  %conf.options("mysqlconf"))

    # 获取指定section的所有键值对
    print("---group_a的所有键-值为：%s" %conf.items("userconf"))

    # 指定section，option读取具体值
    print("---group_a组的a_key1值为：%s" %conf.get("userconf", "user1"))
#
# def writeConfigFile():
#     """
#     根据分组名、键名修改为新键值
#     @param sections: section分组名
#     @param key: 分组中的key
#     @param newvalue: 需要修改后的键值
#     """
#     conf.set("group_b", "b_key3", "new3")   #指定section和option则更新value
#     conf.set("group_b", "b_key5", "value5") #指定section，则增加option和value
#
#     conf.add_section("group_d")             #添加section组
#     conf.set("group_d", "d_key1", "value1") #给添加的section组增加option-value
#     #写回配置文件
#     conf.write(open(iniFileUrl, "wb"))






if __name__ == "__main__":
    readConfigFile()
