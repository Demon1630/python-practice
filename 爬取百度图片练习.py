import requests
from bs4 import BeautifulSoup
import json
import random
import string
import os

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
}

word = input('请输入搜索关键字：')
print(word)

dir_name = input('请输入存储文件夹名：')
os.mkdir('C:\\Users\\Administrator\\Desktop\\'+dir_name)
print(f'图片将存储在：{dir_name}文件夹中')


max_value = 100
current_value = 0

image_index = 1
while current_value < max_value:

    result = requests.get('https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11092943101252335937&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A4%96%E6%98%9F%E4%BA%BA&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={}s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=1e&1620734157038='.format(word,current_value),headers=headers)

    # print(result)

    json_str = result.content
    json_doc = str(json_str,'utf-8')
    # print(json_doc)

    image_result = json.loads(json_doc)

    print(image_result)
    data = image_result['data']
    # print(data)

    #
    # for record in data:
    #     url = record.get('middleURL')
    #     if url != None:
    #         print(f'正在下载图片：{url}')
    #         r = requests.get(url=url,headers=headers)
    #         file_name = dir_name + '/' + str(image_index).zfill(10) + ".png"
    #
    #         with open(file_name,'wb') as f :
    #             f.write(r.content)
    #             image_index += 1
    #     current_value += 30
    # print('图像下载完成！')
    #




