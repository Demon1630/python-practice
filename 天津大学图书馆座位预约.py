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


options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
# options.add_argument('window-size=1600x900') # 指定浏览器分辨率
options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
# options.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
# options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
# options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

driver = webdriver.Chrome(options=options)



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
    # driver.quit()

    print(cookie)
    return cookie


def get_time():
    day = datetime.datetime.now() + datetime.timedelta(days=1)#.strftime("%Y-%m-%d %H:%M:%S")
    time1 = str(day)[:10]
    print(time1)
    return time1



def chaxun(cookie):
    time_data = get_time()

    print(time_data)
    zuowei_id = 919557  # F4C031

    url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/ClientWeb/pro/ajax/reserve.aspx?vpn-12-o2-libic.nankai.edu.cn&dialogid=&dev_id=919576&lab_id=&kind_id=&room_id=&type=dev&prop=&test_id=&term=&number=&classkind=&test_name=&start=' + time_data + '+09:00&end=' + time_data + '+23:00&start_time=0900&end_time=2300&up_file=&memo=&act=set_resv&_=1636860448197'

    headers = {

        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': cookie,

        'DNT': '1',
        'Host': 'webvpn.nankai.edu.cn',
        'Referer': 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx',
        'sec-ch-ua': '"Chromium";v="94","Google Chrome";v="94",";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    key = {

        'vpn-12-o2-libic.nankai.edu.cn': '',
        'dialogid': '',

        'dev_id': zuowei_id,  # F4C031
        'lab_id': '',
        'kind_id': '',
        'room_id': '',
        'type': 'dev',
        'prop': '',
        'test_id': '',
        'term': '',
        'number': '',
        'classkind': '',
        'test_name': '',
        'start': '2021-11-17 09:00',
        'end': '2021-11-17  23:00',
        'start_time': '0900',
        'end_time': '2300',
        'up_file': '',
        'memo': '',
        'act': 'set_resv',
        # '_': '1636823486720',
        '_': '1636860448197',

    }

    response = requests.get(url=url, headers=headers)  # ,json=key)

    print(response.status_code)
    print(response.text)

    # send_wechat('图书馆上午九点半预约通知',response.text,'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx')

def yuyue(cookie):
    time_data = get_time()

    print(time_data)
    zuowei_id = 919557

    url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/ic-web/reserve?vpn-12-o2-libic.nankai.edu.cn'

    headers={
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
            'Connection': 'keep - alive',
            'Content-Length': '213',
            'Content-Type': 'application / json;    charset = UTF - 8',
            'Cookie': cookie,
            'DNT': '1',
            'Host': 'webvpn.nankai.edu.cn',
            'lan': '1',
            'Origin': 'https://webvpn.nankai.edu.cn',
            'Referer': 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'token': '8232c0ea981c406c8d70c8146dc4fb52',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    }
    # key={
    #     "sysKind": '8',
    #     "appAccNo": '22409',
    #     "memberKind": '1',
    #     "resvMember": '[22409]',
    #     "resvBeginTime": "2022-04-10 16:00:00",
    #     "resvEndTime": "2022-04-10 17:00:00",
    #     "testName": "",
    #     "captcha": "",
    #     "resvProperty": 0,
    #     "resvDev": '[919557]',
    #     "memo": ""
    # }

    key = {'"sysKind":8,"appAccNo":22409,"memberKind":1,"resvMember":[22409],"resvBeginTime":"'+time_data+' 09:30:00","resvEndTime":"'+time_data+' 23:00:00","testName":"","captcha":"","resvProperty":0,"resvDev":[919642],"memo":""'}

    response = requests.post(url=url,headers=headers,json=key)
    print(response.status_code)
    print(response.text)

def main():

    cookie = get_cookie()



    # cookie2 = 'wengine_vpn_ticketwebvpn_nankai_edu_cn='+cookie+'; refresh=1'    #   原cookie获取方式

    cookie2 = 'show_vpn=0; wengine_vpn_ticketwebvpn_nankai_edu_cn='+cookie+'; refresh=0'

    # cookie2 = 'show_vpn=0; wengine_vpn_ticketwebvpn_nankai_edu_cn=02917bb1103e88c6; refresh=0'   #浏览器获取的cookie

    print(cookie2)

    time.sleep(5)


    # yuyue(cookie2)

    # time.sleep(5)
    # get_in(cookie2)
    # time.sleep(5)
    # time.sleep(6)
    # chaxun(cookie2)    #原来预约的方式，现在好像已经没用了
    # check_cookie(cookie2)


    yuyue(cookie2)

    time_data = get_time()

    # print(get_time())

    # driver.quit()



main()






