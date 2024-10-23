from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

# url = "http://www.naver.com"

# # 페이지 열기
# browser = webdriver.Chrome()
# browser.get(url)
# elem = browser.find_element(By.ID,"query")
# elem.send_keys("네이버 항공권")
# elem.send_keys(Keys.ENTER)

# # 네이버 항공권 클릭
# elem = browser.find_element(By.CLASS_NAME,"link_name").click()
# time.sleep(random.randint(2,5)) # 페이지 열리고 잠시 멈추기

url = "https://flight.naver.com/"

# 페이지 열기
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)

### 출발지
# 출발지 칸 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]').click()
# 출발지 입력
elem = browser.find_element(By.CLASS_NAME,'autocomplete_input__qbYlb').send_keys("김포")
# 출발지 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a').click()

### 도착지
# 도착지 칸 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]').click()
# 도착지 입력
elem = browser.find_element(By.CLASS_NAME,'autocomplete_input__qbYlb').send_keys("제주")
# 도착지 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a').click()

### 날짜 선택
# 가는 날짜 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
# 가는 날짜 선택 
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button').click()
# 오는 날짜 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[1]/div/button[2]').click()
# 오는 날짜 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button').click()

### 탑승 인원
# 탑승 인원 칸 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button').click()
# 인원 추가
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]').click()
# 항공권 검색 버튼 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()

### 데이터 검색 중, 화면 대기
## 1.
# 검색 중
time.sleep(7)
# 화면 대기 함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # 화면 다 나타날때까지 기다리기

## 2.
# 화면에 찾고자 하는 <html> 요소가 있는지 확인 # 최대 120초 동안
# elem = WebDriverWait(browser, 120).until(lambda x: x.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))

# 화면 스크롤 내리기
# 현재 스크롤의 높이 검색
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 : ", prev_height)

# 스크롤 내리기
while True:
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(2) # 스크롤 한번 내리고 다른 정보가 추가될 때까지 대기
  # 높이 확인
  curr_height = browser.execute_script("return document.body.scrollHeight") # 현재 높이
  # print("현재 높이 : ", curr_height)
  if prev_height == curr_height: # 같으면 중지
    break
  prev_height = curr_height
  print("현재 높이 : ", curr_height)
  


# 웹스크래핑으로 데이터 가져오기
# 데이터 가져온 후 처리
# BeautifulSoup 데이터 처리
soup = BeautifulSoup(browser.page_source,"lxml")
with open("c1023/flight.html","w",encoding="utf-8") as f:
  f.write(soup.prettify())

input("enter키를 입력하면 프로그램이 종료됩니다.")
browser.quit()


# 완료
time.sleep(100)
