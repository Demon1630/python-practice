import datetime
def get_time():
    day = datetime.datetime.now() + datetime.timedelta(days=1)#.strftime("%Y-%m-%d %H:%M:%S")
    time1 = str(day)[:10]
    return time1

time1 = get_time()
print(time1)

