import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains



#需要指定 chromedrivr 位置
browser = webdriver.Chrome('C:/Users/Administrator/Desktop/chromedriver_win32/chromedriver')

# browser.get('https://www.google.com')
browser.get('https://www.strivefysfxyh.com/')

actions = ActionChains(browser)

# li_list = browser.find_element_by_tag_name('li')
li_l = browser.find_element_by_class_name('nav-header')
li_list =li_l.find_elements_by_class_name('sub-menu')

print(li_l.text)

print(li_list[0].text)

actions.move_to_element(li_l).perform()
time.sleep(8)

# for li in li_list:
#     actions.move_to_element(li).perform()
#     time.sleep(2)
browser.close()




# input = browser.find_element_by_class_name('gLFyf gsfi')
# input = browser.find_element_by_name('q')
# input = browser.find_element_by_id("searchform")

# input = browser.find_element_by_css_selector(".search-form")

# print(len(input.text))

# input = browser.find_elements_by_class_name('search-form')


# input = browser.find_element_by_id('search')
# input.send_keys('Python从菜鸟到高手')

# input.send_keys(Keys.ENTER)