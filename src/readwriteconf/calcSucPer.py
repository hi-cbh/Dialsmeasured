

# 计算成功率
class CalcSuccess(object):
    suclist = [] # 成功率统计
    speedlist = [] # 速度统计


    def __init__(self, caselist=[], logpath=""):
        self.caselist = caselist
        self.path = logpath


    def _sortData(self):
        # 数据筛选，成功率
        for caseName in self.caselist:
            self.suclist.append((caseName, [0, 0]))# 第一个为总数，第二个为错误次数
            # self.caselist3.append((caseName,0))

        # print(self.suclist)
        # print(self.caselist3)

        with open(self.path, 'r') as fn:
            txt = fn.readlines()

        # print(txt)
        self.suclist = dict(self.suclist)
        # self.caselist3 = dict(self.caselist3)

        for line in txt:
            if "case" not in line:
                continue

            for case in self.caselist:
                if case in line:
                    self.suclist[case][0] = self.suclist[case][0] + 1
                if case in line and "Fail" in line:
                    self.suclist[case][1] = self.suclist[case][1] + 1

    def _sortSpeed(self):
        # 数据筛选，速度
        for caseName in self.caselist:
            self.speedlist.append((caseName, [0,0])) # 第一个值为速度和，第二个为个数

        print(self.speedlist)

        with open(self.path, 'r') as fn:
            txt = fn.readlines()

        # print(txt)
        self.speedlist = dict(self.speedlist)

        for line in txt:
            if "case" not in line:
                continue

            for case in self.caselist:
                if case in line and "时延" in line:
                    # print("line: %s" %line)
                    sd = line[line.find("时延：")+3:line.find(",",line.find("时延："))]
                    # print("s:%s" %str(sd))
                    # print("type:%s" %type(sd))
                    # print("float:%s" %round(float(sd)))

                    self.speedlist[case][0] = float(self.speedlist[case][0]) + float(sd)
                    self.speedlist[case][1] = self.speedlist[case][1] + 1

        # 计算平均值，赋值第二个值
        for k,v in self.speedlist.items():
            if v[0] == 0:
                continue
            else:
                v[1]=round(float(v[0]/v[1]),2)

        print(self.speedlist)


    def getSuccessercentage(self):
        # 成功率
        self._sortData()
        self._sortSpeed()

        for case, value in self.suclist.items():
            if self.suclist[case][1] == 0:
                self.suclist[case][0] = "100%"
            else:
                self.suclist[case][0] = str(round((1 - value[1]/value[0])*100, 2)) + "%"


        # print(self.suclist)
        result = []

        for k, v in self.suclist.items():
            if k in self.speedlist and self.speedlist[k][0] != 0:
                result.append("case: %s, 成功率: %s , 平均时延: %s \n" %(k, v[0], self.speedlist[k][1]))
            else:
                result.append("case: %s, 成功率: %s \n" %(k, v[0]))
        print(result)
        return result




if __name__ == "__main__":
    caselist = ["用例1","用例2","用例3","用例4"]
    path1 = "/var/appiumRunLog/logs/20171121.log"
    CalcSuccess(caselist, path1).getSuccessercentage()


