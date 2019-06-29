# -*- coding : utf-8 -*-
# @Time      :2019/4/14 1:12
# @Author    : py15期   lemon_huihui
# @File      : __init__.py.py
import datetime
import time

print(datetime.datetime.now())
t1 = datetime.datetime.now()
time.sleep(1)
t2 = datetime.datetime.now()
print(t2-t1)


t1 = time.time()
time.sleep(1)
t2 = time.time()
print(t2-t1)
