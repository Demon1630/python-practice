import time



def get_time():
    # 格式化成2016-03-20 11:45:39形式
    real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:10]
    # print (real_time)
    return real_time

ti = get_time()
print(type(ti))
print(ti)
