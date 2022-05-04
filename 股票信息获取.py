# -*- coding: UTF-8 ...
import tushare  #使用tushare接口可以获取股票所有的历史信息
import pandas
import requests
from  fake_useragent import UserAgent
import datetime

# muyuan = tushare.get_k_data(code='002714',start='2015-01-01')   #获取指定日期以来的某股票信息
# print(muyuan)

def get_time():
    day = datetime.datetime.now() + datetime.timedelta(days=1)#.strftime("%Y-%m-%d %H:%M:%S")
    time1 = str(day)[:10]
    return time1

def send_wechat(title,text,detal_url):

    get_acs_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww43746df157f4949f&corpsecret=b0TEEY0L8DI2Q3FWcV_FqSx7lnoCmUeMQyDYOGKxu9Q'      #xyh
    # get_acs_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww428187fbdb9fd50f&corpsecret=po3lAng2YdZzaa67teFhmOxL34EuuWpffdiZlQeGaNk'    #普通通知

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
        "agentid": 1000004,  #xyh
        # "agentid": 1000002,   #普通通知
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
    print('信息发送成功')
    print(res.text)


def get_price():
    time = get_time()
    real_data = tushare.get_realtime_quotes('002714')
    # real_data = real_data[[code]]
    print(real_data)

    price = eval(real_data[['price']].iloc[0][0])
    print(type(price))
    print(price)
    # if price < 47:
    #     send_info(f'{time}:牧原股票低于47了，目前价格为{price}，请留意！')
    # elif price > 60:
    #     send_info(f'{time}:牧原股票高于60了，目前价格为{price}，请留意！')
    # else:
    #     send_info(f'{time}:牧原股票价格为{price}')
    return price

def send_info(price):
    time = get_time()
    if float(price) < 47:
        send_wechat('股票信息',f'{time}:牧原股票低于47了，目前价格为{price}，请留意！',' ')
    elif float(price) > 60:
        send_wechat('股票信息',f'{time}:牧原股票高于60了，目前价格为{price}，请留意！',' ')
    else:
        send_wechat('股票信息',f'{time}:牧原股票价格为{price}',' ')

def main():
    price = get_price()
    print(price)
    send_info(price)

main()
