from src.readwriteconf.rwconf import  ReadWriteConfFile
import  datetime
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





if __name__ == "__main__":

    HourError().setData("")