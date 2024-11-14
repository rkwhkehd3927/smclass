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
# 창 최대화
browser.maximize_window()
# url 입력
browser.get(url)


# 검색창 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]/div/div').click()
time.sleep(2)
# 키워드 검색
browser.find_element(By.CLASS_NAME,'SearchInput_input__342U2').send_keys("강릉 호텔")
time.sleep(2)

# 날짜 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button').click()
time.sleep(2)
# 가는 날
browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
time.sleep(2)
# 오는 날
browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]').click()
time.sleep(2)
# 확인
browser.find_element(By.CLASS_NAME,'DateRangePicker_rangePickerConfirmButton__2c41H').click()
# Enter
browser.find_element(By.CLASS_NAME,'SearchInput_input__342U2').send_keys(Keys.ENTER)


# 자동시 로딩 대기
# 화면에 호텔검색내용이 다 출력될 때까지, 최대 30초 대기
WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]'))

# 화면을 스크롤해서 내리기 반복
# excute_script() : 자바스크립트 실행함수
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(1)
  # 페이지가 로딩되면서 길어진 길이를 다시 가져옴
  curr_height = browser.execute_script("return document.body.scrollHeight")
  # 페이지를 스크롤하여 길이가 더 길어졌는지 확인
  if prev_height == curr_height:
    break
  # 길이가 길어졌으면, 이전길이에 현재길이를 입력시킴
  prev_height = curr_height

print("스크롤 내리기 완료")


# html 로 파일 저장하기
soup = BeautifulSoup(browser.page_source,"lxml")
with open('c1024/yanolja.html','w',encoding='utf-8') as f :
  f.write(soup.prettify())
# 저장한 파일 읽기(파일 불러와서 soup으로 파싱)
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


print("Enter 를 입력하면 종료됩니다.")
