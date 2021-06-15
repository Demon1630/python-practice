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
from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用
import openpyxl
import random

def get_ip(url,new_ip):
    '''
    从免费代理IP网站获取代理IP
    '''

    # url = 'http://www.xiladaili.com/gaoni/'

    headers= {
        # 'User-Agent': UserAgent().random
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'DNT': '1',
        'Host': 'www.xiladaili.com',
        # 'Referer':'http://www.xiladaili.com/gaoni/7/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',

    }

    proxy = {'http': new_ip, 'https': new_ip}

    respons = requests.get(url=url,headers=headers,proxies= proxy)

    # print(respons.status_code)
    # print(respons.text)

    bs =BeautifulSoup(respons.content,'html.parser')
    info = bs.find('tbody')
    # print(info)
    data = info.find_all('tr')
    # print(data)

    ip_list=[]   #将获取到的IP用列表存储
    for i in data:
        dic = {}
        ip_port = i.find_all('td')[0].string          #拆分IP和端口
        tpy = i.find_all('td')[1].string              #拆分类型 http或https
        time_yanchi = i.find_all('td')[4].string      #响应时间
        core = i.find_all('td')[7].string             #打分


        # if tpy != 'HTTP代理':           #把https存起来，因为使用中主要还是使用https
        dic['ip_port']=ip_port
        dic['tpy']=tpy
        dic['time_yanchi']=time_yanchi
        dic['core']=core

        ip_list.append(dic)    #用字典形式存入列表中

        # print(f'ip和端口：{ip_port},类型：{tpy},响应时间：{time_yanchi},分数：{core}')
    # print(ip_list)
    return ip_list   #将获取到的IP列表返回


# get_ip('http://www.xiladaili.com/gaoni/6/','')

def check_ip(ip_list):
    '''
    检测IP是否有效，但在pycharm中一直返回的是本身IP，而在vps中运行时则会正常。。。不知道怎么回事
    '''
    # 访问网址
    # url = 'http://www.whatismyip.com.tw/'
    url = 'http://icanhazip.com'  # 用来检测IP是否可以正常使用
    # url = 'http://httpbin.org/ip'

    # 这是代理IP
    ip_useful_list = []
    for dic_ip in ip_list:
        ip = dic_ip['ip_port']
        # 设置代理ip访问方式，http和https
        proxy = {'http': ip, 'https': ip}
        # 创建ProxyHandler
        try:
            response = requests.get(url=url, proxies=proxy, timeout=2)

            # print(response.status_code)
            # print(response.text)
            print(f'{dic_ip}有效')
            ip_useful_list.append(dic_ip)  # 有效则把IP添加到列表中
        except:
            print(f'{dic_ip}无效')
            # continue
    return ip_useful_list


def write_excel(list):
    """将传入的数据写入"""
    #先读取，再写入
    book = openpyxl.load_workbook('C:\\Users\\Administrator\\Desktop\\代理IP.xlsx')
    ws = book.active  # 获取当前正在操作的表对象

    #把ip提取出来,判断是否存在

    strs = []
    for key_word in ws['A']:
        strs.append(key_word.value)

    j = ws.max_row  #获取行数，添加到后面去，就不会把前面的覆盖掉
    for ip_info in list:
        ip_port = ip_info['ip_port']
        if ip_port not in strs:
            print(f'{ip_info}  不存在,存入')
            # text = list[0] + '  ' + list[1] + '  ' + list[2] + '\n'
            # send_telegram(text)    #关键词之前不存在,则推送并添加进去
            # ws.append(ip_info)   #不能直接写进去，要先读取字典

            j += 1
            # for item in ip_info.items():
            # j +=1
            ws['A'+str(j)].value=ip_info['ip_port']
            ws['B'+str(j)].value=ip_info['tpy']
            ws['C'+str(j)].value=ip_info['time_yanchi']
            ws['D'+str(j)].value=ip_info['core']


            book.save("C:\\Users\\Administrator\\Desktop\\代理IP.xlsx")
            # print(f'{ip_port}写入成功')



def get_excel():
    '''
    从excle文件中随机读取一个ip，然后判断是否有效，并输出
    :return:
    '''

    book = openpyxl.load_workbook('C:\\Users\\Administrator\\Desktop\\代理IP.xlsx')
    ws = book.active  # 获取当前正在操作的表对象

    k = ws.max_row
    while True:
        i = random.randint(2,k)
        ip_port = ws['A'+str(i)].value
        # print(ip_port)

        url = 'http://icanhazip.com'  # 用来检测IP是否可以正常使用
        proxy = {'http':ip_port, 'https':ip_port}
        try:
            response = requests.get(url=url, proxies=proxy, timeout=2)

            # print(f'{ip_port}有效')
            return ip_port
        except:
            # print(f'{ip_port}无效')
            ws.delete_rows(i)  # 无效则删除第i行，后面数据补充上去
            book.save("C:\\Users\\Administrator\\Desktop\\代理IP.xlsx")



def main():

    new_ip = get_excel()
    i = 1
    j = 1
    while i <=25:
    # for i in range(1,25):   #把前四页的爬取出来

        print(new_ip)
        try:

            url = 'http://www.xiladaili.com/gaoni/'+str(i)+'/'
            ip_list = get_ip(url,new_ip)
            print(ip_list)
            ip_useful_list = check_ip(ip_list)
            print(ip_useful_list)
            if len(ip_list) == 0:

                new_ip = get_excel()
                print(f'第{i}页ip爬取出错{j}次，更换IP:{new_ip}重新爬取')
                if j >8:
                    print(f'出错8次，跳过第{i}页')
                    i+=1
                    j=0

                j += 1

                time.sleep(5)


            else:
                print(ip_useful_list)
                write_excel(ip_useful_list)

                print(f'第{i}页ip爬取写入成功')
                i += 1
                j = 1


        except:
            new_ip = get_excel()
            print(f'第{i}页ip爬取出错{j}次，更换IP:{new_ip}重新爬取')
            if j >8:
                print(f'出错8次，跳过第{i}页')
                i+=1
                j=0
            j+=1
            time.sleep(5)

    #从exel中获取一个有效ip并返回
    ip_useful = get_excel()
    print(ip_useful)


main()
