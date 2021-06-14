# -*- coding: UTF-8 ...
import re
import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import telegram
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

def get_time():
    # 格式化成2016-03-20 11:45:39形式
    real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print (real_time)
    return real_time

def send_telegram(text):
    chat_id = '1203976293'
    token = '1870256785:AAGGYEIaDf9UBs6TBe91ZmxqNRqfMKnZXN4'
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



def get_info():
    # url = 'https://www.demon1630.ga/'
    url = 'https://www.demon1630.ga/json/stats.json'

    headers = {
        'User-Agent':UserAgent().random
    }

    respons = requests.get(url=url,headers=headers)

    print(respons.status_code)
    # print(respons.text)

    data = eval('['+ re.search('"servers": \[\n(.*?)\],',respons.text,re.S).group(1).replace('true','111').replace('false','000') + ']')   #转换成列表
    # print(type(eval(data)))


    # print(data)
    # print(len(data))
    text = get_time() +'\n'
    for i in data:
        # print(i)
        info = eval(str(i))   #获得内容字典
        # print(type(info))
        if info['online4'] == 111:
            status = '在线'
        else:
            status = '不在线'
        memory =  float(info["memory_used"])/float(info["memory_total"])*100
        hdd = float(info["hdd_used"])/float(info["hdd_total"])*100

        text = text+f'主机: {info["name"]}  {status}, 在线时长：{info["uptime"]}  CPU：{info["cpu"]}%  内存：{int(memory)}%  硬盘：{int(hdd)}%' + '\n'

        if hdd >80:
            warm1 = f'警告 {info["name"]} 硬盘使用过高，超过80%'
            send_wechat('主机监控',warm1,'https://www.demon1630.ga/')
            send_telegram(warm1)
            # print(warm1)
        if memory >85:
            warm2 = f'警告 {info["name"]} 内存使用过高，超过85%'
            send_wechat('主机监控',warm2,'https://www.demon1630.ga/')
            send_telegram(warm2)
            # print(warm2)


        # print(f'主机: {info["name"]}  {status}, 在线时长：{info["uptime"]}  CPU：{info["cpu"]}%  内存：{int(memory)}%  硬盘：{int(hdd)}%')

    # print(text)
    return text

def main():
    try:
        info = get_info()
        send_telegram(info)
        send_wechat('主机监控',info,'https://www.demon1630.ga/')
    except:
        send_wechat('主机监控','查询出错','https://www.demon1630.ga/')
        send_telegram('查询出错')

if __name__ == '__main__':
    main()


