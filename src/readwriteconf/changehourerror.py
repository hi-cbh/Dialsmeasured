
import  datetime
from src.readwriteconf.rwconf import  ReadWriteConfFile
from src.sql.docker_mysql import DockerDB


class HourError(object):


    def setData(self,new_dict):

        save_hour = ReadWriteConfFile.get_section_value("hourconf","currenthour")
        current_hour = str(datetime.datetime.now().hour)

        if current_hour.__eq__("0"):
            current_hour = "24"

        if save_hour.__eq__(current_hour):

            # 把数值写入sql
            DockerDB().update_hour("sign_hourerror",new_dict,current_hour)
        else:
            # 使用新的时间
            ReadWriteConfFile.set_section_value("hourconf","currenthour",current_hour)
            # 写入sql
            DockerDB().update_hour("sign_hourerror",new_dict,current_hour)

            # 清除以后数值
            ReadWriteConfFile.read_section_zero("errorhourconf")


    #把数据库所有数据复位
    #在哪个时间段，需要复位？
    def set_zero(self):
        try:

            l = ['testcaseonbtnlogin', 'testcaselogin', 'testcasesendnoattach', 'testcasesendattach', 'testcasefwdsend', 'testcaseforward', 'testcasereply', 'testdownfile', 'testcasecheckaddresslist', 'testcaseselected', 'testcasepush', 'testcasecalendar', 'testcasediscover', 'testcasepersionmessages', 'testcaseskydrive']
            tc = ReadWriteConfFile.read_section_all("errorhourconf")
            # print(type(tc))
            tc = dict(tc)

            new_dict = {}
            for k,v in tc.items():
                if k in l:
                    new_dict[k] = 0

            # print(new_dict)

            DockerDB().set_zero("sign_hourerror",new_dict)
        except BaseException as e:
            # print(e)
            print('修改数据库失败')


if __name__ == "__main__":

    HourError().setData("")