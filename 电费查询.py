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


def send_mail(string):
    # 第三方 SMTP 服务
    mail_host="mail.strivefysfxyh.com"  #设置服务器
    mail_user="huyj@strivefysfxyh.com"    #用户名
    mail_pass="x#3RDK*%JFFZ5f"   #  密码

    sender = 'huyj@strivefysfxyh.com'
    receivers = ['1499906118@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # message = MIMEText(string, 'plain', 'utf-8')
    message = MIMEText(string, 'plain')
    message['From'] = Header("hyj")
    message['To'] =  Header("提醒")

    subject = '电费'  #主题
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


def get_cookie():


    f = open(r'C:\Users\Administrator\Desktop\cookie.txt', 'r+')  # 从cookie。txt文件中读取原cookie
    # old_cookie='shiroJID=44c8aa33-bf1d-4478-b224-74e84c52b16a'
    # old_cookie='shiroJID=ed0b475d-52f3-4af9-a2f5-35dc54dcf9a9'
    old_cookie = f.read()
    # print(old_cookie)
    f.close()



    # url = 'https://application.xiaofubao.com/app/invite/jssdk'
    url = 'https://application.xiaofubao.com/app/login/getUser4Authorize'



    headers = {
        'Host': 'application.xiaofubao.com',
        'Connection': 'keep-alive',
        'Content-Length': '76',
        'deviceId':'',
        # 'User-Agent':'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/32.363636) ZJYXYwebviewbroswer ZJYXYAndroid tourCustomer /yunmaapp.NET/2.1.2/0c5bf2652e3c331c',
        'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
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
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': old_cookie,  #cookie 没过期时不会返回新cookie

    }

    key = {
        # 'url':'https%3A%2F%2Fapplication.xiaofubao.com%2F',
        # 'platform':'YUNMA_APP',
        'code' : 'a2309ba493fdf938ec0617f28571496b',
        'userId' : '1906280823241710',
        'schoolCode' : '19335',
        'platform' : 'YUNMA_APP',
    }

    respons = requests.post(url=url,headers=headers,data=key)

    # print(respons)
    # print(respons.text)
    # print(respons.headers)
    # print(old_cookie)
    if str(respons.headers).find('Set-Cookie') != -1:
        new_header = eval(str(respons.headers))
        # for key,value in new_header.items():
        #     print(f'{key}={value}')
        new_Cookie = new_header['Set-Cookie'].split(';',2)
        print(new_Cookie[0])

        f = open(r'C:\Users\Administrator\Desktop\cookie.txt', 'r+')   # 将获取到的新cookie存入cookie.txt文件
        f.write(str(new_Cookie[0]))
        f.close()

        return new_Cookie[0]
    else:
        # print(old_cookie)
        return old_cookie

    # print(type(eval(str(respons.headers))))





def get_info():

    # url = 'https://application.xiaofubao.com/app/electric/queryRoomSurplus HTTP/1.1'
    url = 'https://application.xiaofubao.com/app/electric/queryRoomSurplus'

    cookie = get_cookie()
    print(f'获取到的cookie为{cookie}')
    # cookie = 'shiroJID=2c25f4c7-06f4-46e2-9abd-747400b8aeb8'
    # cookie = 'shiroJID=62d65a90-db40-4684-9496-9c6bc962a38c'


    headers = {
        'Host': 'application.xiaofubao.com',
        'Connection': 'keep-alive',
        'Content-Length': '123',
        'deviceId':'',
        # 'User-Agent':'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/32.363636) ZJYXYwebviewbroswer ZJYXYAndroid tourCustomer /yunmaapp.NET/2.1.2/0c5bf2652e3c331c',
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
        # 'Cookie': 'shiroJID=44c8aa33-bf1d-4478-b224-74e84c52b16a',  #cookie 隔段时间会变化失效   尝试前面先登入然后设置cookie来看看行不行  登录没用。。。。。
        'Cookie': cookie,  #使用获取cookie函数，估计有用
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
            print(f'{data["displayRoomName"][3:]}电费余额为：{data["surplus"]}')

            if data['surplus'] < 17:
                send_mail(f'{data["displayRoomName"][3:]}电费余额为：{data["surplus"]}度,快充电费')
                # print('邮件已发送')

            return f'{data["displayRoomName"][3:]}电费余额为：{data["surplus"]}'

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
        # print(get_in())
        a = get_info()
        print(a)

        # print(type(a))
        send_wechat(a)
        send_telegram(a)

    except:
        send_wechat('出错了')
        send_telegram('出错了')


if __name__ == '__main__':
    main()
