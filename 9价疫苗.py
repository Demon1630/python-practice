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
    token = '1886850695:AAG-gfzszOsF_RPJHdYCaI0maxszwd4qoL4'
    bot = telegram.Bot(token=token)

    bot.send_message(chat_id=chat_id, text=text)


def send_wechat(text):
    # url = 'https://sc.ftqq.com/SCU93555Tc0608f46612b3f58458bc7236a6b17285e91f9c6173ab.send'
    url = 'https://sctapi.ftqq.com/SCT43501TagBvqSsCzQ5zc1ZyBbthfB8L.send'
    headers = {
            'User-Agent':UserAgent().random
    }
    key = {
        'title':'hpv疫苗通知',
        'desp':text,
    }
    response = requests.post(url=url,headers=headers,data=key)
    # print(response)



def get_in():

    url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=auth&code=073YxKkl2usAa74gpcnl2ay1sO1YxKkH&key302=2caf893321&expire302=1623027326'

    headers = {
        'Host': 'cloud.cn2030.com',
        'Connection': 'keep - alive',
        'Cookie':'',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'content-type': 'application/json',
        'zftsl': 'd3916c78ae31015310937eead3d83093',
        'Referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/73/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',

    }

    response = requests.get(url=url,headers=headers)

    print(response.status_code)
    # print(response.headers)
    info = eval(str(response.headers))
    print(info)
    set_cookie = info['Set-Cookie'].split(';',2)[0]
    print(set_cookie)
    return set_cookie


# get_in()

def get_info(url,cookie,k):


    # url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=3653&lat=30.27415&lng=120.15515&key302=06da522bf2&expire302=1623028311'
    # url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4846&lat=30.27415&lng=120.15515&key302=2b7b75179a&expire302=1623027327'
    # url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4851&lat=30.27415&lng=120.15515&key302=ae9b132ff0&expire302=1623030780'
    # url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4851&lat=30.27415&lng=120.15515&key302=ae9b132ff0&expire302=1623030780'

    headers = {
        'Host': 'cloud.cn2030.com',
        'Connection': 'keep - alive',
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'content-type': 'application/json',
        'zftsl': 'cf6c3f398e93c4b98f9b43dbe3c2814f',
        'Referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/73/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br',

    }

    response = requests.get(url=url,headers=headers)
    # print(response.status_code)
    # print(response.text)
    info = eval(str(response.text.replace('true','111').replace('false','000')))
    # print(type(info))
    addr = info['cname']+':'+info['addr']

    data = eval(str(info['list']))

    # print(f'地址：{addr}')
    # print(type(data))
    # print(len(data))
    text = f'地址：{addr}' + '\n'
    for d in data:
        i = eval(str(d))
        # print(f'{i["text"]} 价格:{i["price"]}   {i["BtnLable"]}， 预约时间：{i["date"]}')
        if str(i["date"])  != '暂无' :
            send_telegram(f'{i["text"]} 价格:{i["price"]}   {i["BtnLable"]}， 预约时间：{i["date"]}  地址：{addr}，请登录知苗预约小程序准备预约')
            send_wechat(f'{i["text"]} 价格:{i["price"]}   {i["BtnLable"]}， 预约时间：{i["date"]}  地址：{addr}，请登录知苗预约小程序准备预约')
        elif str(i["BtnLable"]) != '暂未开始':
            send_telegram(f'{i["text"]} 价格:{i["price"]}   {i["BtnLable"]}， 预约时间：{i["date"]}  地址：{addr}，请登录知苗预约小程序准备预约')
            send_wechat(f'{i["text"]} 价格:{i["price"]}   {i["BtnLable"]}， 预约时间：{i["date"]}  地址：{addr}，请登录知苗预约小程序准备预约')
        else:
            k += 1

        text = text + f'{i["text"]} 价格:{i["price"]}   {i["BtnLable"]}， 预约时间：{i["date"]}' + '\n'
    # print(text)
    return text,k

        # print(type(eval(str(d))))
        # print(d)


    # print(data[0])
    # print(data[1])


# get_info()

def main():
    cookie = get_in()
    url_list = ['https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4846&lat=30.27415&lng=120.15515&key302=2b7b75179a&expire302=1623027327',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=3653&lat=30.27415&lng=120.15515&key302=06da522bf2&expire302=1623028311',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4851&lat=30.27415&lng=120.15515&key302=ae9b132ff0&expire302=1623030780',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4231&lat=30.27415&lng=120.15515&key302=f49f06d8a7&expire302=1623030939',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4852&lat=30.27415&lng=120.15515&key302=174c49fc14&expire302=1623030980',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=1755&lat=30.27415&lng=120.15515&key302=d6901e7a0c&expire302=1623030991',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=1756&lat=30.27415&lng=120.15515&key302=303fc255fc&expire302=1623031022',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4460&lat=30.27415&lng=120.15515&key302=8660f5f3df&expire302=1623031036',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4220&lat=30.27415&lng=120.15515&key302=3b8d039a00&expire302=1623031046',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4475&lat=30.27415&lng=120.15515&key302=27e8a390b6&expire302=1623031057',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4845&lat=30.27415&lng=120.15515&key302=88639f2395&expire302=1623031062',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4849&lat=30.27415&lng=120.15515&key302=ec6d00df21&expire302=1623031077',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4850&lat=30.27415&lng=120.15515&key302=b525ea43e4&expire302=1623031085',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4848&lat=30.27415&lng=120.15515&key302=eaa22b8a8f&expire302=1623031111',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=5172&lat=30.27415&lng=120.15515&key302=eb7d0f49c4&expire302=1623031118',
                'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4847&lat=30.27415&lng=120.15515&key302=fc508a9b9c&expire302=1623031122',
                ]
    text_all = get_time() + '\n'

    k = 0
    for url in url_list:
        # print(url)
        try:
            text = get_info(url,cookie,k)
            # print(type(text))
            k = int(text[1])
            print(text)
            # print(text[1])
            text = text[0] + '\n' + '*'*20 +'\n'
            text_all = text_all + text
            time.sleep(2)
            # print(text)

        except:
            print('查询出错了')
            # send_wechat(f'{get_time()} hpv疫苗查询出错')
            # send_telegram(f'{get_time()} hpv疫苗查询出错')
            k += 2
    # print(k)


    if k == 32:
        print('暂时都不可预约')
        send_wechat(f'{get_time()} hpv疫苗暂时都不可预约')
        send_telegram(f'{get_time()}  hpv疫苗暂时都不可预约')
    else:
        print('有疫苗可预约')
        send_wechat(f'{get_time()} hpv疫苗有可以预约的了，快去准备预约')
        send_telegram(f'{get_time()}  hpv疫苗有可以预约的了，快去准备预约')


    # print(text_all)
    # send_wechat(text_all)
    # send_telegram(text_all)


main()

