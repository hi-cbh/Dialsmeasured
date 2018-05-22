import datetime

from readwriteconf.initData import InitData

d = InitData().get_users()
import random
if random.randint(1, 10)%2 == 0:
    username = d['user3']
    pwd = d['pwd3']
else:
    username = d['user4']
    pwd = d['pwd4']


for i in range(10):

    print((datetime.datetime.now().hour)%2)