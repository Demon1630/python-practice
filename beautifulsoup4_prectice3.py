#导入 bs4 库
import bs4
from bs4 import BeautifulSoup
#准备一串heml代码信息用来练习获取内容
html = """  
<html>
<head><title>The Dormouse's story</title></head>  
<body>  
<h1><b>123456</b></h1>
<p class="title" name="dromouse">
    <b>The Dormouse's story</b>
    aaaaa
</p> 
<p class="title" name="dromouse" title='new'><b>The Dormouse's story</b>a</p>   
<p class="story">Once upon a time there were three little sisters; and their names were  
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,  
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and  
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    <a href="http://example.com/tillie" class="siterr" id="link4">Tillie</a>;  
    <a href="http://example.com/tillie" class="siterr" id="link5">Tillie</a>;  
    and they lived at the bottom of a well.
</p>  
<p class="story">...</p>
<ul id="ulone">
    <li>01</li>
    <li>02</li>
    <li>03</li>
    <li>04</li>
    <li>05</li>
</ul>
<div class='div11'>
    <ul id="ultwo">
        <li>0001</li>
        <li>0002</li>
        <li>0003</li>
        <li>0004</li>
        <li>0005</li>
    </ul>
</div>
</body> 
</html>
"""





#1.得到beautifulsoup对象
soup = BeautifulSoup(html,'html.parser')


# print(soup.p.attrs)
# print(soup.div.string)

# for i in soup.find_all('p'):
#     print(i.attrs)
#     print(i.attrs['class'])

#奇怪
print(soup.find_all(name='dromouse'))   #为什么name属性不行
# print(soup.find_all(title="new"))
print(soup.find_all(class_="title"))
print(soup.find_all(class_="title",title="new"))   #多个属性过滤


# for i in soup.p.children:
#     print(i)


# #2.获取内容
# #获取标题对象
# print(soup.title)
# #获取文本内容
# print(soup.title.get_text())
# print(soup.title.string)
# print(soup.title.text)
#
#
#
# #通过上下级关系获取
# print(soup.title.parent)   #父级
# print(soup.title.child)#没有下级返回None
#
# #获取第一个P标签
# print(soup.p)
# #获取P的孩子们
# print(soup.p.children)
# for i,each in enumerate(soup.p.children):
#     print(i,each)
# print(list(soup.p.children)[2])
#
#
# #获取标签的属性
# print(soup.a)
# print(soup.a.id)#获取不到
# print(soup.a.href)#获取不到
# print(soup.a.name)
# #应该这样写
# print(soup.a.attrs['id'])
# print(soup.a.attrs['href'])
# print(soup.a.attrs['class'])#class得到一个list
#
# #获取多个
# print(soup.find('p'))#获取一个P
# print(soup.find_all('p'))#获取SOUP内的P，要看是谁的find_all()
#
# #多层查询
# print(soup.find_all('ul')[0].find_all('li'))
# print(soup.find('ul').find_all('li'))
#
# #通过指定的 属性获取对象
# print(soup.find(id='ulone'))#单个对象
# print(soup.find('ul',id='ulone'))#单个对象
# print(soup.find_all('ul',id='ulone'))#这个是列表，实际使用要加下表的
#
# #calss这么写class_
# print(soup.find_all('p',class_='title'))
# #更通用的方式
# print(soup.find_all('p',attrs={'class':'title'}))
# print(soup.find_all('p',attrs={'class':'title','title':'new'}))
#
# #使用函数 作为参数获取元素
# def judgeTitle(t):
#     if t == 'div11':
#         return True
# print(soup.find_all(class_=judgeTitle))
#
# import re
# reg = re.compile('sis')
# def judgeLen(t):
#     #f返回长度为6，且包含’sis‘的参数
#     return len(str(t))==6 and bool(re.search(reg,t))
# print(soup.find_all(class_=judgeLen))
#
#
# #limit参数：限制访问个数
# print(soup.find_all('a',limit=2))
#
# #recursive参数：recursive = Ture 寻找子孙。false只寻找子
# print(soup.find_all('body')[0].find_all('ul',recursive='false'))