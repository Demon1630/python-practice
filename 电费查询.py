# -*- coding: UTF-8 ...
import re
import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import telegram



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
    return respons.status_code






def get_info():

    # url = 'https://application.xiaofubao.com/app/electric/queryRoomSurplus HTTP/1.1'
    url = 'https://application.xiaofubao.com/app/electric/queryRoomSurplus'

    headers = {
        'Host': 'application.xiaofubao.com',
        'Connection': 'keep-alive',
        'Content-Length': '123',
        'deviceId':'',
        'User-Agent':'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/32.363636) ZJYXYwebviewbroswer ZJYXYAndroid tourCustomer /yunmaapp.NET/2.1.2/0c5bf2652e3c331c',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
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
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': 'shiroJID=ca49d8ca-ba77-405a-9723-8c35ba78de7f',  #cookie 隔段时间会变化失效
        'Cookie': 'shiroJID=7cd3aaa3-9b6b-4d7d-83e9-ff0a92ae361a',  #cookie 隔段时间会变化失效   尝试前面先登入然后设置cookie来看看行不行
    }

    key ={
        'areaId':'1903011714264042',
        'buildingCode' : '001001001',
        'floorCode' : '001001001004',
        'roomCode' : '001001001004005',
        'areaCode' :'',
        'platform' : 'YUNMA_APP',
    }

    respons = requests.post(url=url,headers=headers,data=key)

    # print(respons)
    print(respons.status_code)
    print(respons.text)
    # print(type(respons.text))
    if respons.status_code == 200:
        if respons.text.find('操作成功'):
            info = respons.text.replace('true','11')
            datas = eval(info)
            data = datas['data']
            print('采集成功，通知已发送')
            return f'{data["displayRoomName"]}电费余额为：{data["surplus"]}'

        else:
            return '查询错误'
    else:
        return '访问错误'


def send_telegram(text):
    chat_id = '1203976293'
    token = '1806211680:AAF_lT_1fh18LzHRLMYcWsZFima8efqU83o'
    bot = telegram.Bot(token=token)

    bot.send_message(chat_id=chat_id, text=text)


def send_wechat(text):
    # url = 'https://sc.ftqq.com/SCU93555Tc0608f46612b3f58458bc7236a6b17285e91f9c6173ab.send'
    url = 'https://sctapi.ftqq.com/SCT43501TagBvqSsCzQ5zc1ZyBbthfB8L.send'
    headers = {
            'User-Agent':UserAgent().random
    }
    key = {
        'title':'电费通知',
        'desp':text,
    }
    response = requests.post(url=url,headers=headers,data=key)
    # print(response)



def main():

    try:
        get_in()
        a = get_info()
        # print(type(a))
        send_wechat(a)
        send_telegram(a)

    except:
        send_wechat('出错了')
        send_telegram('出错了')


if __name__ == '__main__':
    main()
