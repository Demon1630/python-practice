# -*- coding: UTF-8 ...
import re
import time

import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import datetime

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()

def get_points():
    url = 'https://router-app-api.jdcloud.com/v1/regions/cn-north-1/routerAccountInfo?mac=DCD87C258CB6'
    headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36 (JBOX-APP; Android/3.0.0/51)',
        'Content-Type': 'application/json',
        'Referer': 'http://guanli.luyou.360.cn/new_index.htm',
        'Connection': 'close',
        'jdmt-rx-sign': '32e62c1ea426c4fd69d73320a7d9efad',
        'jdmt-rx-time': '1638672432476',
        'jdmt-rx-appKey': 'fe2c20725c261e49a80d707a6ab299e1',
        'wskey': 'AAJhgUP3AEAnJrcZNIGgsjSJ_F85JPSY2udsrLkWBbIYG0SXMG_Ucd59rUbPqDEfUDxv5_uqxPtSI3HvUzEvjew9rlmZFAyl',
        'X-MLAAS-AT': 'wl=0',
        'Host': 'router-app-api.jdcloud.com',
        'Accept-Encoding': 'gzip',
    }

    response = requests.get(url=url,headers=headers)
    print(response.status_code)
    print(response.text)

def duihuan_points():

    url = 'https://router-app-api.jdcloud.com/v1/regions/cn-north-1/point:exchange'

    headers={
        # 'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36 (JBOX-APP; Android/3.0.0/51)',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36 (JBOX-APP; Android/3.0.0/51)',
        'Referer': 'http://guanli.luyou.360.cn/new_index.htm',

        # 'Connection': 'close',
        'Connection': 'keep alive',
        'jdmt-rx-sign': '32e62c1ea426c4fd69d73320a7d9efad',
        'jdmt-rx-time': '1638672432476',
        'jdmt-rx-appKey': 'fe2c20725c261e49a80d707a6ab299e1',
        'wskey': 'AAJhgUP3AEAnJrcZNIGgsjSJ_F85JPSY2udsrLkWBbIYG0SXMG_Ucd59rUbPqDEfUDxv5_uqxPtSI3HvUzEvjew9rlmZFAyl',
        'X-MLAAS-AT': 'wl=0',
        'Content-Type': 'application/json',
        'Content-Length': '320',
        'Host': 'router-app-api.jdcloud.com',
        'Accept-Encoding': 'gzip',
        # 'cookie':'abtest=20210928160911055_30; mba_muid=16328165519261007732204; webp=1; shshshfpa=917a5994-b871-d5b1-a37a-a72996c03de4-1632816557; visitkey=42075572647941658; shshshfpb=eoir1NHjb6II6uGq6LwJkHg==; whwswswws=; __jdu=16328165519261007732204; __jdc=122270672; areaId=7; ipLoc-djd=7-538-541-0; wxa_level=1; retina=1; jxsid=16388016404657887987; jcap_dvzw_fp=Hnrt4_gUnHvRMHaeQ8Z4ivWIlsot39Gm3SrU4Qd_GBphf0gOwE5b3LvMDGulWK2NF2lIEQ==; TrackerID=ijLpkEDt9ZztAXgABOphurfnLiF3NTKkmbn1qk1CNneLbsfMdJM7rkJvsjtx3bn4xDNR5JM9WueNHX08GyMTWvjfzu143bgnaUFhNkCCsGk; pt_key=AAJhriEXADAZy4LLvWiYgDpcSub4rmVdYNC3yDbnPxX6zxlNdxX9w14-oizAbkkKqfQel3szsBg; pt_pin=jd_475c36015164f; pt_token=vgaqlsnn; pwdt_id=jd_475c36015164f; sfstoken=tk01md1dd1d44a8sMXgyeDN0ZmRLopKtwKtzAAp25arEYZIoq6DbOLua2E1afNXbT3vCau8HktWb0vcXFsxOpzzmt0a5; PPRD_P=UUID.16328165519261007732204; source_module=; erp=; shareChannel=; share_gpin=; share_open_id=; share_cpin=; sc_width=1707; cid=3; __wga=1638802557590.1638801690310.1632831855158.1632816556407.10.3; jxsid_s_t=1638802557618; jxsid_s_u=https://wqs.jd.com/wxsq_project/portal/m_category/index.shtml; wq_area=7_538_541|1; wqmnx1=MDEyNjM1MnQvam1hc290b192cz9pNzc2MW9hIGROLmkgIGVpNyhMa2NDZTA0U2kuNGY3bjI0MllPT1UhSCU=; autoOpenApp_downCloseDate_jd_homePage=1638802561771_1; __jd_ref_cls=MHome_BIcons; __jdv=122270672|google|AmericaBrandC013|cpc|not set|1638804620473; __jda=122270672.16328165519261007732204.1632816551.1638801640.1638804620.18; shshshfp=336cf18cef0e30ab7b3a0ee78a57acd5; user-key=ca96824e-9c83-4bea-86a2-9630033ac4cd; wlfstk_smdl=s6c8mppw56vku797hk736ng6j4asz90s; TrackID=1DfgrqMT_c8UA69i-XGYuwfjC9CF3iWiTPBvDFIE-fsmgE6qSIGyW9UrSaXRcxH-SdbpJsToZ1NeZaL5aZmZf4pE9urfh6dnYepeIrn6Voe4; thor=68F29D7EA54B30502833381BE9AB536E66FD3B794A6F1B9F45E7E63A45E012D192D779E5C5A049DCE449ABF2BA47CEFD82FA0BA87A281133F4126BAF6CAA642B960322FD5E5503060D72399050A265CF444F686FF0D52D1DE05F2B67E6B67B94C4E7FF566CC6959622765E8FD5F99BA9F9B2EA8E0C4BB1235F97097C556EC236DCA201D82D09E5B0F504269F8493F95ED544F6F3CD26DEB5216258F131FD9305; pinId=LMVpsqOgNOTWvEk9aY-D67V9-x-f3wj7; pin=jd_475c36015164f; unick=jd_187795mwz; ceshi3.com=103; _tp=CplogIhqs/mf/xpddOpKplXsPnoMHq8RhejZy+9djOg=; logining=1; _pst=jd_475c36015164f; __jdb=122270672.4.16328165519261007732204|18.1638804620; shshshsID=557b4679b2c40dbc23c5d9f3d0ad6e99_2_1638804759166; TARGET_UNIT=bjcenter; cn=32; 3AB9D23F7A4B3C9B=IABGRKC6RQXNGXVTIOITU7EN2SOWS6VOQHVMUUDULAJC6OA4ROKZC2ATUMEFTJ6QSXD3YPVHORIY7JOM2KP3Y74JDQ'
        'cookie':'abtest=20210928160911055_30; mba_muid=16328165519261007732204; webp=1; shshshfpa=917a5994-b871-d5b1-a37a-a72996c03de4-1632816557; visitkey=42075572647941658; shshshfpb=eoir1NHjb6II6uGq6LwJkHg==; whwswswws=; __jdu=16328165519261007732204; jcap_dvzw_fp=Hnrt4_gUnHvRMHaeQ8Z4ivWIlsot39Gm3SrU4Qd_GBphf0gOwE5b3LvMDGulWK2NF2lIEQ==; autoOpenApp_downCloseDate_jd_homePage=1638802561771_1; pinId=LMVpsqOgNOTWvEk9aY-D67V9-x-f3wj7; __jdc=122270672; __jda=122270672.16328165519261007732204.1632816551.1639799105.1641658530.20; ipLoc-djd=7-502-0-0; areaId=7; wlfstk_smdl=tk9lzgrsl8tqb80m3c515m13aol4ep38; TrackID=1Vh1JceS3Epl-eptUvGJHNUQ5ayU8dsP4fo_fdoh59BElfOjV4doJ_L2-Zk4nwOIuuDmbgNQSj6HOMEjw5Mb-g_i7oCEvBzzR0JXgQN4OMzk; pin=jd_475c36015164f; unick=jd_187795mwz; ceshi3.com=103; _tp=CplogIhqs/mf/xpddOpKplXsPnoMHq8RhejZy+9djOg=; _pst=jd_475c36015164f; cn=30; user-key=d0528d96-a3cc-43d6-82d4-afdd362deac3; __jdv=122270672|google|AmericaBrandC013|cpc|notset|1641658601708; thor=68F29D7EA54B30502833381BE9AB536E66FD3B794A6F1B9F45E7E63A45E012D1712EAA5FF1219DDE0E547EFCCCAC1F7302C4C0A26B5780B011FCCB8FB8C4DF8D2E1DC37FCB106F4FB07A7C83BDA113A23711E49DFC0968898864FD94D0606C03887D86B723F094E7DCBC9E0901E138C1D669906C732D9D4CC0AFF7505A1F2C75A10C4E64C836649ED793249135ECCBD4BB76F32F51C8458E54F70CB84CB43577; currenttime=1641658690.121; 3AB9D23F7A4B3C9B=IABGRKC6RQXNGXVTIOITU7EN2SOWS6VOQHVMUUDULAJC6OA4ROKZC2ATUMEFTJ6QSXD3YPVHORIY7JOM2KP3Y74JDQ; TrackerID=-nChv8XTpEVHratpu1Sz2uA5YlkLLUjmoBTLgCbTCPd1jrqffmf-VyUiH7QJT5O-VL5Gn18i_hP7UKD3xhux7RsYrWWOl8T6DMg4nI0G0n4; pt_key=AAJh2bnbADD7xps-3vWBIHXf5RJYyWSmtROEeo5mg94uTl4QZdvaHnjLeU0V7ktelRuCYh-YX0w; pt_pin=jd_475c36015164f; pt_token=w0zzjgq9; pwdt_id=jd_475c36015164f; sfstoken=tk01mc33e1b7fa8sMisyKzJ4MSszyFGKhxp7SLvIX+idB6bYFfYpEjXd5SpT3/u/YccVD2TH0m89uVADXgC5JdcSN334; wxa_level=1; retina=1; cid=9; wqmnx1=MDEyNjM2NTplLnl3YT92dTg1OU1hKHcxVyBBZTUgTGVvby40Uy82RjJuLTNRVU8qJkg=; jxsid=16416588443143438849; __jdb=122270672.11.16328165519261007732204|20.1641658530; mba_sid=16416588060192849763649323327.2; sc_width=1707; __wga=1641658844790.1641658844790.1638801690310.1632816556407.1.4; PPRD_P=UUID.16328165519261007732204; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; jxsid_s_t=1641658844827; jxsid_s_u=https://home.m.jd.com/myJd/newhome.action; shshshfp=12ae2ba334bbce838a2e9289eb14f03b; shshshsID=321d29f9d09077a9f5e7ed07f2d2dc99_5_1641658845026'
    }

    key = {
        "pointExchangeReqVo":
            {
                "deviceId":"DCD87C258CB6",

                "exchangeType":1,
                "pointAmount":10,
                # "sign":"To9JAWZ8YHmiyH2HiV6LBrWEImvCKUpUhsb120kvEB0tBtKrDeig7gttEIpKvvrdOmRritP9_MIJ--9nVSx1wbaqADIOT8uyk4Ml7pXE6uhbkbXQ83VAcLN-nhNEeI52b_80iLWmYIz4uCApefz0REOdEv-rzYVoZGvU6yZtYqYRkbBa-eWAYYnjKzle3E81",
                # "sign":"CWN8ddCPA9Lh_3Izvue-Jqy1tBMyLdE5ifuIiMW_E1huNOAubzD1aSrp-blE45-glHPsAQHAibqN6_FYhcSYylz6D5ESKkKuqNG72Vzm34JqRu-3yn1lFItwhdiVTtp03FbrLWm56ZlOtVvkRG8RyOpJi6uHiWLa5nhh1M01uvRbSNsXIBrzB9ISq044lTDd",
                # "sign":"Ur6bFUcsFdkzKaaKa3RtGzDsl2zxUb8EeEzM29M0WtBozp-8TFw2fCXkfZxWpTcHcqcD5naCaHePTDrqa1lo46ns6EgS9Sq7NnFO4hUrYT7bPyuSSwwPuS4WBor5bSXEqMvpONAY1fwBqpHjuk-FSjczl9rRgKUfPANEIVAIj07ZnPLJt4ztHavEl_L-so3W",
                # "sign":"SFV1Qbb53HZLavmVTVaQLpgM9pAo4a5czzIUald0JE1Db18dd9kS0TMTA1t6xV7RqqstFMJFenB4NC_K005vGzCyjDC8bjYYRkK-o6AuacxKtx-_frv1cV5UwQm0rjChun42uKFqeK4W0pfaKv8WvhxVSSR4knegq4_XvN7jCIt6pWC4ceNp1iWXqLH-Q4qd",
                "source":3
            },
        "regionId":"cn-north-1",
    }

    response = requests.post(url=url,headers=headers,json=key)
    print(response.status_code)
    print(response.text)

def get_sign():
    url = 'https://saturn.jd.com/log/sdk HTTP/1.1'

    headers = {
        'Connection': 'Keep-Alive',
        'JD-STD': 'JA2019_3232206',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 10; MI 8 MIUI/V12.5.2.0.QEACNXM)',
        'Host': 'saturn.jd.com',
        'Accept-Encoding': 'gzip',
        'Content-Length': '484',
    }

    key = {
        'R4iSKKKKKKKKKPVIGU7NCLN8s89V5dquJhrV6gVSqKJcOSfcZ9E6TRam3aMg6j'
    }

    response = requests.post(url=url,headers=headers)#,data=key)

    print(response.status_code)
    print(response.text)



def main():
    get_points()
    duihuan_points()
    # get_sign()

if __name__ == '__main__':
    main()
