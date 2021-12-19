# -*- coding: UTF-8 ...
import json

import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome()


from selenium.webdriver.chrome.options import Options

# 实例化一个Options
chrome_options = Options()  # 用于定义下载不弹窗和默认下载地址（默认下载地址还要再后面的commands里启动，默认是不开启的）
# prefs = {"download.default_directory": "E:\download", "download.prompt_for_download": False, }
prefs = {"download.default_directory": "C:\\Users\\demon\\Downloads\\Documents", "download.prompt_for_download": False, }
chrome_options.add_experimental_option("prefs", prefs)
# 无头模式（就是不打开浏览器）
# chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
# params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': "E:\download"}}
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': "C:\\Users\\demon\\Downloads\\Documents"}}
command_result = browser.execute("send_command", params)




#原先的
# options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
# options.add_argument('window-size=1600x900') # 指定浏览器分辨率
# options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
# options.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
# options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
# # options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
#
# # driver = webdriver.Chrome(options=options)#,executable_path='./chromedriver')
driver = webdriver.Chrome(options=chrome_options)#,executable_path='./chromedriver')




def get_cookie():

    url1 = 'https://fsso.cnki.net/'
    driver.get(url1)
    # time.sleep(3)

    school = driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div[2]/input')
    school.send_keys('南开大学')

    enter = driver.find_element_by_xpath('/html/body/form/div[4]/div[1]/div[2]/div[2]')
    get_enter = enter.click()
    # time.sleep(4)

    #填入名称和密码
    name = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[1]/input')
    name.send_keys('1120210985')
    pw = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[2]/input[1]')
    pw.send_keys('Xyh0945')
    #
    log_in = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[5]/button')
    html_get = log_in.click()

    log_in2=driver.find_element_by_xpath('/html/body/form/div/div[2]/p[2]/input[2]')
    get_in=log_in2.click()
    #
    # time.sleep(8)

    #获取cookie
    # c = driver.get_cookies()

    # print(c)
    # print(type(c))
    # print(len(c))
    # for i in c:
    #     print(i)
    #     print(len(i))
    # print(c[5])
    # print(type(c[0]))
    # print(type(eval(c)))
    # return c[5]


    #



def get_doc_byurl(url):
    driver.get(url)
    time.sleep(5)
    # download = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div/div[9]/div[1]/ul/li[4]/a')
    download = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div/div[9]/div[1]/ul/li[4]/a')
    download.click()

def get_doc_bywd(kw):
    url = "https://www.cnki.net/"
    driver.get(url)
    time.sleep(5)
    send_kw=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/input[1]')
    send_kw.send_keys(kw)
    send_kw.send_keys(Keys.ENTER)

    # get_doc = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/form/div/table/tbody/tr[1]/td[2]/a/font')
    get_doc = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/form/div/table/tbody/tr/td[2]/a/font')
    get_doc.click()
    time.sleep(4)
    doc_url=driver.current_url
    get_doc_byurl(doc_url)


"""
    s = requests.Session()
    # 从driver中获取cookie列表（是一个列表，列表的每个元素都是一个字典）
    cookies = driver.get_cookies()
    print(cookies)
    # 把cookies设置到session中
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])

    print(f'当前url是：{driver.current_url}')
    # page_url = driver.current_url
    page_url = 'https://kns.cnki.net/KNS8/Brief/GetGridTableHtml'
    # 获取该页面的HTML
    queryjson='{"Platform":"","DBCode":"SCDB","KuaKuCode":"CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCJD,CCVD,CJFN","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"'+kw+'","Operate":"%=","BlurType":""}],"ChildItems":[]}]}}'
    keywd={
        "IsSearch": "true",
        "QueryJson":queryjson,
        "PageName":"DefaultResult",
        "DBCode":"SCDB",
        "KuaKuCodes":"CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCJD,CCVD,CJFN",
        "CurPage":"1",
        "RecordsCntPerPage":"20",
        "CurDisplayMode":"listmode",
        "CurrSortField":"%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27)",
        "CurrSortFieldType":"desc",
        "IsSentenceSearch":"false",
        "Subject":"",
    }
    resp = s.post(url=page_url,json=keywd)
    print(resp.status_code)
    print(resp.text)
"""




def main():

    cookie = get_cookie()
    while True:
        # i = input("请选择：    1-输入文章链接地址下载      2-输入文章完整名称下载       3-退出:")
        TiShiXinXi = """请输入功能\n
         1.输入文章链接地址下载\n
         2.输入文章完整名称下载\n
         3.退出
         \n
         """
        i = input(TiShiXinXi)
        if i==str(1):
            url = input("请输入文章链接地址")
            get_doc_byurl(url)
            continue
        elif i==str(2):
            kew=input("请输入文章完整名称")
            get_doc_bywd(kew)

            continue
        else:
            driver.quit()
            break


main()




