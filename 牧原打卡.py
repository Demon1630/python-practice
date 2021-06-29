# -*- coding: UTF-8 ...
import re
import time

import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import telegram
# import schedule

def get_time():
    # 格式化成2016-03-20 11:45:39形式
    real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print (real_time)
    return real_time




# print(date)


def get_info():
    url = 'https://jsrz.imuyuan.com/api/recruitment/myMPPControl/insertMyMPPControl'


    # date = get_time()[:10].replace('-', '')

    headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Content-Length':'209',
        'Content-Type':'application/json',
        'DNT':'1',
        'Host':'jsrz.imuyuan.com',
        'Origin':'https://jsrz.imuyuan.com',
        'Pragma':'no-cache',
        'Referer':'https://jsrz.imuyuan.com/xiaozhao/pages/yqfk.html?prod=innership',
        'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile':'?0',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',

    }

    key = {
        "isCrossCity": "0",
        "isFever": "0",
        "name": "13163292090",
        "nowAddress": "江西省宜春市万载县康乐街道建材辅料批发",
        "remark": "",
        "symptom": "",
        "tel": "13163292090",
        "temperature": "36",
        "userId": "809186",
    }

    response =requests.post(url=url,headers=headers,json=key)
    # print(response.status_code)
    # print(response.headers)
    # print(response.text)
    if response.status_code == 200:
        print(response.text)
        return str(response.text)
    elif response.status_code == 400:
        print(response.text)
        return str(response.text)
    else:
        return '打卡出错了'


def send_telegram(text):
    chat_id = '1203976293'
    token = '1756504990:AAHyJcj1GZSDWYnrrm3a0i22dXU76q7_mtE'
    bot = telegram.Bot(token=token)


    bot.send_message(chat_id=chat_id, text=text)


def send_wechat(title,text,detal_url):

    get_acs_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww428187fbdb9fd50f&corpsecret=po3lAng2YdZzaa67teFhmOxL34EuuWpffdiZlQeGaNk'

    access = requests.get(url=get_acs_token_url)
    access_token = eval(access.text)['access_token']
    # print(type(eval(access_token.text)))
    # print(access_token)


    url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
    # print(url)

    headers = {
        'User-Agent': UserAgent().random
    }

    key = {
        "touser": "@all",
        # "toparty": "PartyID1|PartyID2",
        # "totag": "TagID1 | TagID2",
        "msgtype": "textcard",
        "agentid": 1000002,
        # "text": '测试',
        "textcard": {
            "title": title,
            "description": text,#"<div class=\"gray\">2016年9月26日</div> <div class=\"normal\">恭喜你抽中iPhone 7一台，领奖码：xxxx</div><div class=\"highlight\">请于2016年10月10日前联系行政同事领取</div>",
            "url": detal_url,
            "btntxt": "更多"
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }

    res = requests.post(url=url,headers=headers,json=key)
    # print(res.status_code)
    # print(res.text)

# send_wechat('测试','你好啊','URL')



def main():
    try:
        info = get_info()
        # print(info)
        send_wechat('牧原每日打卡通知',info,'URL')
        send_telegram(info)

    except:
        send_wechat('牧原每日打卡通知','错误','URL')
        send_telegram('错误')

if __name__ == '__main__':
    main()

