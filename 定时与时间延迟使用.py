import  time

import schedule
# import time

def get_time():
    # 格式化成2016-03-20 11:45:39形式
    real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print (real_time)
    return real_time

def main():
    while True:
        t = get_time()
        # print(t)

        hour = t[-8:]
        print(hour)
        time.sleep(10)
        # if

# main()



# 定义你要周期运行的函数
def job():
    print(f"I'm working...{get_time()}")

# schedule.every(10).minutes.do(job)               # 每隔 10 分钟运行一次 job 函数
# schedule.every().hour.do(job)                    # 每隔 1 小时运行一次 job 函数
schedule.every().day.at("16:15").do(job)         # 每天在 10:30 时间点运行 job 函数
# schedule.every().monday.do(job)                  # 每周一 运行一次 job 函数
# schedule.every().wednesday.at("13:15").do(job)   # 每周三 13：15 时间点运行 job 函数
# schedule.every().minute.at(":17").do(job)        # 每分钟的 17 秒时间点运行 job 函数

while True:
    schedule.run_pending()   # 运行所有可以运行的任务
    time.sleep(20)


