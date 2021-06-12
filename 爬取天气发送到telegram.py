# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import telegram


def get_time():
    # 格式化成2016-03-20 11:45:39形式
    real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print (real_time)
    return real_time

def get_weather():

    url1 = 'http://d3.weather.com.cn/webgis_rain_new/webgis/minute?lat=30.333264&lon=120.166367&callback=fc5m&_=1621743825997'
    url2 = 'http://forecast.weather.com.cn/town/api/v1/sk?lat=30.334511&lng=120.162918&callback=getDataSK&_=1621744557971'


    headers1 = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Cookie': 'f_city=%E6%9D%AD%E5%B7%9E%7C101210101%7C; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1621743444,1621743523; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1621743523',
    'DNT': '1',
    'Host': 'd3.weather.com.cn',
    'Referer': 'http://www.weather.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    }
    headers2 = {
    'Accept': '* / *',
    'Accept - Encoding': 'gzip, deflate',
    'Accept - Language': 'zh - CN, zh;q = 0.9, zh - TW;q = 0.8, en;q = 0.7',
    'Connection': 'keep - alive',
    'Cookie': 'f_city=%E6%9D%AD%E5%B7%9E%7C101210101%7C; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1621743444,1621743523,1621744161; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1621744161',
    'DNT': '1',
    'Host': 'forecast.weather.com.cn',
    'Referer': 'http: // www.weather.com.cn/',
    'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',

    }

    string1 = {
    'lat': '30.33102',
    'lon': '120.163062',
    'callback': 'fc5m',
    '_': '1621744175001',
    }
    string2 = {
    'lat': '30.334511',
    'lng': '120.162918',
    'callback': 'getDataSK',
    '_': '1621744557971',
    }

    respons1 = requests.get(url=url1,headers=headers1,data=string1)
    respons2 = requests.get(url=url2,headers=headers2,data=string2)

    # print(respons2.text)
    # print(respons1.text)

    text = '杭州拱墅区天气\n'


    info = re.search('getDataSK\((.*?)\)',respons2.text)
    dic =  eval(info.group(1))
    WD = '风速：'+dic.get('WD') + ' ' + dic.get('WS')
    text = text+WD+'\n'

    temp = '温度：'+ dic.get('temp') +'℃'
    text = text+temp+'\n'

    weather = dic.get('weather')
    text = text+weather+'\n'

    hd = '湿度：' + dic.get('humidity')
    text = text+hd+'\n'

    # print(WD)
    # print()

    message = re.search('msg":"(.*?)","times',respons1.text)
    # print(message.group(1))
    text = text+message.group(1)+'\n'


    return text

def send_weather(text):
    chat_id = '@Python1633'
    token = '1779618476:AAHfqFU_KumuNdywCle3y-ZJCXa56SulYY8'
    bot = telegram.Bot(token=token)

    bot.send_message(chat_id=chat_id, text=text)

def main():
    while True:
        try:
            times = get_time()
            text = get_weather()

            text  = text+times
            send_weather(text)
            print(f'天气已发送 {times}')
        except:
            send_weather('爬取天气出现问题')
        time.sleep(600)
if __name__ == '__main__':
    main()

