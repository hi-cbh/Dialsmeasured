

# 计算成功率
class CalcSuccess(object):
    caselist2 = [] # 数量统计
    caselist3 = [] # 错误统计


    def __init__(self, caselist=[], logpath=""):
        self.caselist = caselist
        self.path = logpath


    def _sortData(self):
        # 数据筛选
        for caseName in self.caselist:
            self.caselist2.append((caseName,0))
            self.caselist3.append((caseName,0))

        print(self.caselist2)
        print(self.caselist3)

        with open(self.path, 'r') as fn:
            txt = fn.readlines()

        # print(txt)
        self.caselist2 = dict(self.caselist2)
        self.caselist3 = dict(self.caselist3)

        for line in txt:
            if "case" not in line:
                continue

            for case in self.caselist:
                if case in line:
                    self.caselist2[case] = self.caselist2[case] + 1
                if case in line and "Fail" in line:
                    self.caselist3[case] = self.caselist3[case] + 1

        print(self.caselist2)
        print(self.caselist3)


    def getSuccessercentage(self):
        # 成功率
        self._sortData()

        for case1, value1 in self.caselist2.items():
            for case2, value2 in self.caselist3.items():
                if case1 == case2:
                    if self.caselist3[case1] == 0:
                        self.caselist2[case1] = "100%"
                    else:
                        self.caselist2[case1] = str((round(1-value2/value1, 2))*100)+"%"


        print(self.caselist2)
        result = []

        for k, v in self.caselist2.items():
            result.append("case: %s, 成功率: %s \n" %(k, v))

        return result




if __name__ == "__main__":
    caselist = ["用例1","用例2","用例3","用例4"]
    path1 = "/var/appiumRunLog/logs/20171121.log"
    CalcSuccess(caselist, path1).getSuccessercentage()


