import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
from lxml import etree




header = {'User-Agent':UserAgent().random}
print(header)

url = 'https://www.qidian.com/rank/yuepiao?page=1'

response = requests.get(url=url,headers=header)


# print(response.text.replace('\r',''))   #终于找到了  哈哈哈！  反爬虫  必须去除 \r  否则都是空白

html = etree.HTML(response.text)


#获取字体反扒对应文件
# font_url = re.findall("; src: url\('(.*?)'\) format",response.text)[1]
# print(font_url)

soup = BeautifulSoup(response.text.replace('\r',''),'html.parser')
# print(soup.find(class_='book-img-text'))

for i in range(1,21):

    for li in soup.find_all(name='li',attrs={'data-rid':f'{i}'}):
        # print(li)

        print(li.contents[1].text,end='\t')
        # print(li.contents[3].h4.a['href'])
        print(li.contents[3].text)

        print(li.contents[5].text)
        # for a in li.contents:
        #     print(a)
        # print(type(li))
    i +=1

# print(type(soup.find(class_='book-img-text')))


# for i in range(1,20):



    # soup = BeautifulSoup(response.content,'html.parser')

    # lis = soup.find_all(name='div',attrs={'class_':'book-img-text'})
    # for li in  lis:
        # print(li)

    # Num = soup.select(f'#rank-view-list > div > ul > li:nth-child({i}) > div.book-img-box > span')[0].text
    # print(f'排名：{Num}')
    #
    # name = soup.select(f'#rank-view-list > div > ul > li:nth-child({i}) > div.book-mid-info > h4')[0].text
    # print(name)
    #
    # author = soup.select(f'#rank-view-list > div > ul > li:nth-child({i}) > div.book-mid-info > p.author')[0].text
    # print(author)
    #
    # total = soup.select(f'#rank-view-list > div > ul > li:nth-child({i}) > div.book-right-info > div > p')[0].text
    # print(total)
    #
    # nodes = html.xpath(f'//*[@id="rank-view-list"]/div/ul/li[{i}]/div[2]/p[2]/text()')[0].replace('\r','')
    # print(type(nodes))
    # print(len(nodes))
    # print(nodes)
