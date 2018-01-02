
caselist = {"case1":[12,3],"case2":[24,3],"case3":[24,3]}

l = []
for casetimes, value in caselist.items():
    l.append(value[0])
    print(casetimes)

print("-----")
print(max(l))
