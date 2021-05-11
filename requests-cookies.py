import requests

r1 = requests.get('http://wwwbaidu.com')

print(r1.cookies)

for key,value in r1.cookies.items():
    print(f'cookies是：{key}={value}')

