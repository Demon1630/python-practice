import requests


#分钟级别降雨预测，付费
html = requests.get('https://api.qweather.com/v7/minutely/5m?location=120.15568361068728,30.325674788822027&key=50ed3b00f6224a5dbd68e0ac73c10dde')
print(html.text)
predic = eval(html.text).get('summary')

print(f'天气预测:{predic}')

#未来24时天气预测，免费
respons= requests.get('https://devapi.qweather.com/v7/weather/24h?location=120.162349,30.33473&key=ac9fa3adf2b9442e810d19ef581d84d3')
# print(respons.text)
# print(respons.json())
#
# print(type(eval(respons.text)))

# for item in eval((respons.text)).items():
#     print(item)

weather = eval((respons.text)).get('hourly')
# print(weather)
# print(type(weather))
# print(len(weather))
str = '时间\t\t\t\t\t天气\t\t温度'+'\n'
# print(str)
for i in weather:
    # print(i)
    # print(type(i))
    # print(i.get('text'))
    wea = i.get('text')
    tim = i.get('fxTime')[:16].replace('T',' ')
    temp = i.get('temp')
    str = str + tim + '\t'+wea+'\t    '+temp+'\n'
    # print(f'{tim}\t{wea}\t    {temp}\t')

print(str)