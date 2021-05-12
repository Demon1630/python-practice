from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec






#需要指定 chromedrivr 位置
browser = webdriver.Chrome('C:/Users/Administrator/Desktop/chromedriver_win32/chromedriver')

# browser.get('https://www.strivefysfxyh.com')
browser.get('https:www.jd.com')

input = browser.find_element_by_id('key')

# input = browser.find_element_by_class_name('')

input.send_keys('Python从菜鸟到高手')

input.send_keys(Keys.ENTER)

wait = WebDriverWait(browser,4)

wait.until(ec.presence_of_element_located((By.ID,'J_goodsList')))

print(browser.title)

print('title打印完成')

print(browser.page_source)

browser.close()
