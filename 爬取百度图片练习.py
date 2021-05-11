import requests
from bs4 import BeautifulSoup


# headers = {
#     'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
# }

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
}




url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&oq=%E7%BE%8E%E5%A5%B3&rsp=-1'

r = requests.get(url=url,headers=headers)

html = r.content

soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
print(soup)

f = open('C:\\Users\\Administrator\\Desktop\\1111.txt', 'a+',encoding='utf-8')
f.write(soup.prettify())
f.write('2')
f.close()

spans = soup.find_all(name='div',attrs={'class':'imgbox'})
# spans = soup.find_all(name='img',attrs={'class':'main_img img-hover'})

# print(soup.title)
# for i in  spans:
#     print(i)
# print(spans)