# -*- coding: UTF-8 ...
import re
import requests
from bs4 import BeautifulSoup
from  fake_useragent import UserAgent
import os
import telegram


def get_in(time_avable):

    url = 'http://one.zju.edu.cn/infoplus/interface/doAction'

    headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '4691',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'JSESSIONID=21D079E4974B25D613708717AC1167DF.tomcatC; _csrf=S8mwplVi9KWoF2WQ0TlCeCbxlV4gH3xIZevTsWNd67k=; _pv0=1KU3wvuVR2p+hLYc1kzg+VLvagroyLBPBKdMXTqbNbOTuRziuXo/ig2ekIJut0ju/C8JPsG5ZPdreEGE2LE/FFuaCWispeuhOtD56sany8OGD5CCY2WUvMxMvswR7F87SUWxRBkVHvd6TW8qyzG7BssB1iJ+hXw+gMy1hcdes6uhMRbRDXMTSY//KgDRgN8lvJQ35U8i9EO2z4Bj7j9DctThJGvhvzvPsqHx1ePAzLKJ3wDWlppIP01Mjp+QF30bf6KuzScfxz/qKLp3njGu8cizPz4s3wn7nw10KoAEiF0S1NH0pNvrkp1nSGXQsWy4/OkwJ3ksjn2d3Qy2uwwE+YN16OR4P3VnAXPClO4XSGPsqEQHWCWjTXR7zfbOk1T0Y6yR6f7ffM/N6zbvDLH4XOu5XzDosrXHjRUTJRjZekE=; _pf0=hV+ce9T1G+JDMcqj/IEA0wpXfrP/R1YzJQJoVVVyNDw=; _pc0=4wxTRYkh1Mj8bgEFWbRXyJv4fgAYG4ZlXM9hsyhIunY=; iPlanetDirectoryPro=P5tgqKye3THGfSPDvIlAmgHDKA66F8Yt88LpvjHH/P9E10djFD3TCfwbj+caEKip0j9fAhAfJD1Ygt9f8LQUpoG/+q9Lgi975w4sn/rS7rNVw6YF3AIeUrGzkhHduAJ175jJ+hHI1AFesJUh1AsUtz1lHjA4cO1cqO+gdPGlwf5V4mB0FgvGzSCGvBFEvm6auqNw5OSZGix1v9J7K5ngxrSM8kDvmHkCeGYd04UQbGFY60Vu/dQ1vPT2bJrSPZ90138EDgLWu3Z0Nqib45jJ/cbsYLh43/w7Zq+zXXjpZdkhGTFNpI6FMRECbe2w0aeneDt2C22ezLYlf6co8Hk2v3OjLL0jXuNq77OJoKysq+M=; Coremail=8008b3d385a9ad15',
            'DNT': '1',
            'Host': 'one.zju.edu.cn',
            'Origin': 'http://one.zju.edu.cn',
            'Referer': 'http://one.zju.edu.cn/infoplus/form/4823134/render',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
    }

    key = {
        'actionId': '10',
        'csrfToken': 'y4XdQWpK9Qw8Zty2WboWjFca2LvYPUKe',
        'formData':time_avable,
        'remark':'',
        'rand': '505.0304264936361',
        'nextUsers': '{}',
        'stepId': '4823134',
        'timestamp': '1622766024',
        'boundFields':'fieldDQZT,fieldYYRQPid,fieldZJHM,fieldXM,fieldSQTJSJ,fieldGH,fieldQR,fieldYYRQ,fieldFZWCJZ,fieldFZYYJG,fieldSQBH,fieldDBLJ,fieldDYZYMPC,fieldFSYJ,fieldJZD,fieldYYSJ,fieldYYSJPid,fieldSZDW,fieldSJHM,fieldSQRQ',
        'csrfToken': 'y4XdQWpK9Qw8Zty2WboWjFca2LvYPUKe',
        'lang': 'zh',
    }

    response=requests.post(url=url,headers=headers,data=key)
    # print(type(eval(response.text)))
    dic = eval(response.text)
    ecode = dic['ecode']
    eror = dic['error']
    # print(response.text)
    return ecode,eror


# info = get_in(time_avable)
# print(info)
# # print(type(info))
# print(info[0])

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
        'title':'通知',
        'desp':text,
    }
    response = requests.post(url=url,headers=headers,data=key)
    # print(response)



