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


# 2.
# 제목, 금액, 평점, 평가수, 찜 정보를 1-5 페이지까지 가져온 후
# 평점 4.8 이상, 평가수 1000명 이상 인 상품을 csv파일로 저장하고 출력하시오.


# html 파일 생성
# browser.switch_to.window(browser.window_handles[1])
browser = webdriver.Chrome()
# browser.maximize_window()
# for i in range(1,6):
#   url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
#   time.sleep(2)
#   browser.get(url)
#   time.sleep(2)
#   pre_height = browser.execute_script("return document.body.scrollHeight")
#   while True:
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(2)
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     if pre_height == curr_height: break
#     pre_height = curr_height
#   time.sleep(3)
#   soup = BeautifulSoup(browser.page_source,"lxml")
#   with open(f"c1025/mouse{i}.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())

# html 파일 읽기
for i in range(1,6):
  with open(f"c1025/mouse{i}.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div")
# adPros = data.select("div.adProduct_item__1zC9h") # 4개
# pros = data.select("div.product_item__MDtDF") # 40개
pros = data.select("div.adProduct_item__1zC9h")+data.select("div.product_item__MDtDF") # 44개
# cl = pros[0]['class']
# print(cl[0]) # adProduct_item__1zC9h

for idx, pro in enumerate(pros):
  if pro['class'][0] == 'adProduct_item__1zC9h':
    title = pro.select_one("div.adProduct_title__amInq").text.strip()
    print(title)
  else : 
    title = pro.select_one("div.product_title__Mmw2K").text.strip()
    print(title)


# for idx, adPro in enumerate(adPros):
#   try:
#     title = adPro.select_one("div.adProduct_title__amInq").text.strip()
#     price = adPro.select_one("span.price_num__S2p_v > em").text.strip().replace(",","")
#     price = int(price.replace(",",""))
#     rating = adPro.select_one("span.product_grade__IzyU3").text.strip().replace("\n","").replace(" ","")[2:]
#     rating = float(rating)
#     r_num = int(adPro.select_one("em.product_num__fafe5").text.strip())
#     zzim = adPro.select_one("span.product_num__fafe5").text.strip()
#     print("제품명 : ",title)
#     print(f"금액 : {price:,} 원")
#     print("평점 : ",rating)
#     print(f"리뷰수 : {r_num} 개")
#     print(f"찜 : {zzim} 개")
#     print("-"*30)
#   except Exception as e:
#     pass


# for idx, area in enumerate(pros):
#   try:
#     title = area.select_one("div.product_title__Mmw2K").text.strip()
#     price = area.select_one("span.price_num__S2p_v > em").text.strip().replace(",","")
#     price = int(price.replace(",",""))
#     rating = area.select_one("span.product_grade__IzyU3").text.strip().replace("\n","").replace(" ","")[2:]
#     rating = float(rating)
#     r_num = int(area.select_one("em.product_num__fafe5").text.strip())
#     zzim = area.select_one("span.product_num__fafe5").text.strip()
#     print("제품명 : ",title)
#     print(f"금액 : {price:,} 원")
#     print("평점 : ",rating)
#     print(f"리뷰수 : {r_num} 개")
#     print(f"찜 : {zzim} 개")
#     print("-"*30)
#   except Exception as e:
#     pass