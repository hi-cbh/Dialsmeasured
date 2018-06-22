# urs/bin/python
# encoding:utf-8

import os
import configparser as cparser
from src.readwriteconf.initData import InitData

class ReadWriteConfFile:
    file_path = InitData().get_sys_path()['rwconf']
    print(file_path)

    @staticmethod
    def get_config_parser():
        cf=cparser.ConfigParser()
        cf.read(ReadWriteConfFile.file_path)
        return cf

    @staticmethod
    def write_config_parser(cf):
        f=open(ReadWriteConfFile.file_path,"w")
        cf.write(f)
        f.close()

    @staticmethod
    def get_section_value(section, key):
        cf=ReadWriteConfFile.get_config_parser()
        return cf.get(section, key)

    @staticmethod
    def add_section(section):
        cf=ReadWriteConfFile.get_config_parser()
        all_sections=cf.sections()
        if section in all_sections:
            return
        else:
            cf.add_section(section)
            ReadWriteConfFile.write_config_parser(cf)

    @staticmethod
    def set_section_value(section, key, value):
        cf=ReadWriteConfFile.get_config_parser()
        cf.set(section, key, value)
        ReadWriteConfFile.write_config_parser(cf)

    @staticmethod
    def read_section_all(section):
        '''读取配置中所有数据'''
        cf=ReadWriteConfFile.get_config_parser()
        all_sections=cf.items(section)
        for k,v in all_sections:
            print("key: %s, value: %s" %(k, v))
        return all_sections

    @staticmethod
    def read_section_zero(section):
        '''读取配置中所有数据，并设置为0'''
        cf=ReadWriteConfFile.get_config_parser()
        all_sections=cf.items(section)
        for k,v in all_sections:
            ReadWriteConfFile.set_section_value(section,k,"0")


    @staticmethod
    def value_add_one(section,case_name):
        '''用例只加1'''
        try:
            value = ReadWriteConfFile.get_section_value(section, case_name)
            ReadWriteConfFile.set_section_value(section, case_name, str(int(value)+1))
        except BaseException as e:
            print(e)
            print("值出错")

    @staticmethod
    def value_set_zero(section,case_name):
        '''用例只为0'''
        try:
            value = ReadWriteConfFile.get_section_value(section, case_name)
            if int(value) != 0:
                ReadWriteConfFile.set_section_value(section, case_name, "0")
        except BaseException:
            print("值出错")





if __name__ == '__main__':
    ReadWriteConfFile.read_section_zero('reportconf')
    ReadWriteConfFile.set_section_value('sendconf', 'error', '0')
    x=ReadWriteConfFile.get_section_value('reportconf', 'testcase01')
    print(x)