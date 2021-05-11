import  requests


urls = 'https://www.taobao.com'


r = requests.get(urls)

print(type(r))

print(r.status_code)

print(type(r.text))

print(type(r.cookies))
print(r.cookies)

print(r.text)