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

    print(response.status_code)
    print(response.text)

qiandao()

