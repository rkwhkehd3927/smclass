from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random

url = "http://www.yanolja.com"
# 브라우저 열기
browser = webdriver.Chrome()

soup = BeautifulSoup(browser.page_source,"lxml")

with open('c1024/yanolja.html','r',encoding='utf-8') as f :
  soup = BeautifulSoup(f,"lxml")

  # 평점이 4.8이상, 금액은 17만원 이하인 것들만 검색하여 아래와 같이 출력하기
# 1. 
# 호텔명 : 
# 평점 : 
# 금액 :
# --------------
# 2.

num = 0
e_num = 0
soldOut = 0
search_list = []
data = soup.select_one("#__next > div > main > section > div.PlaceListBody_listContainer__2qFG1")
lists = data.select("div.PlaceListItemText_container__fUIgA")
for idx, list in enumerate(lists):
  try:
    name = list.select_one("strong.PlaceListTitle_text__2511B").text.strip()
    rating = float(list.select_one("span.PlaceListScore_rating__3Glxf").text.strip())
    price = list.select_one("span.PlacePriceInfoV2_discountPrice__1PuwK").text.strip()
    price = int(price.replace(",",""))
    if rating >= 4.8 and price <= 170000:
      print(f"{idx+1}.")
      print("호텔명 : ",name)
      print("평점 : ",rating)
      print("금액 : ",price)
      print("-"*30)
      num += 1
      search = [idx+1,name,rating,price]
      search_list.append(search)
      
    else: 
      print(f"{idx+1}번 조건에 부합하지 않음")
      e_num += 1
      continue

  except Exception as e:
    print(f"{idx+1}번 예약마감")
    soldOut += 1

print("-"*30)
print("[ 검색 정보 ]")
print(f"조건에 맞는 호텔 : {num} 개")
print(f"조건에 맞지 않는 호텔 : {e_num} 개")
print(f"예약 마감 호텔 : {soldOut}개")

# 평점 역순 정렬
search_list.sort(key=lambda x:x[2],reverse=True)
print("평점 높은 호텔 TOP 3 : ",search_list[:3])

# 금액 순차 정렬
search_list.sort(key=lambda x:x[3])
print("가격 낮은 호텔 TOP 3 : ",search_list[:3])