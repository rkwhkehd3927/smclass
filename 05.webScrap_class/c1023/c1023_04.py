# import time
# import random

# print(random.uniform(1,3))

# # a = [0]*100
# # for i in range(100):
# #   a[i] = i

# b = [i for i in range(100)] 
# # # print(b)

# for i in b:
#   print(i)
#   # time.sleep(1) # 1초씩 멈춤
#   time.sleep(random.uniform(1,3)) # 랜덤 1,2,3초씩 멈춤

# 다음 사이트에서 검색창에 주식정보를 입력하여 페이지를 이동하시오.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://www.daum.net")

elem = browser.find_element(By.ID,'q')
# 글자입력
elem.send_keys("주식 정보")
# ENTER 입력
elem.send_keys(Keys.ENTER)

browser.get("http://www.naver.com")
elem = browser.find_element(By.CLASS_NAME,"search_input")
elem.send_keys("주식 정보")
time.sleep(3)
elem.send_keys(Keys.ENTER)



time.sleep(100) # 100초 후에 종료
