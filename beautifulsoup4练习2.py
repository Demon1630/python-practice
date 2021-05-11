from bs4 import  BeautifulSoup

html ='''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautiful Soup 演示</title>
</head>
<body>
<div>
    <ul>
        <li class="item1" value1="1234" value2="hello world">
            <a href="https://geekori.com"> geekori.com
            </a>
        </li>
        <li class="item2"><a href="https://www.jd.com">京东商城</a></li>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        
    </ul>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html,'lxml')

print(soup.title.name)
print(soup.title.string)

print(soup.li.attrs)

print(soup.li.attrs["value2"])

print(soup.li["value1"])

print(soup.a["href"])

print(soup.a.string)