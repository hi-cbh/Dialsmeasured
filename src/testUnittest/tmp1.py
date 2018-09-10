# urs/bin/python
# encoding:utf-8
import time
'''
装饰器，脚本中，添加装饰器，减少代码的调用

'''

def auth_func(func):
    def wrapper(*args, **kwargs):
        username = input("name: ").strip()
        passpwd = input("pwd: ").strip()
        if username == "sb" and passpwd == '123':
            res = func(*args, **kwargs)
            return res
        else:
            print("name or pwd error!")
    return wrapper

@auth_func
def index():
    print("主页")

@auth_func
def home(name):
    print("Home页面 %s" %name)

@auth_func
def shopping_car(name):
    print("%s 购物车： mac" %name)
    pass


# index()

def timer(func):
    '''嵌套包
    1、这里没有调用嵌套的函数
    2、返回wrapper 才开始调用函数
    3、func必须返回值，否则调用的原函数，无法返回正确函数
    '''

    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("value %s" %(end - start))
        return res

    return wrapper

@timer
def test_time(name):
    print("start......")
    time.sleep(2)
    print("test: %s" %name)
    print("end......")
    return "test"


res=test_time("ktv")
print("demo_mothod %s" %res)



