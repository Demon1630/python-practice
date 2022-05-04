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






options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
# options.add_argument('window-size=1600x900') # 指定浏览器分辨率
# options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
# options.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
# options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
# options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

driver = webdriver.Chrome(options=options)#,executable_path='./chromedriver')
# driver = webdriver.Chrome(chrome_options=options)#,executable_path='./chromedriver')






def get_cookie():

    url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421e3e44ed22931665b7f01c7a99c406d3635/sso/login?service=https%3A%2F%2Fwebvpn.nankai.edu.cn%2Flogin%3Fcas_login%3Dtrue'

    driver.get(url)
    time.sleep(3)

    #填入名称和密码
    name = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/ul/li[2]/input')
    name.send_keys('1120210985')
    pw = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/ul/li[3]/input')
    pw.send_keys('Xyh0945')

    #移动滑块
    action = ActionChains(driver)
    source=driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/ul/li[4]/div/div/div")#需要滑动的元素
    action.click_and_hold(source).perform()  #鼠标左键按下不放
    action.move_by_offset(250,0)#需要滑动的坐标
    action.release().perform() #释放鼠标
    time.sleep(2)

    #登入点击
    log_in = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/ul/li[9]')
    html_get = log_in.click()

    time.sleep(10)

    #获取cookie
    c = driver.get_cookies()

    # print(type(c))
    # print(len(c))

    # print(type(c[1]))
    cookie = c[1]['value']
    # print(cookie)

    url2 = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx'

    driver.get(url2)

    time.sleep(5)
    driver.quit()
    return cookie

    # for i in c:
    #     print(i)


def get_time():
    day = datetime.datetime.now() + datetime.timedelta(days=1)#.strftime("%Y-%m-%d %H:%M:%S")
    time1 = str(day)[:10]
    return time1



'''


def get_in(cookie):
    # url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx'
    url='https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx'
    headers = {
        # 'User-Agent':UserAgent().random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'show_vpn=0; refresh=1; wengine_vpn_ticketwebvpn_nankai_edu_cn=b351c4893f40b96c',
        'Cookie': cookie,
        # 'DNT': '1',
        'Host': 'webvpn.nankai.edu.cn',
        'Referer': 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe43d22931665b7f01c7a99c406d361d/12060/list.htm',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    }

    response = requests.get(url=url, headers=headers)

    print(response.status_code)

    print(response.text)


# url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421e3e44ed22931665b7f01c7a99c406d3635/sso/login?service=https%3A%2F%2Fwebvpn.nankai.edu.cn%2Flogin%3Fcas_login%3Dtrue'




def yuyue(cookie):
    url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe43d22931665b7f01c7a99c406d361d/12060/list.htm'

    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection':'keep-alive',
        'Cookie':cookie,
        'Host':'webvpn.nankai.edu.cn',
        'Origin':'https://webvpn.nankai.edu.cn',
        # 'Referer':'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx',
        'Referer':'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe43d22931665b7f01c7a99c406d361d/',
        'sec-ch-ua':'"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':"Windows",
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',

    }


    response = requests.get(url=url,headers=headers)

    print(response.status_code)
    # print(response.text)


'''


def chaxun(cookie):

    time_data = get_time()

    print(time_data)
    zuowei_id=919557  #F4C031

    # url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/ClientWeb/pro/ajax/reserve.aspx?vpn-12-o2-libic.nankai.edu.cn&dialogid=&dev_id=919576&lab_id=&kind_id=&room_id=&type=dev&prop=&test_id=&term=&number=&classkind=&test_name=&start=2021-11-17+09:00&end=2021-11-17+23:00&start_time=0900&end_time=2300&up_file=&memo=&act=set_resv&_=1636860448197'
    url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/ClientWeb/pro/ajax/reserve.aspx?vpn-12-o2-libic.nankai.edu.cn&dialogid=&dev_id=919576&lab_id=&kind_id=&room_id=&type=dev&prop=&test_id=&term=&number=&classkind=&test_name=&start='+time_data+'+09:00&end='+time_data+'+23:00&start_time=0900&end_time=2300&up_file=&memo=&act=set_resv&_=1636860448197'

    headers={

        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Cookie': 'show_vpn=0;refresh=1;wengine_vpn_ticketwebvpn_nankai_edu_cn=f7fa2789652709eb',
        # 'Cookie': 'show_vpn=0;refresh=1;wengine_vpn_ticketwebvpn_nankai_edu_cn=3de91e51494c801f',
        'Cookie': cookie,

        # 'Cookie':cookie,    #c37379f2d6d8ee08',


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
        # 'dev_id': '919557',#F4C013
        # 'dev_id': '919578',#F4C033

        'dev_id': zuowei_id,  # F4C031
        # 'dev_id': '919551',#F4C007

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
        'start': '2021-11-17 09:00',
        'end': '2021-11-17  23:00',
        'start_time': '0900',
        'end_time': '2300',
        'up_file':'',
        'memo':'',
        'act': 'set_resv',
        # '_': '1636823486720',
        '_': '1636860448197',

    }

    response = requests.get(url=url, headers=headers)#,json=key)

    print(response.status_code)
    print(response.text)

    send_wechat('图书馆预约通知',response.text,'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx')


'''
def check_cookie(cookie):

    url = 'https://webvpn.nankai.edu.cn/'

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection': 'keep - alive',
    # 'Cookie': cookie,
    'Host': 'webvpn.nankai.edu.cn',
    'Referer': 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421e3e44ed22931665b7f01c7a99c406d3635/sso/login?service=https://webvpn.nankai.edu.cn/login?cas_login=true',
    'sec-ch-ua': '"Google Chrome";v="95","Chromium";v="95",";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',

    }

    cookie1 = {"Cookie":cookie}

    response = requests.get(url=url,headers=headers,cookies=cookie1)
    print(response.status_code)
    print(response.text)
'''

def main():

    cookie = get_cookie()
    # cookie1 = 'show_vpn=0;refresh=1;wengine_vpn_ticketwebvpn_nankai_edu_cn='+cookie
    # cookie1 = 'show_vpn=0;refresh=1;wengine_vpn_ticketwebvpn_nankai_edu_cn=2303d166cb0d52d3'
    # cookie2 = 'wengine_vpn_ticketwebvpn_nankai_edu_cn=5403e9a94bac2e32; refresh=1'
    # cookie2 = 'wengine_vpn_ticketwebvpn_nankai_edu_cn=cf81b8780adfea61; refresh=1'


    cookie2 = 'wengine_vpn_ticketwebvpn_nankai_edu_cn='+cookie+'; refresh=1'

    print(cookie2)

    time.sleep(5)


    # yuyue(cookie2)

    # time.sleep(5)
    # get_in(cookie2)
    # time.sleep(5)
    # time.sleep(6)
    chaxun(cookie2)


    # check_cookie(cookie2)


    time_data = get_time()

    # print(get_time())

    driver.quit()



main()



