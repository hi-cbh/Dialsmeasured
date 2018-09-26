# urs/bin/python
# encoding:utf-8
import time
'''
装饰器，脚本中，添加装饰器，减少代码的调用

'''

user_list = [
    {"name":"ciewe", "pwd":"123"},
    {"name":"hello", "pwd":"123"},
    {"name":"sb", "pwd":"123"},
    {"name":"nb", "pwd":"123"},
]

current_dic={"name": None, "login":False}


def auth(auth_type="filedb"):
    def auth_func(func):
        def wrapper(*args, **kwargs):
            print(auth_type)
            # 判断是否为None
            if current_dic["name"] and current_dic["login"]:
                res = func(*args, **kwargs)
                return res

            username = input("name: ").strip()
            passpwd = input("pwd: ").strip()
            # 如果账户密码正确，修改dict

            for index, user_dic in enumerate(user_list):
                print("find: %s" %user_dic["name"])
                if username == user_dic["name"] and passpwd == user_dic["pwd"]:
                    current_dic["name"] = username
                    current_dic["login"] = True

                    res = func(*args, **kwargs)
                    return res
            else:
                print("name or pwd error!")

        return wrapper
    return auth_func

@auth(auth_type="db")
def index():
    print("主页")

@auth
def home(name):
    print("Home页面 %s" %name)


index()
home("ktv")

# def timer(func):
#     '''嵌套包
#     1、这里没有调用嵌套的函数
#     2、返回wrapper 才开始调用函数
#     3、func必须返回值，否则调用的原函数，无法返回正确函数
#     '''
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print("value %s" %(end - start))
#         return res
#
#     return wrapper
#
# @timer # test_time = timer(test_time)
# def test_time(name):
#     print("start......")
#     time.sleep(2)
#     print("test: %s" %name)
#     print("end......")
#     return "test"
#
#
# res=test_time("ktv")
# print("demo_mothod %s" %res)



