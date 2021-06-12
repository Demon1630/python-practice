# -*- coding: UTF-8 ...
import re
import time

import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import telegram
import schedule

def get_time():
    # 格式化成2016-03-20 11:45:39形式
    real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print (real_time)
    return real_time




# print(date)


def get_info():
    url = 'https://healthreport.zju.edu.cn/ncov/wap/default/save'

    date = get_time()[:10].replace('-', '')

    headers = {
                'Host': 'healthreport.zju.edu.cn',
                'Connection': 'keep-alive',
                'Content-Length': '2844',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Origin': 'https://healthreport.zju.edu.cn',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Linux; U; Android 10; zh-CN; MI 8 Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.13.2.100 Mobile Safari/537.36 AliApp(DingTalk/5.0.15) com.alibaba.android.rimet.zju/13014669 Channel/1543545060864 language/zh-CN UT4Aplus/0.2.25 colorScheme/light',
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'Referer': 'https://healthreport.zju.edu.cn/ncov/wap/default/index?ticket=ST-7273876-uikCTfw6HAVDxilcpryF-zju.edu.cn',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN, en-US;q=0.8',
                'Cookie':'UUkey=f5ee3f558d204787c88bdd803024d1bc; cas_ck=8EA0E39822ECEFF3DE38FED2679E5CD101EB66E39F6914123633EBDCE5AF5714DAFCC8EA9BEEF0A6C3039938DE6EE6779DD1A4AFA0B7F119506A6D057C029D05C1DBD8FC845E98C5C66C341CE1329A92; eai-sess=h46pl5nue91qi0dua7aqms2v06; _csrf=S8mwplVi9KWoF2WQ0TlCeDUWbCzhCYB4i8HdSTKVNhs%3D; _pv0=yCVskit%2F0F1VBTSoAWQeU%2Bob%2BaY69qKl0%2BVbtTxoKajWQx2qwznZl%2Bb44LLQ1lUBLnvNI0amUuoIdM75s8skBRpLySh72rYV%2BvKWDIP7fJJzfha%2FbVRp6FUp5WhdajRH%2Bfd4IO3fWEMXZnqNIxLeHlKcsD0UmA1dJun6rPNzkMNQHA4Ou%2Bof51JpGSRoPcHX6G6xajZHK9m%2FSzpg1%2F3UB4EwgEY0wc6c2lnEr0lBx40JHXV4%2Fery4p00FjMvJuzt6zupgjQllA%2B5N%2BhqCu8ppXpfv5vzXTSt9fmPwLULPCr1Au%2Fg9uS5htNi03T9HPOREyXOLpvVmIeReB6Ibx4hS7%2FJ%2BS%2Bsas8%2BntB8H3rZuE40X1TtmN%2BWgYq%2B9ZXImSB5Vgk4X04JwDenrw%2FEIP92npMgEnUghTHA0B7JB2SJriA%3D; _pc0=4wxTRYkh1Mj8bgEFWbRXyBfJIU2SRPauYYIKzcgdLLY%3D; Hm_lvt_48b682d4885d22a90111e46b972e3268=1621501604,1622126211; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1622791540; iPlanetDirectoryPro=yefZrkLWLa0mnVRJyzbb6DACCEr5147CSCXgfjZGygHtjKbAuHIpCd8liLZbeH8GZu2%2B0faoebRP8oanP3aFWC1gGocpSGYTT1%2BMMcH%2FY2w5w3%2FRL0o7GSnVPj50vTRPzCsJrffMwGLtrsr4atu1TMENYwGAkBIarwzT7li0HLdO1ebIVoaz5TneJLfHTZhtN%2FMJEadR9MtF63UDhE0brwCPA5EVey%2F9Tc8nRajg4mXSQbqwuxmXgQbNSPHj%2F%2BmSoRKz4dsyyvviu1EBZoxBMxRAxLV13XABxRt3D7xO1TjVumzNaZ%2FxG2P6dpFEzEhgWpJqgBF4wG2vv6kW6hIizyRqqpHd%2FmzIqpogxNyRAwrJjgGawoMFSqsk2WVTexyg8%2FpV%2BWeRuFuvvK3QBYs7MQujTYutpDn0Bbw4GBRqckhJNBK4L0BoFdcP4EyIFfMsGSbxHa2MXEIaNC57BRvlmoUmLheWIZngd3RujEojKczaEY1SQrZ%2BSe9akIZRXvuP3UDB0PRYv2grxkSmE80SaGTRoScVx5BAN%2FCspEfPQ1F7CyhO74kJN5p5Qq2yVoK7MFfAI4y3xmNqPrZw9FpZ6xzM0tEnAPly66Olo%2FDy0ADYLAD0gtm4%2BOa7bKQH4B%2FbTjTK33yJ8HpZ7%2BEp7BzLFj%2B0ga1zbZIZs6f8YMtYWrckOWjmWzbIPQtH1oWEIaYFMh6q%2FddkYJGDn1CaaE4Z76siMRZvrpK9tqDHPX7bSXc%3D',

    }

    key = {
        'sfymqjczrj': '0',
        'zjdfgj':'',
        'sfyrjjh':'0',
        'cfgj':'',
        'tjgj':'',
        'nrjrq': '0',
        'rjka':'',
        'jnmddsheng':'',
        'jnmddshi':'',
        'jnmddqu':'',
        'jnmddxiangxi':'',
        'rjjtfs':'',
        'rjjtfs1':'',
        'rjjtgjbc':'',
        'jnjtfs':'',
        'jnjtfs1':'',
        'jnjtgjbc':'',
        'sfqrxxss':'1',
        'sfqtyyqjwdg': '0',
        'sffrqjwdg': '0',
        'sfhsjc':'',
        'zgfx14rfh':'0',
        'zgfx14rfhdd':'',
        'sfyxjzxgym':'1',
        'sfbyjzrq': '5',
        'jzxgymqk': '2',
        'id': '27554633',
        'uid': '6100',
        'date': date,
        'tw': '0',
        'sfcxtz': '0',
        'sfyyjc': '0',
        'jcjgqr': '0',
        'jcjg':'',
        'sfjcbh':'0',
        'sfcxzysx': '0',
        'remark':'',
        'address': '%E6%B5%99%E6%B1%9F%E7%9C%81%E6%9D%AD%E5%B7%9E%E5%B8%82%E8%A5%BF%E6%B9%96%E5%8C%BA%E4%B8%89%E5%A2%A9%E9%95%87%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6%E8%89%BA%E6%9C%AF%E4%B8%8E%E8%80%83%E5%8F%A4%E5%8D%9A%E7%89%A9%E9%A6%86%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6%E7%B4%AB%E9%87%91%E6%B8%AF%E6%A0%A1%E5%8C%BA',
        'area': '%E6%B5%99%E6%B1%9F%E7%9C%81+%E6%9D%AD%E5%B7%9E%E5%B8%82+%E8%A5%BF%E6%B9%96%E5%8C%BA',
        # 'province': '%E6%B5%99%E6%B1%9F%E7%9C%81',
        # 'province': '\\u6d59\\u6c5f\\u7701',
        'province': '浙江省',
        # 'city': '%E6%9D%AD%E5%B7%9E%E5%B8%82',
        'city': '杭州市',
        'geo_api_info': '%7B%22type%22%3A%22complete%22%2C%22info%22%3A%22SUCCESS%22%2C%22status%22%3A1%2C%22cEa%22%3A%22jsonp_598090_%22%2C%22position%22%3A%7B%22Q%22%3A30.29804%2C%22R%22%3A120.07193000000001%2C%22lng%22%3A120.07193%2C%22lat%22%3A30.29804%7D%2C%22message%22%3A%22Get+geolocation+time+out.Get+ipLocation+success.Get+address+success.%22%2C%22location_type%22%3A%22ip%22%2C%22accuracy%22%3Anull%2C%22isConverted%22%3Atrue%2C%22addressComponent%22%3A%7B%22citycode%22%3A%220571%22%2C%22adcode%22%3A%22330106%22%2C%22businessAreas%22%3A%5B%7B%22name%22%3A%22%E8%A5%BF%E6%BA%AA%22%2C%22id%22%3A%22330106%22%2C%22location%22%3A%7B%22Q%22%3A30.271791%2C%22R%22%3A120.09102999999999%2C%22lng%22%3A120.09103%2C%22lat%22%3A30.271791%7D%7D%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E4%BD%99%E6%9D%AD%E5%A1%98%E8%B7%AF%22%2C%22streetNumber%22%3A%22900%E5%8F%B7%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E6%B5%99%E6%B1%9F%E7%9C%81%22%2C%22city%22%3A%22%E6%9D%AD%E5%B7%9E%E5%B8%82%22%2C%22district%22%3A%22%E8%A5%BF%E6%B9%96%E5%8C%BA%22%2C%22township%22%3A%22%E4%B8%89%E5%A2%A9%E9%95%87%22%7D%2C%22formattedAddress%22%3A%22%E6%B5%99%E6%B1%9F%E7%9C%81%E6%9D%AD%E5%B7%9E%E5%B8%82%E8%A5%BF%E6%B9%96%E5%8C%BA%E4%B8%89%E5%A2%A9%E9%95%87%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6%E8%89%BA%E6%9C%AF%E4%B8%8E%E8%80%83%E5%8F%A4%E5%8D%9A%E7%89%A9%E9%A6%86%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6%E7%B4%AB%E9%87%91%E6%B8%AF%E6%A0%A1%E5%8C%BA%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%7D',
        'created': '1622766621',
        'qksm':'',
        'sfzx':'1',
        'sfjcwhry': '0',
        'sfcyglq': '0',
        'gllx':'',
        'glksrq':'',
        'jcbhlx':'',
        'jcbhrq':'',
        'sftjwh': '0',
        'sftjhb': '0',
        'fxyy':'',
        'bztcyy':'',
        'fjsj': '0',
        'sfjchbry': '0',
        'jrsfqzys':'',
        'jrsfqzfy':'',
        'sfyqjzgc':'',
        'jrdqjcqk':'',
        'sfjcqz':'',
        'jcqzrq':'',
        'jcwhryfs':'',
        'jchbryfs':'',
        'xjzd':'',
        'szgj':'',
        'sfsfbh': '0',
        'jhfjrq':'',
        'jhfjjtgj':'',
        'jhfjhbcc':'',
        'jhfjsftjwh':'0',
        'jhfjsftjhb': '0',
        'szsqsfybl': '0',
        'sfsqhzjkk': '1',
        'sqhzjkkys': '1',
        'sfygtjzzfj': '0',
        'gtjzzfjsj':'',
        'gwszgz':'',
        'gwszgzcs':'',
        'gwszdd':'',
        'szgjcs':'',
        'ismoved':'0',
        'zgfx14rfhsj':'',
    }

    response =requests.post(url=url,headers=headers,data=key)
    # print(response.status_code)
    if response.status_code == 200:
        print(response.text)
        return str(response.text)
    else:
        return '打卡出错了'


def send_telegram(text):
    chat_id = '1203976293'
    token = '1886850695:AAG-gfzszOsF_RPJHdYCaI0maxszwd4qoL4'
    bot = telegram.Bot(token=token)

    bot.send_message(chat_id=chat_id, text=text)


def send_wechat(text):
    # url = 'https://sc.ftqq.com/SCU93555Tc0608f46612b3f58458bc7236a6b17285e91f9c6173ab.send'
    url = 'https://sctapi.ftqq.com/SCT43501TagBvqSsCzQ5zc1ZyBbthfB8L.send'
    headers = {
            'User-Agent':UserAgent().random
    }
    key = {
        'title':'每日打卡通知',
        'desp':text,
    }
    response = requests.post(url=url,headers=headers,data=key)
    # print(response)



def main():
    try:
        info = get_info()
        # print(info)
        send_wechat(info)
        send_telegram(info)

    except:
        send_wechat('错误')
        send_telegram('错误')

if __name__ == '__main__':
    main()

