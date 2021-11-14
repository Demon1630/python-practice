# -*- coding: UTF-8 ...
import re
import time

import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os





def get_in():
    url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx'

    headers = {
        # 'User-Agent':UserAgent().random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': 'show_vpn=0; refresh=1; wengine_vpn_ticketwebvpn_nankai_edu_cn=b351c4893f40b96c',
        'DNT': '1',
        'Host': 'webvpn.nankai.edu.cn',
        'Referer': 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe43d22931665b7f01c7a99c406d361d/12060/list.htm',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    }

    response = requests.get(url=url, headers=headers)

    print(response.status_code)

    print(response.text)


# url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421e3e44ed22931665b7f01c7a99c406d3635/sso/login?service=https%3A%2F%2Fwebvpn.nankai.edu.cn%2Flogin%3Fcas_login%3Dtrue'



def yuyue():
    url = 'https://webvpn.nankai.edu.cn/wengine-vpn/input'

    headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Connection':'keep-alive',
        'Content-Length':'44',
        'Content-Type':'text/plain;charset=UTF-8',
        'Cookie':'show_vpn=0;refresh=1;wengine_vpn_ticketwebvpn_nankai_edu_cn=b351c4893f40b96c',
        'DNT':'1',
        'Host':'webvpn.nankai.edu.cn',
        'Origin':'https://webvpn.nankai.edu.cn',
        'Referer':'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx',
        'sec-ch-ua':'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':"Windows",
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',

    }

    key = {
        # 'name': "",
        # 'type': "button",
        # 'value': "提交",

        'name': "start_time",
        'type': "select-one",
        'value': "1100",


    }

    response = requests.post(url=url,headers=headers,json=key)

    print(response.status_code)
    print(response.text)




def chaxun():
    url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/ClientWeb/pro/ajax/reserve.aspx?vpn-12-o2-libic.nankai.edu.cn&dialogid=&dev_id=919544&lab_id=&kind_id=&room_id=&type=dev&prop=&test_id=&term=&number=&classkind=&test_name=&start=2021-11-14+10:20&end=2021-11-14+12:00&start_time=1020&end_time=1200&up_file=&memo=&act=set_resv&_=1636823486720'

    headers={

        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': 'show_vpn=0;refresh=1;wengine_vpn_ticketwebvpn_nankai_edu_cn=b351c4893f40b96c',
        'DNT': '1',
        'Host': 'webvpn.nankai.edu.cn',
        'Referer': 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx',
        'sec-ch-ua': '"Chromium";v="94","Google Chrome";v="94",";Not A Brand";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    key = {

        'vpn-12-o2-libic.nankai.edu.cn':'',
        'dialogid':'',
        'dev_id': '919544',
        'lab_id':'',
        'kind_id':'',
        'room_id':'',
        'type': 'dev',
        'prop':'',
        'test_id':'',
        'term':'',
        'number':'',
        'classkind':'',
        'test_name':'',
        'start': '2021-11-15 10:20',
        'end': '2021-11-15  12:00',
        'start_time': '1020',
        'end_time': '1200',
        'up_file':'',
        'memo':'',
        'act': 'set_resv',
        '_': '1636823486720',

    }

    response = requests.get(url=url,headers=headers,json=key)

    print(response.status_code)
    print(response.text)

def main():
    # get_in()
    # yuyue()
    chaxun()

main()



