
path = "/Users/apple/autoTest/workspace/DialsMeasured/logs/2_20171120.log"

txt = []

with open(path, 'r') as fn:
    txt = fn.readlines()

txt2 = []
for line in txt:
    key = line.split(":")[0]
    value = line.split(":")[1][:-1]
    print(key, value)
    txt2.append((key, value))

txt2 = dict(txt2)

print(txt2)

def has_key(ss):
    if ss in txt2:
        print("true")
    else:
        print("false")


has_key("用例1")
with open(path, 'w') as fn:
    fn.write("")