def main():
    time_avable = '{"_VAR_EXECUTE_INDEP_ORGANIZE_Name":"工程师学院","_VAR_ACTION_ACCOUNT":"21860358","_VAR_ACTION_INDEP_ORGANIZES_Codes":"441000","_VAR_ACTION_REALNAME":"胡永军","_VAR_ACTION_INDEP_ORGANIZES_Names":"工程师学院","_VAR_OWNER_ACCOUNT":"21860358","_VAR_ACTION_ORGANIZES_Names":"工程师学院","_VAR_STEP_CODE":"YY","_VAR_ACTION_ORGANIZE":"441000","_VAR_OWNER_PHONE":"13163292090","_VAR_OWNER_USERCODES":"21860358","_VAR_EXECUTE_ORGANIZE":"441000","_VAR_EXECUTE_ORGANIZES_Codes":"441000","_VAR_NOW_DAY":"4","_VAR_ACTION_INDEP_ORGANIZE":"441000","_VAR_OWNER_EMAIL":"1499906118@qq.com","_VAR_OWNER_REALNAME":"胡永军","_VAR_ENTRY_TAGS":"09-医保计生","_VAR_ACTION_INDEP_ORGANIZE_Name":"工程师学院","_VAR_NOW":"1622766303","_VAR_PARTICIPANTS":",21860358,","_VAR_ACTION_ORGANIZE_Name":"工程师学院","_VAR_EXECUTE_ORGANIZES_Names":"工程师学院","_VAR_OWNER_ORGANIZES_Codes":"441000","_VAR_ADDR":"10.190.65.189","_VAR_URL_Attr":"{\\"release\\":\\"true\\",\\"theme\\":\\"zju_new\\"}","_VAR_ENTRY_NUMBER":"1843722","_VAR_EXECUTE_INDEP_ORGANIZES_Names":"工程师学院","_VAR_ENTRY_NAME":"新冠疫苗接种预约","_VAR_STEP_NUMBER":"4823134","_VAR_POSITIONS":"441000:MASTER:21860358","_VAR_ACTION_PHONE":"13163292090","_VAR_OWNER_ORGANIZES_Names":"工程师学院","_VAR_URL":"http://one.zju.edu.cn/infoplus/form/4823134/render","_VAR_EXECUTE_ORGANIZE_Name":"工程师学院","_VAR_EXECUTE_INDEP_ORGANIZES_Codes":"441000","_VAR_RELEASE":"true","_VAR_EXECUTE_POSITIONS":"441000:MASTER:21860358","_VAR_NOW_MONTH":"6","_VAR_ACTION_USERCODES":"21860358","_VAR_ACTION_EMAIL":"1499906118@qq.com","_VAR_ACTION_ORGANIZES_Codes":"441000","_VAR_EXECUTE_INDEP_ORGANIZE":"441000","_VAR_NOW_YEAR":"2021","fieldFZYYJG":"","fieldFZWCJZ":"","fieldSQBH":"1843722","fieldSQRQ":1622736000,"fieldXM":"21860358","fieldXM_Name":"胡永军","fieldGH":"21860358","fieldSZDW":"441000","fieldSZDW_Name":"工程师学院","fieldSJHM":"13163292090","fieldZJHM":"362227199607274119","fieldDQZT":"2","fieldDQZT_Name":"已接种第一针","fieldDYZYMPC":"02","fieldDYZYMPC_Name":"北京生物","fieldYYSJPid":"玉泉校区邵体馆,2021-06-04","fieldJZD":"玉泉校区邵体馆","fieldJZD_Name":"玉泉校区邵体馆","fieldYYRQPid":"玉泉校区邵体馆","fieldYYRQ":"2021-06-04","fieldYYRQ_Name":"2021-06-04","fieldYYRQ_Attr":"{\\"_parent\\":\\"玉泉校区邵体馆\\"}","fieldYYSJ":"11:00~12:00","fieldYYSJ_Name":"11:00~12:00","fieldYYSJ_Attr":"{\\"_parent\\":\\"玉泉校区邵体馆,2021-06-04\\"}","fieldQR":true,"fieldFSYJ":"","fieldDBLJ":"","fieldSQTJSJ":""}'

    # print(time_avable)
    day = 4
    while day<=15:
        new_day = '2021-06-'+str(day).zfill(2)
        time_avable = time_avable.replace('2021-06-04',new_day)
        t = 10
        while t < 18:
            t += 1
            new_t = str(t) + ':00' + '~' + str(t + 1) + ':00'
            new_time = time_avable.replace('11:00~12:00', new_t)
            # print(new_time)
            info = get_in(new_time)
            # print(info)
            if info[0] != 'EVENT_CANCELLED':
                # break
                print(f'{new_day}  {new_t} 时间可以预约了,快去查看预约结果')
                send_telegram(f'{new_day}  {new_t} 时间可以预约了,快去查看预约结果')
                send_wechat(f'{new_day}  {new_t} 时间可以预约了,快去查看预约结果')
                return
            else:
                if day == 15 and t == 18:
                    send_telegram('到15号仍然都不可预约')
                    send_wechat('到15号仍然都不可预约')
                print(f'{new_day}  {new_t}  {str(info)}')
                # send_telegram(f'{new_day}  {new_t}  {str(info)}')
                # send_wechat(f'{new_day}  {new_t}  {str(info)}')

        day += 1


if __name__ == '__main__':
    try:
        main()
    except:
        send_telegram('出错了')
        send_wechat('出错了')



