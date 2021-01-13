import os
import datetime
import threading
import time



'''

loop对内存的占用率，
1. 进来之后判断hour时间
   时间符合，开启
   时间符合，已经开启，就不再执行开启动作
2  时间符合关闭，则调用关闭
3  以此循环

day_set  达到24 个 后，要清空数组
'''
cmd_start = './start_mining.sh'
cmd_stop = './stop_mining.sh'


day_set = []
clear_day_set = 0   # 24小时为0
hour = 0
while True:
    time.sleep(0.5)   # 防止内存被占满
    print('loop____ing.')
    print('loop____ing..')
    print('loop____ing...')
    print('loop____ing....', hour)
    # hour = datetime.datetime.now().hour # int (0 - 24)


    # 这里是指， 如果开启的时刻已经存在day_set里面，那么就不用再去开启
    if hour not in day_set or day_set[-1] is not 0:
        day_set.append(hour)
        if hour == 20:
            # start_t = threading.Thread(target=start_mine)
            # start_t.setDaemon(True)
            # start_t.start()
            os.system("./start_mining.sh")
        elif hour == 8:
            os.system("./stop_mining.sh")
    # bug : day_set = [0, 1, 2, 3]
    # 只要都有0， 都会被清空
    elif clear_day_set in day_set:
        # [0, 1, 2, 3, 4, 5......23, 0]
        # 这里的区别就是第一个0和最后一个0的区别，第一个0代表进入凌晨， 最后一个0代表已经是过了一天。
        if day_set[-1] is 0 and len(day_set) > 1:
            print('day_set..........', day_set)
            day_set = [0]
            # 达到一天的时间了，就清0

    # hour += 1
    if hour == 23:
        hour = 0
    else:
        hour += 1