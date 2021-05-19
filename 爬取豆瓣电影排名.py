# -*- coding: UTF-8 ...
import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


headers = {
    'User-Agent':UserAgent().random
}

def get_content(url):
# url = 'https://movie.douban.com/top250'

    respons = requests.get(url=url,headers=headers)

    # print(respons.text)
    try:
        soup = BeautifulSoup(respons.content,'html.parser')

        for j in  soup.find_all('div',attrs={'class':'item'}):    #返回的i是bs4格式，同样还可以用标签继续提取

            list = j.find('div',attrs={'class':'pic'})
            # print(type(list))
            print(f'排名：{list.em.text}',end='\t')

            for i in j.find_all('div',attrs={'class':'info'}):
                # print(f'电影名：{i.a.span}')    #继续使用a标签提取


                    #获取电影名
                    name = i.a.span.text
                    print(f'电影名：{name}\t',end='\t\t')    #继续使用a标签提取电影名

                    #提取导演演员信息
                    info = i.find("div",attrs={"class":"bd"}).p.text.replace('\n','').replace(' ','').strip()
                    print(f'电影信息：{info}',end='\t')    #继续使用a标签提取
                    # print(type(i.find("div",attrs={"class":"bd"})))  #继续使用a标签提取

                    # 获取评分
                    n = str(i)
                    num_list = re.search('average">(.*?)</span>',n)  #使用正则表达式提取出来
                    print(f'评分：{num_list.group(1)}',end='\t')

                    #获取一句话评价
                    eval = re.search('class="inq">(.*?)</span>',n)
                    # print(type(eval))
                    # print(len(eval))
                    #添加一个判断语句
                    if eval:
                        print(f'一句话评价：{eval.group(1)}',end='\t')
                    else:
                        print(f'一句话评价：无',end='\t')

                    #获取详情链接
                    url_detail = i.a.attrs['href']
                    print(f'详情页链接为：{url_detail}',end='\n')
                    print('*'*80)
    except Exception as result:
        print(result)
def geturl_list(i):
    """使用循环获取前250电影页面链接"""
    j = i*25
    url_250 = 'https://movie.douban.com/top250?start='+str(j)+'&filter='
    # print(url_250)
    return url_250

    # print(f'电影名：{i.a.span.next_sibling.next_sibling}')    #继续使用next_sibling标签提取后面的span内容
    # print(f'电影名：{i.a.find_all("span")}')    #继续使用a标签提取
# print(type(soup.find_all('li')))
def main():
    for i in range(0,10):
        print(f'爬取页面{i+1}内容')
        url = geturl_list(i)
        get_content(url)


if __name__ == '__main__':
    main()
