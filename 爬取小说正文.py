import re
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}


def get_content(url):


    # for chapter in chapters:
    #     print(chapter)
    #     url_l = chapter['url']

    response = requests.get(url=url,headers=headers)
    response.encoding='etf-8'

    # print(response.text)


    content_all = re.search('m-post(.*)</div>',response.text,re.S)

    print(content_all.group(0))


    contents = re.findall('<p>(.*?)</p>', content_all.group())

    # for content in contents:
        # name = chapter['title']
        # name = name.replace('?','')
        # dic = 'C:\\Users\\Administrator\\Desktop\\novel\\'+name+'.txt'
        # f = open(dic, 'a+')
        # f.write(content+'\n')
        # print(f'{name}打印成功')
        # print(content_all.group(1))

        # str = content + '\n'

    # print(str)

get_content('http://www.doupoxs.com/nalanwudi/2911.html')
