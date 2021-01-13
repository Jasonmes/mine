import os
import datetime
import threading


# 这个用于验证Python对Linux下的操作


cmd = 'ps -a'
# print(os.system(cmd))
data = os.popen(cmd)
print(data.read())
data = data.read()
print(type(data))