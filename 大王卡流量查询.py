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
    token = '1889538918:AAEAXxBMr8MpBzDU_403b09vR-6ryJKkda0'
    bot = telegram.Bot(token=token)

    bot.send_message(chat_id=chat_id, text=text)


def send_wechat(text):
    # url = 'https://sc.ftqq.com/SCU93555Tc0608f46612b3f58458bc7236a6b17285e91f9c6173ab.send'
    url = 'https://sctapi.ftqq.com/SCT43501TagBvqSsCzQ5zc1ZyBbthfB8L.send'
    headers = {
            'User-Agent':UserAgent().random
    }
    key = {
        'title':'大王卡流量查询',
        'desp':text,
    }
    response = requests.post(url=url,headers=headers,data=key)
    # print(response)




def get_info():
    url = 'https://kapi.10010.com/KCard/personalCenterNew/balance/base'

    headers = {
        'Host': 'kapi.10010.com',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cache-Control': 'max-age=0',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://txwk.10010.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://txwk.10010.com/KCard/mPages/balanceQuery.html?openid=oMwiav8GZN5sSBD4Y4DoNB_mKmsw',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
        'Cookie': 'KSESSIONID=MmYzNGIwODAtNzA4ZS00ZjRkLWI4MjktZDg5OTk4NjczMjU4; acw_tc=73eec92116230438944933112e10c2e84fcf3f64b9913929622ea8ed73',

    }

    response = requests.post(url=url,headers=headers)
    print(response.status_code)
    # print(response.text)
    info = eval(str(response.text).replace('false','000').replace('true','111').replace('null','222'))['data']
    print(type(info))

    # for key,value in info.items():
    #     print(f'{key} = {value}')


    fee = info['fee']
    specificPkg = info['flow']['specificPkg']
    flexy = info['flow']['flexy']

    text = f'账单：\n  本月已用 {fee["used"]}元  \n  剩余话费：{fee["left"]}元  ' \
           f'\n定向流量使用情况：\n  总共：{specificPkg["total"]} MB \n  已用:{specificPkg["used"]} MB  \n  剩余：{specificPkg["left"]} MB  ' \
           f'\n通用流量使用情况：\n  总共：{flexy["total"]} MB \n  已用:{flexy["used"]} MB  \n  剩余：{flexy["left"]} MB'
    # print(text)
    return text

def main():

    t = get_time()
    text = t + '\n'+get_info()
    print(f'{t}  \n{text}')
    send_telegram(text)
    send_wechat(text)

# get_info()
main()