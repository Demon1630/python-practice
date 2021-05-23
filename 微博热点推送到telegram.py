# -*- coding: UTF-8 ...
import re
import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用
import openpyxl
import wordcloud
import jieba  #分词
import telegram



headers = {
    'User-Agent':UserAgent().random
}

def get_content(url):

    response = requests.get(url=url,headers=headers)

    # print(response.text)

    soup =BeautifulSoup(response.text,'html.parser')   #必须要加上content或者text

    # print(soup)
    content = soup.tbody
    # print(content)
    # print(type(content))
    lists = content.find_all('tr')
    i = 1
    list=[]
    for l in lists:

        # print(l)
        # print(type(l))
        dic_li = []
        if i != 1:   #排除掉第一个上升热点
            info_num = l.find('td', class_='td-01 ranktop').text  #获取排名
            dic_li.append(info_num)
            # print(info_num)
            info_name = l.find('td',class_ = 'td-02').a.text   #获取关键词
            info_url = 'https://s.weibo.com'+l.find('td',class_='td-02').a.attrs['href']   #获取链接
            # print(info_name)
            # print(info_url)
            dic_li.append(info_name)
            dic_li.append(info_url)

            # print(dic_li)
            list.append(dic_li)
        i += 1


    return list
    # print(list)


def send_telegram(text):
    chat_id = '1203976293'
    token = '1865491593:AAG_GtZ7ANjE54m_9m1JGex1fQPtW9Wy8jM'
    bot = telegram.Bot(token=token)

    bot.send_message(chat_id=chat_id, text=text)


def main():
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    try:
        list = get_content(url)
        for l in list:
            if l[0].isdigit() :
                if int(l[0]) <= 20:
                    text =  l[0] + '  ' + l[1] + '  '+ l[2] +'\n'
                    send_telegram(text)
                    print(text)
    except:
        send_telegram('采集出错了！')


if __name__ == '__main__':

    main()



