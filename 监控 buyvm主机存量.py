import  requests
from bs4 import BeautifulSoup
# import re
# from fake_useragent import UserAgent
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
    message['From'] = Header("小葫芦")
    message['To'] =  Header("警告警告！")

    subject = 'buyvm主机监控'  #主题
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



def send_telegram(text):
    chat_id = '1203976293'
    token = '1853245438:AAFquYVfAcEEJ_ouNbKM5Z8-GSHfitYipms'
    bot = telegram.Bot(token=token)

    bot.send_message(chat_id=chat_id, text=text)


def make_sure():
    url = 'https://my.frantech.ca/cart.php'

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'WHMCSAffiliateID=2787; __tawkuuid=e::my.frantech.ca::ph7uSokZQoHuo6LfGVUPiAQDEzW0XrA46LZFZWGUdgQQL70GGIb500qP4gyaE3Gc::2; flp_checksum=67CCCC3F06494BF88004C6B04DA90BAD; __stripe_mid=1bcbbdae-9080-477b-a0eb-0306b7a761ab6e80ac; WHMCSdl2ywzxcLWez=r2scgdlktvd43kjbp33flboub4; __stripe_sid=621295dd-895b-4382-8d17-ff90aa96358c6599db; TawkConnectionTime=0',
    'DNT': '1',
    'Host': 'my.frantech.ca',
    'Referer': 'https://my.frantech.ca/index.php',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    }

    respons = requests.get(url=url,headers=headers)

    soup = BeautifulSoup(respons.content,'lxml')

    # print(type(soup))
    # print(soup.title)

    goods = soup.find_all('div',class_ = 'package')

    k = 0
    for i in goods:

        price = i.find('div',class_ ='price')
        avaiable = i.find('div',class_='package-qty')
        # print(price.text)
        # print(avaiable.text.strip())
        if avaiable.text.strip() != '0 Available':    #根据关键词判断是否有货
            print(f'{price.text}有货了,快去买')
            send_telegram(f'{price.text}有货了,快去买{url}')   #如果有货就发送通知和邮件
            send_mail(f'{price.text}有货了,快去买{url}')
            k += 1


        # else:
        #     send_telegram()
        #     k +=1
    if k ==0:   #利用 k 判断是否全部都无货
        send_telegram(f'暂时都没货{url}')
        print('暂时都没货')


def main():
    try:
        make_sure()
    except:
        send_telegram('出错了')

main()