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



def check_ip(ip_list):
    #访问网址
    # url = 'http://www.whatismyip.com.tw/'
    url = 'http://icanhazip.com'
    # url = 'http://httpbin.org/ip'
    #这是代理IP
    # ip = '125.177.124.73:80'

    ip_useful_list = []

    for ip in ip_list:
        # ip = '103.103.3.6:8080'
        # ip = '131.161.68.37:31264'
        #设置代理ip访问方式，http和https
        proxy = {'http':ip,'https':ip}
        # proxy = {'http':'http://103.103.3.6:8080','https':'https://103.103.3.6:8080'}
        #创建ProxyHandler
        try:
            response = requests.get(url=url,proxies=proxy,timeout=2)

            print(response.status_code)
            print(response.text)
            print(f'{ip}有效')
            ip_useful_list.append(ip)


        except:
            print(f'{ip}无效')

    return ip_useful_list

def get_ip():

    url = 'http://www.xiladaili.com/gaoni/'

    headers= {
        'User-Agent': UserAgent().random
    }

    respons = requests.get(url=url,headers=headers)

    bs =BeautifulSoup(respons.content,'html.parser')
    info = bs.find('tbody')
    data = info.find_all('tr')
    # print(data)
    ip_list=[]
    for i in data:
        # print(str(i))
        # detal = str(i)
        ip_port = i.find_all('td')[0].string
        tpy = i.find_all('td')[1].string
        time_yanchi = i.find_all('td')[4].string
        core = i.find_all('td')[7].string

        if tpy != 'HTTP代理':
            ip_list.append(ip_port)

        print(f'ip和端口：{ip_port},类型：{tpy},响应时间：{time_yanchi},分数：{core}')

        # for j in i.find_all('td'):
        #     print(j)
        # print(type(detal))

    # print(type(data))
    # print(ip_list)



    # print(respons.status_code)
    # print(respons.text)

    return ip_list

def main():
    ip_list = get_ip()

    ip_useful_list = check_ip(ip_list)

    print(ip_useful_list)

main()
