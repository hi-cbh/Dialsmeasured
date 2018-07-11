# urs/bin/python
# encoding:utf-8

import os,sys,time



p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("RunAll path: %s" %p)
sys.path.append(p+"/")
from src.readwriteconf.rwconf import ReadWriteConfFile
from testUnittest.testcasedemo.testdemo1 import MyTest1
from testUnittest.testcasedemo.testdemo2 import MyTest2
from testUnittest.testcasedemo.testdemo3 import MyTest3

class RunAll(object):

    def run_case(self):


        print('=================重跑用例=================')
        ReadWriteConfFile.value_set_true_false(False)


        MyTest1().testCase01()
        MyTest2().testCase01()
        MyTest3().testCase01()



        print("运行结束")
        time.sleep(5)
        print('=================运行结束=================')

RunAll=RunAll()


if __name__ == "__main__":
    RunAll.run_case()