# urs/bin/python
# encoding:utf-8

import os
import configparser as cparser
from src.readwriteconf.initData import InitData

class ReadWriteConfFile:
    # base_dir = str((os.path.dirname(os.path.dirname(__file__))))
    # 固定路径
    # file_path ="/var/appiumRunLog/ini/user_db.ini"
    file_path = InitData().getsysPath()['rwconf']
    # file_path = base_dir + "/user_db.ini"
    print(file_path)

    @staticmethod
    def getConfigParser():
        cf=cparser.ConfigParser()
        cf.read(ReadWriteConfFile.file_path)
        return cf

    @staticmethod
    def writeConfigParser(cf):
        f=open(ReadWriteConfFile.file_path,"w")
        cf.write(f)
        f.close()

    @staticmethod
    def getSectionValue(section,key):
        cf=ReadWriteConfFile.getConfigParser()
        return cf.get(section, key)

    @staticmethod
    def addSection(section):
        cf=ReadWriteConfFile.getConfigParser()
        allSections=cf.sections()
        if section in allSections:
            return
        else:
            cf.add_section(section)
            ReadWriteConfFile.writeConfigParser(cf)

    @staticmethod
    def setSectionValue(section,key,value):
        cf=ReadWriteConfFile.getConfigParser()
        cf.set(section, key, value)
        ReadWriteConfFile.writeConfigParser(cf)


if __name__ == '__main__':
    ReadWriteConfFile.addSection( 'sendconf')
    ReadWriteConfFile.setSectionValue( 'sendconf','error','0')
    x=ReadWriteConfFile.getSectionValue( 'sendconf','error')
    print(x)