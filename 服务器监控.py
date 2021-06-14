# -*- coding: UTF-8 ...
import re
import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import telegram
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

def get_time():
    # 格式化成2016-03-20 11:45:39形式
    real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print (real_time)
    return real_time

def send_telegram(text):
    chat_id = '1203976293'
    token = '1870256785:AAGGYEIaDf9UBs6TBe91ZmxqNRqfMKnZXN4'
    bot = telegram.Bot(token=token)

    bot.send_message(chat_id=chat_id, text=text)


def send_wechat(text):
    # url = 'https://sc.ftqq.com/SCU93555Tc0608f46612b3f58458bc7236a6b17285e91f9c6173ab.send'
    url = 'https://sctapi.ftqq.com/SCT43501TagBvqSsCzQ5zc1ZyBbthfB8L.send'
    headers = {
            'User-Agent':UserAgent().random
    }
    key = {
        'title':'主机监控',
        'desp':text,
    }
    response = requests.post(url=url,headers=headers,data=key)
    # print(response)




def get_info():
    # url = 'https://www.demon1630.ga/'
    url = 'https://www.demon1630.ga/json/stats.json'

    headers = {
        'User-Agent':UserAgent().random
    }

    respons = requests.get(url=url,headers=headers)

    print(respons.status_code)
    # print(respons.text)

    data = eval('['+ re.search('"servers": \[\n(.*?)\],',respons.text,re.S).group(1).replace('true','111').replace('false','000') + ']')   #转换成列表
    # print(type(eval(data)))


    # print(data)
    # print(len(data))
    text = get_time() +'\n'
    for i in data:
        # print(i)
        info = eval(str(i))   #获得内容字典
        # print(type(info))
        if info['online4'] == 111:
            status = '在线'
        else:
            status = '不在线'
        memory =  float(info["memory_used"])/float(info["memory_total"])*100
        hdd = float(info["hdd_used"])/float(info["hdd_total"])*100

        text = text+f'主机: {info["name"]}  {status}, 在线时长：{info["uptime"]}  CPU：{info["cpu"]}%  内存：{int(memory)}%  硬盘：{int(hdd)}%' + '\n'

        if hdd >80:
            warm1 = f'警告 {info["name"]} 硬盘使用过高，超过80%'
            send_wechat(warm1)
            send_telegram(warm1)
            # print(warm1)
        if memory >85:
            warm2 = f'警告 {info["name"]} 内存使用过高，超过85%'
            send_wechat(warm2)
            send_telegram(warm2)
            # print(warm2)


        # print(f'主机: {info["name"]}  {status}, 在线时长：{info["uptime"]}  CPU：{info["cpu"]}%  内存：{int(memory)}%  硬盘：{int(hdd)}%')

    # print(text)
    return text

def main():
    try:
        info = get_info()
        send_telegram(info)
        send_wechat(info)
    except:
        send_wechat('查询出错')
        send_telegram('查询出错')

if __name__ == '__main__':
    main()


