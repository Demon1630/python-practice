import requests
import re
import os

os.mkdir('C:\\Users\\Administrator\\Desktop\\novel')


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

#抓取小说每个章节目录和url
def get_cateloges(url):

    #创建一个空列表，用来存储title和url
    result = []

    r= requests.get(url=url,headers= headers)

    #进行编码
    r.encoding='utf-8'
    html = r.text

    #提取li标签中目录和url内容
    li_list = re.findall('<li>.*</li>',html)

    #利用循环读取 li标签
    for i in  li_list:

        #提取title和url  ，使用seach函数， 使用（）可以后面用group函数直接提取括号中内容出来。
        g = re.search('href="(/.*.html)".*title="(.*)"',i)

        #把title和url连接起来
        url_all = g.group(2)+ '\t\t\t'+ 'http://www.doupoxs.com'+g.group(1) + '\n'
        # print(url_all)

        #用字典存储单个titl和对应的url，然后添加到列表中
        chapter = {'title':g.group(2),'url':'http://www.doupoxs.com'+g.group(1)}
        result.append(chapter)

        #把内容存储到桌面上文件中，由于是循环存储，使用 a+
        # f = open(r'C:\Users\Administrator\Desktop\novel_list.txt', 'a+')
        # f.write(url_all)

    #把存储的每个章节标题和url的列表返回
    return result

#抓取小说正文
def get_content(chapters):


    for chapter in chapters:
        # print(chapter)
        url_l = chapter['url']

        response = requests.get(url=url_l,headers=headers)
        response.encoding='etf-8'

        # print(response.text)


        content_all = re.search('m-post"(.*)</div>',response.text,re.S)   #加上re.s 因为 . 无法匹配\n换行符，当文章中有换行符时，会出错，所以加上re.S，使得 . 号可以匹配所有字符

        contents = re.findall('<p>(.*?)</p>', content_all.group())
        for content in contents:
            name = chapter['title']
            name = name.replace('?','')
            dic = 'C:\\Users\\Administrator\\Desktop\\novel\\'+name+'.txt'
            f = open(dic, 'a+')
            f.write(content+'\n')
        print(f'{name}打印成功')
        # print(content_all.group(1))



url1 = "http://www.doupoxs.com/nalanwudi/"
chapters = get_cateloges(url1)

get_content(chapters)

