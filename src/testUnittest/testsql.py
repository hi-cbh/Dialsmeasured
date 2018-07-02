from readwriteconf.rwconf import ReadWriteConfFile





l = ['testcaseonbtnlogin', 'testcaselogin', 'testcasesendnoattach', 'testcasesendattach', 'testcasefwdsend', 'testcaseforward', 'testcasereply', 'testdownfile', 'testcasecheckaddresslist', 'testcaseselected', 'testcasepush', 'testcasecalendar', 'testcasediscover', 'testcasepersionmessages', 'testcaseskydrive']
tc = ReadWriteConfFile.read_section_all("caseconf")
# print(type(tc))
tc = dict(tc)

new_dict = {}
for k,v in tc.items():
    if k in l:
        new_dict[k] = v

print(new_dict)