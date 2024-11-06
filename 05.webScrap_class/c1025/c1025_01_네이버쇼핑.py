from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
from selenium.webdriver.chrome.options import Options
import pyautogui

# 1.
# https://www.naver.com/
# 네이버 쇼핑 검색창 입력 enter
# 네이버 쇼핑 클릭 -> 검색창에 '무선마우스' 입력. enter

# 네이버 열기
# url = "https://www.naver.com"
browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# 네이버 검색창에 '무선마우스' 검색 -> 네이버 쇼핑 클릭
# browser.find_element(By.XPATH,'//*[@id="query"]').click()
# time.sleep(2)
# browser.find_element(By.XPATH,'//*[@id="query"]').send_keys("무선마우스")
# time.sleep(2)
# browser.find_element(By.XPATH,'//*[@id="query"]').send_keys(Keys.ENTER)
# time.sleep(2)
# browser.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a').click()
# time.sleep(2)

