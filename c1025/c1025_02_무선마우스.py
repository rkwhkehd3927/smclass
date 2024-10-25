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
# browser = webdriver.Chrome()
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
# 파일 하나만 읽기
# with open("c1025/mouse1.html","r",encoding="utf-8") as f:
#   soup = BeautifulSoup(f,"lxml")

  data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx")
  # lists = data.select("div.product_item__MDtDF")

  # adPros = data.select("div.adProduct_item__1zC9h") # 4개
  # pros = data.select("div.product_item__MDtDF") # 40개
  pros = data.select("div.adProduct_item__1zC9h")+data.select("div.product_item__MDtDF") # 44개
  # cl = pros[0]['class']
  # print(cl[0]) # adProduct_item__1zC9h


  # ★ 광고말고 일반제품 찜수(span)랑 리뷰수(em) 클래스가 같아서 계속 찜수로 불러와짐ㅠㅠ

  f = open('c1025/naver.csv','a',encoding='utf-8-sig')
  writer = csv.writer(f)

  for idx, pro in enumerate(pros):
    try:
      if pro['class'][0] == 'adProduct_item__1zC9h': # 광고
        title =  pro.select_one("div.adProduct_title__amInq").text.strip() # 제품명
        rating = pro.select_one("span.adProduct_rating__PaMzh").text.strip() # 평점
        rating = float(rating)
        r_num = pro.select_one("em.adProduct_count__EDNPm").text.strip().replace(",","") # 리뷰수
        if '만' in r_num:
          r_num = int(r_num)*10000
        else:
          r_num = int(r_num)
        zzim = pro.select_one("span.adProduct_num__t7R1x").text.strip().replace(",","")
      else: # 일반
        title = pro.select_one("div.product_title__Mmw2K").text.strip() # 제품명
        # 엔터(" ")랑 공백(\n), 그리고 글자 "별점" 없애기 -  .replace("\n","").replace(" ","")[2:]
        rating = pro.select_one("span.product_grade__IzyU3").text.strip().replace("\n","").replace(" ","")[2:] # 평점
        rating = float(rating)
        # [1:-2] ()랑 글자 "만" 없애기
        r_num = pro.select_one("em.product_num__fafe5").text.strip().replace("\n","").replace(" ","").replace(",","") # 리뷰수
        if '만' in r_num:
          r_num = int(r_num)*10000
        else:
          r_num = int(r_num)
        zzim = pro.select_one("span.product_etc__LGVaW > span.product_num__fafe5").text.strip().replace(",","")
      price = pro.select_one("span.price_num__S2p_v > em").text.strip()
      price = int(price.replace(",",""))
      if rating >= 4.8 or r_num >= 1000:
        print(f"{idx+1}. 제품명 : ",title)
        print(f"금액 : {price:,} 원")
        print("평점 : ",rating)
        print(f"리뷰수 : {r_num} 개")
        print(f"찜 : {zzim} 개")
        print("-"*30)
      else : 
        print("조건에 부합하지 않음")
      writer.writerow([title,price,rating,r_num,zzim])
    except Exception as e:
      print(f"{idx+1}번째 에러",e)
      print("-"*30)

f.close()