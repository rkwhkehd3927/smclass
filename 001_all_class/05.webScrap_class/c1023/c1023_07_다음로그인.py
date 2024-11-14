from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random


# 다음 아이디, 패스워드 로그인

url = "http://www.daum.net"

# Chrome
browser = webdriver.Chrome()
# Daum.net
browser.get(url)
# select Sign_in
elem = browser.find_element(By.CLASS_NAME,"btn_login")
# click Sign_in
elem.click()
time.sleep(random.randint(2,5))

# 자바스크립트로 id,pw 호출
id = "dnskem1213@naver.com"
pw = "1111"
input_js = f'document.getElementByid("loginId--1").value = "{id}";\
  document.getElementByid("password--2").value = "{pw}";'
browser.execute_script(input_js)
time.sleep(random.randint(2,5))

# click button for submit 
elem = browser.find_element(By.CLASS_NAME,"btn_g highlight submit")
elem.click()

# 완료
time.sleep(100)