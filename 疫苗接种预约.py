# -*- coding: UTF-8 ...
import re
import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用
import openpyxl
import wordcloud
import jieba  #分词
import telegram


def get_in():

    url = 'http://one.zju.edu.cn/infoplus/interface/start'

    headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '2084',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'JSESSIONID=21D079E4974B25D613708717AC1167DF.tomcatC; _csrf=S8mwplVi9KWoF2WQ0TlCeCbxlV4gH3xIZevTsWNd67k=; _pv0=1KU3wvuVR2p+hLYc1kzg+VLvagroyLBPBKdMXTqbNbOTuRziuXo/ig2ekIJut0ju/C8JPsG5ZPdreEGE2LE/FFuaCWispeuhOtD56sany8OGD5CCY2WUvMxMvswR7F87SUWxRBkVHvd6TW8qyzG7BssB1iJ+hXw+gMy1hcdes6uhMRbRDXMTSY//KgDRgN8lvJQ35U8i9EO2z4Bj7j9DctThJGvhvzvPsqHx1ePAzLKJ3wDWlppIP01Mjp+QF30bf6KuzScfxz/qKLp3njGu8cizPz4s3wn7nw10KoAEiF0S1NH0pNvrkp1nSGXQsWy4/OkwJ3ksjn2d3Qy2uwwE+YN16OR4P3VnAXPClO4XSGPsqEQHWCWjTXR7zfbOk1T0Y6yR6f7ffM/N6zbvDLH4XOu5XzDosrXHjRUTJRjZekE=; _pf0=hV+ce9T1G+JDMcqj/IEA0wpXfrP/R1YzJQJoVVVyNDw=; _pc0=4wxTRYkh1Mj8bgEFWbRXyJv4fgAYG4ZlXM9hsyhIunY=; iPlanetDirectoryPro=P5tgqKye3THGfSPDvIlAmgHDKA66F8Yt88LpvjHH/P9E10djFD3TCfwbj+caEKip0j9fAhAfJD1Ygt9f8LQUpoG/+q9Lgi975w4sn/rS7rNVw6YF3AIeUrGzkhHduAJ175jJ+hHI1AFesJUh1AsUtz1lHjA4cO1cqO+gdPGlwf5V4mB0FgvGzSCGvBFEvm6auqNw5OSZGix1v9J7K5ngxrSM8kDvmHkCeGYd04UQbGFY60Vu/dQ1vPT2bJrSPZ90138EDgLWu3Z0Nqib45jJ/cbsYLh43/w7Zq+zXXjpZdkhGTFNpI6FMRECbe2w0aeneDt2C22ezLYlf6co8Hk2v3OjLL0jXuNq77OJoKysq+M=; Coremail=8008b3d385a9ad15',
            'DNT': '1',
            'Host': 'one.zju.edu.cn',
            'Origin': 'http://one.zju.edu.cn',
            'Referer': 'http://one.zju.edu.cn/infoplus/form/FW_XGYMJZYY/start?release=true&theme=zju_new&_p=YXM9MiZ0PTUmZD0xMzgmcD0xJmY9MzAmbT1OJg__&_l=&_t=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
    }

    key = {
        'idc': 'FW_XGYMJZYY',
        'release': 'true',
        'csrfToken': 'y4XdQWpK9Qw8Zty2WboWjFca2LvYPUKe',
        'formData':'{"fieldQR":true,"_VAR_ACTION_ACCOUNT":"21860358","_VAR_ACTION_INDEP_ORGANIZES_Codes":"441000","_VAR_ACTION_REALNAME":"胡永军","_VAR_ACTION_INDEP_ORGANIZES_Names":"工程师学院","_VAR_OWNER_ACCOUNT":"21860358","_VAR_ACTION_ORGANIZES_Names":"工程师学院","_VAR_ACTION_ORGANIZE":"441000","_VAR_OWNER_PHONE":"13163292090","_VAR_OWNER_USERCODES":"21860358","_VAR_NOW_DAY":"4","_VAR_ACTION_INDEP_ORGANIZE":"441000","_VAR_OWNER_EMAIL":"1499906118@qq.com","_VAR_OWNER_REALNAME":"胡永军","_VAR_ACTION_INDEP_ORGANIZE_Name":"工程师学院","_VAR_NOW":"1622766302","_VAR_ACTION_ORGANIZE_Name":"工程师学院","_VAR_OWNER_ORGANIZES_Codes":"441000","_VAR_ADDR":"10.190.65.189","_VAR_URL_Attr":"{\"release\":\"true\",\"theme\":\"zju_new\",\"_p\":\"YXM9MiZ0PTUmZD0xMzgmcD0xJmY9MzAmbT1OJg__\"}","_VAR_ENTRY_NUMBER":"-1","_VAR_POSITIONS":"441000:MASTER:21860358","_VAR_ACTION_PHONE":"13163292090","_VAR_OWNER_ORGANIZES_Names":"工程师学院","_VAR_URL":"http://one.zju.edu.cn/infoplus/form/FW_XGYMJZYY/start?release=true&theme=zju_new&_p=YXM9MiZ0PTUmZD0xMzgmcD0xJmY9MzAmbT1OJg__&_l=&_t=","_VAR_RELEASE":"true","_VAR_NOW_MONTH":"6","_VAR_ACTION_USERCODES":"21860358","_VAR_ACTION_EMAIL":"1499906118@qq.com","_VAR_ACTION_ORGANIZES_Codes":"441000","_VAR_NOW_YEAR":"2021","_VAR_ENTRY_NAME":"","_VAR_ENTRY_TAGS":""}',
        'lang': 'zh',
    }

    response=requests.post(url=url,headers=headers,data=key)
    print(response.text)

get_in()
