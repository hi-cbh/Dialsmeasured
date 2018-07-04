from sql.sql import DB
from src.base.baseTime import BaseTime
from readwriteconf.rwconf import ReadWriteConfFile





l = ['testcaseonbtnlogin', 'testcaselogin', 'testcasesendnoattach', 'testcasesendattach', 'testcasefwdsend', 'testcaseforward', 'testcasereply', 'testdownfile', 'testcasecheckaddresslist', 'testcaseselected', 'testcasepush', 'testcasecalendar', 'testcasediscover', 'testcasepersionmessages', 'testcaseskydrive']
tc = ReadWriteConfFile.read_section_all("caseconf")
# print(type(tc))
tc = dict(tc)

new_dict = {}
for k,v in tc.items():
    if k in l:
        new_dict[k] = v

new_dict["times"] = BaseTime.get_current_time()
print(new_dict)
print(new_dict)
try:
    db = DB()
    db.update("test_data",new_dict)
    db.close()
except Exception as e:
    print("数据库连接失败")
    print(e)