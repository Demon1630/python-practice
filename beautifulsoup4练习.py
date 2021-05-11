from bs4 import BeautifulSoup

# soup = BeautifulSoup('<h2>hello world</h2>','lxml')
#
# print(soup.h2.string)

html='''
<html>
    <head><title>这是一个演示页面</title></head>
    <body>
        <a href='a.html'>第一页</a>
        <p>
        <a href='b.html'>第二页</a>
    </body>
</html>
'''

soup = BeautifulSoup(html,'lxml')

#打印title标签
print('<'+soup.title.string +'>')

#打印a标签中的url链接
print('['+soup.a["href"]+']')

#打印格式化html代码
print(soup.prettify())
