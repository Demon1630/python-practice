# -*- coding: UTF-8 ...
import re
import time

import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import datetime

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()


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






# options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
# options.add_argument('window-size=1600x900') # 指定浏览器分辨率
# options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
# options.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
# options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
# options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

driver = webdriver.Chrome()#,executable_path='./chromedriver')
# driver = webdriver.Chrome(chrome_options=options)#,executable_path='./chromedriver')

driver.get("http://www.python.org")  # 这个时候chromedriver会打开一个Chrome浏览器窗口，显示的是网址所对应的页面
