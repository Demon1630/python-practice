# -*- coding: UTF-8 ...
import re
import time

import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import telegram
import schedule




def get_cookie():


    f = open(r'C:\Users\Administrator\Desktop\cookie.txt', 'r+')  # 从cookie。txt文件中读取原cookie
    # old_cookie='shiroJID=44c8aa33-bf1d-4478-b224-74e84c52b16a'
    # old_cookie='shiroJID=ed0b475d-52f3-4af9-a2f5-35dc54dcf9a9'
    old_cookie = f.read()
    # print(old_cookie)
    f.close()



    # url = 'https://application.xiaofubao.com/app/invite/jssdk'
    url = 'https://application.xiaofubao.com/app/login/getUser4Authorize'



    headers = {
        'Host': 'application.xiaofubao.com',
        'Connection': 'keep-alive',
        'Content-Length': '76',
        'deviceId':'',
        # 'User-Agent':'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/32.363636) ZJYXYwebviewbroswer ZJYXYAndroid tourCustomer /yunmaapp.NET/2.1.2/0c5bf2652e3c331c',
        'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
        'OSVersion':'',
        'timestamp':'',
        'userId':'',
        'signature':'',
        'appId':'',
        'token':'',
        'Accept': '*/*',
        'Origin': 'https://application.xiaofubao.com',
        'X-Requested-With': 'cn.com.yunma.school.app',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://application.xiaofubao.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': old_cookie,  #cookie 没过期时不会返回新cookie

    }

    key = {
        # 'url':'https%3A%2F%2Fapplication.xiaofubao.com%2F',
        # 'platform':'YUNMA_APP',
        'code' : 'a2309ba493fdf938ec0617f28571496b',
        'userId' : '1906280823241710',
        'schoolCode' : '19335',
        'platform' : 'YUNMA_APP',
    }

    respons = requests.post(url=url,headers=headers,data=key)

    # print(respons)
    # print(respons.text)
    # print(respons.headers)
    # print(old_cookie)
    if str(respons.headers).find('Set-Cookie') != -1:
        new_header = eval(str(respons.headers))
        # for key,value in new_header.items():
        #     print(f'{key}={value}')
        new_Cookie = new_header['Set-Cookie'].split(';',2)
        print(new_Cookie[0])

        f = open(r'C:\Users\Administrator\Desktop\cookie.txt', 'r+')   # 将获取到的新cookie存入cookie.txt文件
        f.write(str(new_Cookie[0]))
        f.close()

        return new_Cookie[0]
    else:
        # print(old_cookie)
        return old_cookie

    # print(type(eval(str(respons.headers))))



new_cookie = get_cookie()

print(new_cookie)
