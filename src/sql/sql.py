# urs/bin/python
# encoding:utf-8
import pymysql.cursors
import os
import configparser as cparser
from src.readwriteconf.rwconf import ReadWriteConfFile

base_dir = str((os.path.dirname(os.path.dirname(__file__))))
file_path = base_dir + "/user_db.ini"

cf = cparser.ConfigParser()
print(file_path)
cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db   = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


class DB:

    def __init__(self):
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

    # clear table data
    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()


    # 修改
    def update(self, table_name, table_data):
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
            print("本地数据库连接失败")
            print(e)
        finally:
            self.close()



    # close database
    def close(self):
        try:
            self.connection.close()
        except BaseException:
            print("数据库连接失败")

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()

    def show_data(self,table_name):
        sql = "SELECT * FROM %s" %table_name
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        print(results)
        return results

if __name__ == '__main__':


    l = ['testcaseonbtnlogin', 'testcaselogin', 'testcasesendnoattach', 'testcasesendattach', 'testcasefwdsend', 'testcaseforward', 'testcasereply', 'testdownfile', 'testcasecheckaddresslist', 'testcaseselected', 'testcasepush', 'testcasecalendar', 'testcasediscover', 'testcasepersionmessages', 'testcaseskydrive']
    tc = ReadWriteConfFile.read_section_all("caseconf")
    # print(type(tc))
    tc = dict(tc)

    new_dict = {}
    for k,v in tc.items():
        if k in l:
            new_dict[k] = int(v)

    print(new_dict)

    DB().update("test_data",new_dict)