# -*- coding: UTF-8 ...
import re
import time

import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import telegram
import schedule

def get_time():
    # 格式化成2016-03-20 11:45:39形式
    real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print (real_time)
    return real_time


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
    f = open(r'C:\Users\Administrator\Desktop\card_money.txt', 'r+')  # 从cookie。txt文件中读取原cookie
    money = f.read()
    f.close()

    url= 'https://compus.xiaofubao.com/compus/user/getCardMoney'

    headers={
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/32.363636) ZJYXYwebviewbroswer ZJYXYAndroid tourCustomer /yunmaapp.NET/2.1.2/0c5bf2652e3c331c',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'compus.xiaofubao.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Length': '149',

    }

    key = {
        'id':'1906280823241710',
        'schoolCode':'19335',
        'token':'b4d44185afbb47bc9d3038c406bb9331',
        'deviceId':'0c5bf2652e3c331c',
        'testAccount':'1',
        'appVersion':'170',
        'platform':'YUNMA_APP',
    }

    respons = requests.post(url=url,headers=headers,data=key)

    t = get_time()

    # print(respons)
    # print(respons.text)
    if respons.status_code == 200:
        if str(respons.text).find('操作成功') != -1:
            data = eval(respons.text.replace('true','11'))
            print(f'卡余额为:  {data["data"]}')
            if float(data["data"]) != float(money):

                f = open(r'C:\Users\Administrator\Desktop\card_money.txt', 'r+')  # 从cookie。txt文件中读取原cookie
                f.write(str(data['data']))
                f.close()

                if  float(data["data"]) < float(money):
                    new_money = float(money)-float(data["data"])
                    print(f'{t} 消费了{float("%.2f" % new_money)}')
                    if new_money < 10:
                        return f'{t}  消费了{float("%.2f" % new_money)}  当前卡余额为:  {data["data"]} 少于10元，请充值'
                    else:
                        return f'{t}  消费了{float("%.2f" % new_money)}  当前卡余额为:  {data["data"]} '
                else:
                    new_money = float(data["data"])-float(money)
                    print(f'{t}  充值了{float("%.2f" % new_money)}')
                    return f'{t}  充值了{float("%.2f" % new_money)}  当前卡余额为:  {data["data"]}'
            else:
                return '暂无新消费'



        else:
            return '查询失败'
    else:
        return '爬取失败'




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
        'title':'校园卡余额通知',
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

# schedule.every().day.at("17:00").do(main)
# schedule.every().day.at("11:30").do(main)
# schedule.every().day.at("07:30").do(main)
# schedule.every().day.at("16:20").do(main)

if __name__ == '__main__':

    # while True:
        main()
        # schedule.run_pending()
        # time.sleep(30)


