import requests
import re
from bs4 import BeautifulSoup
import time

from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# url = 'https://rvpn.zju.edu.cn/por/service.csp?showsvc=1&autoOpen=1&rnd=khcalfpflkj'
url = 'https://webvpn.nankai.edu.cn/https/77726476706e69737468656265737421e3e44ed22931665b7f01c7a99c406d3635/sso/login?service=https%3A%2F%2Fwebvpn.nankai.edu.cn%2Flogin%3Fcas_login%3Dtrue'


driver.get(url)
time.sleep(5)

sour=driver.find_element(By.CLASS_NAME,'slide_xbox') #获取滑块
ele=driver.find_element(By.CLASS_NAME,'slide_box') #获取整个滑块框

print (ele.size,ele.location['x'])



