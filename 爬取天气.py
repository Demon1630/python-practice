# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def get_time():
    # 格式化成2016-03-20 11:45:39形式
    real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print (real_time)
    return real_time


def get_weather(url):

    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'ssuid=8929248355; tour_city=%E5%8C%97%E4%BA%AC; __mtmc=123890447; __mtmz=123890447.1621324370.1.1.mtmcsr=(direct)|mtmccn=(direct)|mtmcmd=(none); SUV=00FBE666DA6CBF6E60A372527D5EE861; __mtma=123890447.522512551.1621324370.1621324370.1621324370.2; location_key=105567; wt_city=changsha; tid=101250101; __mtmb=123890447.4.99.1621326566672',
        'DNT': '1',
        'Host': 'tianqi.sogou.com',
        'Pragma': 'no-cache',
        'Referer': 'http://tianqi.sogou.com/pc/weather?tid=101280601',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': UserAgent().random,
    }

    html = requests.get(url=url,headers=headers)
    respons = html.content.decode('utf-8')
    # print(type(respons))
    # print(respons)

    res = BeautifulSoup(respons,'lxml')

    #获取城市
    city = res.find('em',class_='city-name').text
    # print(f'城市：{city}')
    str = '地区：' + city

    #爬取当前温度
    tem = res.find('span',class_='num').text
    # print(type(tem))
    # print(f'当前温度：{tem}')
    str = str + '\n' + '当前温度：' + tem +'℃'

    #获取今日最高温度
    # tem_high = re.search('y="22">(.*?)</text>',respons)
    # print(tem_high)

    #爬取空气质量
    air = res.find('span',class_='liv-text').a.text.replace('\n',' ')
    # print(type(air))
    # print(air)
    str = str + '\n' + air

    #爬取风力湿度等信息
    wind = res.find('p',class_='condition').text.replace('\n',' ').lstrip()
    # print(type(wind))
    # print(wind)
    str = str + '\n' + wind

    #获取当天天气信息
    weather = res.find_all('li',class_='r-col')
    # print(type(weather))
    # print(weather)
    for w in weather:
        weather_all = w.text.replace('\n',' ').lstrip()
        # print(weather_all)
        str = str + '\n' + weather_all

    #获取预警信息
    warn = res.find('div',class_='row3')
    # print(type(warn))
    # print(warn.text)
    # print(len(warn.text))
    #增加判断是否有预警信息
    if len(warn.text)>2:
        li = warn.find_all('p')
        # print(type(li))
        for warn in li:
            # print(warn.text.replace('\n',' ').lstrip())
            # print(warn.a.attrs['href'])
            warn_title = warn.text.replace('\n',' ').lstrip()
            warn_url = warn.a.attrs['href']

            #获取预警内容
            warn_data = requests.get(url=warn_url)
            soup = BeautifulSoup(warn_data.content.decode('utf-8'),'lxml')
            # print(soup.text)
            data = soup.find('div',class_='text').text
            # print(soup.find('div',class_='text'))

            str = str +'\n'+warn_title+':'+data


    return str


def send_mail(string):
    # 第三方 SMTP 服务
    mail_host="mail.strivefysfxyh.com"  #设置服务器
    mail_user="huyj@strivefysfxyh.com"    #用户名
    mail_pass="x#3RDK*%JFFZ5f"   #  密码

    sender = 'huyj@strivefysfxyh.com'
    receivers = ['1499906118@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # message = MIMEText(string, 'plain', 'utf-8')
    message = MIMEText(string, 'plain')
    message['From'] = Header("小葫芦")
    message['To'] =  Header("老婆")

    subject = '天气'  #主题
    # message['Subject'] = Header(subject,'utf-8')
    message['Subject'] = Header(subject)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")



def main():
    #拱墅区
    # url = 'http://tianqi.sogou.com/pc/weather/2333616'
    #岳麓区
    url = 'http://tianqi.sogou.com/pc/weather/2332937'
    data = get_time()+'\n'+ get_weather(url)
    # print(data)
    send_mail(data)

if __name__ == '__main__':
    main()


