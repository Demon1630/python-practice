from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()


def get_cookie():

    url1 = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421e3e44ed22931665b7f01c7a99c406d3635/sso/login?service=https%3A%2F%2Fwebvpn.nankai.edu.cn%2Flogin%3Fcas_login%3Dtrue'

    driver.get(url1)
    time.sleep(3)

    #填入名称和密码
    name = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/ul/li[2]/input')
    name.send_keys('1120210985')
    pw = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/ul/li[3]/input')
    pw.send_keys('Xyh0945')

    #移动滑块
    action = ActionChains(driver)
    source=driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/ul/li[4]/div/div/div")#需要滑动的元素
    action.click_and_hold(source).perform()  #鼠标左键按下不放
    action.move_by_offset(250,0)#需要滑动的坐标
    action.release().perform() #释放鼠标
    time.sleep(2)

    #登入点击
    log_in = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/ul/li[9]')
    html_get = log_in.click()

    time.sleep(10)



    #获取cookie
    c = driver.get_cookies()

    # print(type(c))
    # print(len(c))

    # print(type(c[1]))
    cookie = c[1]['value']
    # print(cookie)


    url2='https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx'

    # newwindow = 'window.open(https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421fcfe4395247e6651700388a5d6502720c6dba7/clientweb/xcus/ic2/Default.aspx)'
    # driver.execute_script(newwindow)
    # driver.execute_script("window.open();")
    driver.get(url2)

    return cookie

    # for i in c:
    #     print(i)

cookie = get_cookie()



print(type(cookie))
print(cookie)

# driver.quit()


