from bs4 import BeautifulSoup

soup = BeautifulSoup('<h2>hello world</h2>','lxml')

print(soup.h2.string)