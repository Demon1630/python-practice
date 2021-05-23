import requests
import re
from bs4 import BeautifulSoup
import time

def get_in(url):

    headers = {
    'authority': 'hostloc.com',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'cookie': 'hkCM_2132_sid=ZBKm14; hkCM_2132_saltkey=nCpk13T1; hkCM_2132_lastvisit=1621780014; hkCM_2132_sendmail=1; hkCM_2132_st_t=0%7C1621783616%7C5bd718fd76a1191fea65e7c8c0b33363; hkCM_2132_forum_lastvisit=D_45_1621783616; hkCM_2132_visitedfid=45; hkCM_2132_secqaaqSZBKm14=398.9754eef16740fdd654; hkCM_2132_seccodecSZBKm14=399.53194c1f84b7789908; hkCM_2132_lastact=1621783671%09member.php%09logging; hkCM_2132_ulastactivity=fd3fmr6P5fmyahDylR9R9V9ArI2nXlw9TY%2FxwbgY7wn1y%2FPay3%2BJ; hkCM_2132_auth=2791ni%2F8h86%2ByY9xswIkQQwOazjaxLMSGFHiJvECCaPbvJ3OaA%2Byj0u8kKtUIfsEtRdL85%2FB7bHRXFNDzvWbTNELkg; hkCM_2132_lastcheckfeed=41544%7C1621783671; hkCM_2132_checkfollow=1; hkCM_2132_lip=95.169.25.225%2C1621783614',
    'dnt': '1',
    'referer': 'https://hostloc.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    }

    respons = requests.get(url=url,headers=headers)

    # url1 = 'https://hostloc.com/forum.php?mod=guide&view=my'
    # respons2 = requests.get(url=url1,headers=headers)
    # print()
    # print(respons)
    return respons

def get_time():
    # 格式化成2016-03-20 11:45:39形式
    real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print (real_time)
    return real_time

def main():
    url = 'https://hostloc.com/'
    times = get_time()
    try:


        code_ = get_in(url)
        print(f'{times}  登录成功')
    except:
        print(f'{times}  登录出错')

if __name__ == '__main__':
    main()

