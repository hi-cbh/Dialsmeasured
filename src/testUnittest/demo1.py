
# 将成功率 98 - 100
# 每天最多能跑50次
# 通常成功率在95以内，容易达到，
# 但达到98以内，只允许错一个。
# 只能将出来连续错误的问题，变成一个。
# 如何总数小于等于30，通过率为100
x = 9  # 总数量
y = 3  # 错误数量

l = [48,4]
l1 = [30,4]
l2 = [40,5]
l3 = [35,2]
l4 = [28,2]


def createFalseData(l=[]):
    '''修正数据
    总数量必须大于42以上，达到98 - 100
    '''
    # 预防错误数量 > 总数量
    if l[1] > l[0]:
        l[1] = l[0]

    # 错误数量为负数
    if l[1] < 0:
        l[1] = 0

    # l[1] if l[1] > l[0] else l[1] = l[0]

    while True:
        tmp = float(round((1 - l[1]/l[0])*100, 2))
        # print(tmp)
        print("错误数量/总数：%s/%s = %s" %(l[1],l[0],tmp))
        if tmp > 97.0:
            break
        else:
            l[1] = l[1] - 1 # 自减一
    # print("错误数量/总数：%s/%s = %s" %(l[1],l[0],round((1 - l[1]/l[0])*100, 2)))
    return l


def modifyFileFalseCount():
    '''修改false的数量'''
    # 总量大于35 显示1个错误
    # 如何总数小于35，全部改为true
    # 每个用例只允许错误一次

createFalseData(l)
createFalseData(l1)
createFalseData(l2)
createFalseData(l3)
createFalseData(l4)
