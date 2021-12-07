# -*- coding: UTF-8 ...nbm';
import re
import time

import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import telegram
# import schedule


def qiandao():
    url = 'https://note.youdao.com/yws/mapi/user?method=checkin'
    # url = 'https://note.youdao.com/yws/mapi/payment?method=status&pversion=v2&pt=true&ClientVer=61000010000&GUID=PC20dee46d9e6d55ba3&client_ver=61000010000&device_id=PC20dee46d9e6d55ba3&device_name=DEMON&device_type=PC&keyfrom=pc&os=Windows&os_ver=Windows%2010&vendor=website&vendornew=website'

    headers = {
        'Accept': '*/*',
        'User-Agent': 'YNote',
        'Host': 'note.youdao.com',
        'Content-Length': '0',
        'Connection': 'Keep-Alive',
        'Cache-Control': 'no-cache',
        'Cookie': 'YNOTE_FORCE=true; YNOTE_SESS=v2|4ig7Z3Yu-mQF0f6Fn4lfRqSOMYlhLez0Yl6LOGhLqFReyn4QZO4lGROEnfQBkflGRpShf6FnMqS0J4OLOGRfOm06ZhfpuO4PBR; YNOTE_LOGIN=1||1638797500570; JSESSIONID=aaa__wVr7gYHEcVqhlb2x',
    }

    response = requests.post(url=url,headers=headers)

    # print(response.status_code)
    # print(response.text)
    # print(type(eval(response.text)['success']))
    i = eval(response.text)['success']
    if i == 0:
        print(f'今日已经签到过了，本次签到获取到{i}Mb')
        send_telegram(f'今日已经签到过了，本次签到获取到{i}Mb')
    else:
        print(f'签到成功，本次签到获取到{i}Mb')
        send_telegram(f'签到成功，本次签到获取到{i}Mb')


def send_telegram(text):
    chat_id = '1203976293'
    token = '5065693849:AAGTkzWOZPKCsAOnyiZox0-qkm8GbaCSx6I'
    bot = telegram.Bot(token=token)
    try:
        bot.send_message(chat_id=chat_id, text=text)
        print('telegram信息发送成功')
    except:
        print('信息发送失败')

def main():
    try:
        qiandao()
    except:
        print('程序错误')
        send_telegram('程序错误')

if __name__ == '__main__':
    main()






