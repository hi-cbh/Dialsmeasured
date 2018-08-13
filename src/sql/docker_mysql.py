# urs/bin/python
# encoding:utf-8
import pymysql.cursors
import os
import configparser as cparser

from src.readwriteconf.rwconf import ReadWriteConfFile
from src.readwriteconf.initData import InitData

_path = InitData().get_sys_path()["rwconf"]

cf = cparser.ConfigParser()
print(_path)
cf.read(_path)
host = cf.get("alyconf", "host")
port = cf.get("alyconf", "port")
db   = cf.get("alyconf", "db_name")
user = cf.get("alyconf", "user")
password = cf.get("alyconf", "password")



class DockerDB:

    def __init__(self):
        print("数据更新到阿里云，测试........")
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 修改
    def update(self,table_name, table_data):
        try:

            key   = "=%r,".join(table_data.keys())
            key = key + "=%r"
            # print(tuple(table_data.values()))
            real_sql = "UPDATE " + table_name + " SET " + key %tuple(table_data.values())
            print(real_sql)

            with self.connection.cursor() as cursor:
                cursor.execute(real_sql)

            self.connection.commit()
        except BaseException as e:
            print("数据修改失败")
            print(e)

        finally:
            self.close()

    # 修改
    def update_hour(self, table_name, table_data, hour):
        try:
            key   = "=%r,".join(table_data.keys())
            key = key + "=%r"
            # print(tuple(table_data.values()))
            real_sql = "UPDATE " + table_name + " SET " + key %tuple(table_data.values()) + " WHERE hour = %d ;"  %int(hour)
            print(real_sql)

            with self.connection.cursor() as cursor:
                cursor.execute(real_sql)

            self.connection.commit()
        except BaseException as e:
            print("本地数据库连接失败")
            print(e)
        finally:
            self.close()





    # close database
    def close(self):
        print("数据更新到阿里云，结束........")
        try:
            self.connection.close()
        except BaseException:
            print('无连接')



    def show_data(self,table_name):
        sql = "SELECT * FROM %s" %table_name
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        print(results)
        return results


    def set_zero(self, table_name, table_data):
        try:
            key   = "=%r,".join(table_data.keys())
            key = key + "=%r"
            # print(tuple(table_data.values()))
            real_sql = "UPDATE " + table_name + " SET " + key %tuple(table_data.values()) + " WHERE times like '2018%' ;"
            # print(real_sql)

            with self.connection.cursor() as cursor:
                cursor.execute(real_sql)

            self.connection.commit()
        except BaseException as e:
            print("本地数据库连接失败")
            print(e)
        finally:
            self.close()

if __name__ == '__main__':


    l = ['testcaseonbtnlogin', 'testcaselogin', 'testcasesendnoattach', 'testcasesendattach', 'testcasefwdsend', 'testcaseforward', 'testcasereply', 'testdownfile', 'testcasecheckaddresslist', 'testcaseselected', 'testcasepush', 'testcasecalendar', 'testcasediscover', 'testcasepersionmessages', 'testcaseskydrive']
    tc = ReadWriteConfFile.read_section_all("errorhourconf")
    # print(type(tc))
    tc = dict(tc)

    new_dict = {}
    for k,v in tc.items():
        if k in l:
            new_dict[k] = 0

    print(new_dict)

    # DockerDB().update("sign_case", new_dict)
    # DockerDB().update("sign_error", new_dict)
    DockerDB().set_zero("sign_hourerror",new_dict)



