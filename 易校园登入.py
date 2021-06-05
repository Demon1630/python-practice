# -*- coding: UTF-8 ...
import re
import time

import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import telegram
import schedule


# def get_in():
#     url = 'https://application.xiaofubao.com/app/invite/jssdk'
#
#     headers = {
#         'Host': 'application.xiaofubao.com',
#         'Connection': 'keep-alive',
#         'Content-Length': '65',
#         'deviceId':'',
#         'User-Agent':'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/32.363636) ZJYXYwebviewbroswer ZJYXYAndroid tourCustomer /yunmaapp.NET/2.1.2/0c5bf2652e3c331c',
#         'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
#         'OSVersion':'',
#         'timestamp':'',
#         'userId':'',
#         'signature':'',
#         'appId':'',
#         'token':'',
#         'Accept': '*/*',
#         'Origin': 'https://application.xiaofubao.com',
#         'X-Requested-With': 'cn.com.yunma.school.app',
#         'Sec-Fetch-Site': 'same-origin',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Dest': 'empty',
#         'Referer': 'https://application.xiaofubao.com/',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#         'Cookie': 'shiroJID=7cd3aaa3-9b6b-4d7d-83e9-ff0a92ae361a',
#
#         'Set-Cookie': 'shiroJID=7cd3aaa3-9b6b-4d7d-83e9-ff0a92ae361a',
#         'Path' : '/',
#         'HttpOnly':'',
#         'SameSite' : 'lax',
#
#     }
#
#     key = {
#         'url':'https%3A%2F%2Fapplication.xiaofubao.com%2F',
#         'platform':'YUNMA_APP',
#     }
#
#     respons = requests.post(url=url,headers=headers,data=key)
#
#     print(respons)
#     print(respons.text)


def get_in():
    url = 'https://compus.xiaofubao.com/login/doLoginBySilent'

    headers = {
        'Accept':'application/json',
        'User-Agent':'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/32.363636) ZJYXYwebviewbroswer ZJYXYAndroid tourCustomer /yunmaapp.NET/2.1.2/0c5bf2652e3c331c',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'compus.xiaofubao.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Length': '297',

        'Set-Cookie': 'shiroJID=7cd3aaa3-9b6b-4d7d-83e9-ff0a92ae361a',
        'Path' : '/',
        'HttpOnly':'',
        'SameSite' : 'lax',

    }

    key = {
        'clientId' : '3a2c98574679a76d4fbb1c3cd4bc4f73',
        'osType' : 'Android',
        'osVersion' : '10',
        'mobileType' : 'MI+8',
        'oaid' : '0c5bf2652e3c331c',
        'appAllVersion' : '2.1.2',
        'appWgtVersion' : '2.1.3',
        'id' : '1906280823241710',
        'schoolCode' : '19335',
        'token' : 'b4d44185afbb47bc9d3038c406bb9331',
        'deviceId' : '0c5bf2652e3c331c',
        'testAccount' : '1',
        'appVersion' : '170',
        'platform' : 'YUNMA_APP',
    }
    respons = requests.post(url=url,headers=headers,data=key)

    print(respons)
    print(respons.text)


get_in()
