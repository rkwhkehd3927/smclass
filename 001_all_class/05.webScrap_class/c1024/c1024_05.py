from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options
import pyautogui

url = "https://new.land.naver.com/complexes?ms=37.4592802,126.8930386,17&a=APT:PRE:ABYG:JGC&e=RETAIL"

browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# pyautogui.moveTo(1270,550)
# time.sleep(1)
# pyautogui.moveTo(1270,480)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(200,800)
# time.sleep(1)
# prev_height = browser.execute_script("return articleListArea.scrollHeight")
# print("화면 높이 : ",prev_height)
# while True:
#   # browser.execute_script("window.scroll(0,articleListArea.scrollHeight)")
#   pyautogui.scroll(-prev_height)
#   time.sleep(2)
#   curr_height = browser.execute_script("return articleListArea.scrollHeight")
#   if prev_height == curr_height: break
#   prev_height = curr_height
#   print("높이 : ",prev_height)

# print("-"*50)
# all_height = browser.execute_script("return document.body.scrollHeight")
# print("화면 전체 높이 : ",all_height)

soup = BeautifulSoup(browser.page_source,"lxml")
# with open("c1024/naver.html","w",encoding="utf-8") as f:
#   f.write(soup.prettify())
with open("c1024/naver.html","r",encoding="utf-8") as f:
  soup = BeautifulSoup(f,"lxml")

# 매매 가격이 낮은 5개, 전세가격이 낮은 5개를 출력하시오.


data = soup.select_one("#articleListArea")
lists = data.select("div.false")
list1 = 0 # 매매
list2 = 0 # 전세
search_list1 = [] # 매매
search_list2 = [] # 전세
for idx, area in enumerate(lists):

  name = area.select_one("div.item_title").text.strip()
  hType = area.select_one("span.type").text.strip()
  # 가격 - 문자열
  price = area.select_one("span.price").text.strip()
  # price = int(price.replace("억","00000000"))

  if hType == "매매":
    print("[ 매매 아파트 ]")
    print(f"{idx+1}번째 아파트 : ",name)
    print(hType, price)
    list1 += 1
    search1 = [idx+1,name,hType,price]
    search_list1.append(search1)
  elif hType == "전세": 
    print("[ 전세 아파트 ]")
    print(f"{idx+1}번째 아파트 : ",name)
    print(hType, price)
    list2 += 1
    search2 = [idx+1,name,hType,price]
    search_list2.append(search2)
  else: 
    print("월세 제외")
    
      


print("-"*30)
print("[ 검색 정보 ]")
print(f"매매 아파트 : {list1} 채")
print(f"전세 아파트 : {list2} 채")

# 매매 낮은 순
search_list1.sort(key=lambda x:x[3])
print("매매가 낮은 순 TOP 5 : ",search_list1[:5])

# 전세 낮은 순
search_list2.sort(key=lambda x:x[3])
print("매매가 낮은 순 TOP 5 : ",search_list2[:5])



input("엔터키 입력완료")

