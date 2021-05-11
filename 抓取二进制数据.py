import requests

r = requests.get('https://tenfei03.cfp.cn/creative/vcg/veer/1600water/veer-373639937.jpg')
# print(r.text)

print(type(r.content))
# print(r.content)

with open(r'C:\Users\Administrator\Desktop\2.txtPython从菜鸟到高手.png','wb') as f:

    #content内容是字节文件
    f.write(r.content)

