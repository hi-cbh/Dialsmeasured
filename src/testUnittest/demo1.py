import re

s = "case：用例3 , 时延：1.0, result：Success"


a = []
a.append(("case1",[0,1]))
a.append(("case2",[0,1]))

a = dict(a)

print(a)
print(a["case1"][0])
print(a["case2"][1])

for k, v in a.items():
    print(k)
    print(v[0])