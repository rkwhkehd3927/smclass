# flight.html 에 금액이 80000원 이하인 항공권을 출력하시오.
# 김포 -> 제주 80000원 이하 항공권 개수 : 15개
# 제주 -> 김포 80000원 이하 항공권 개수 : 30개

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

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

# 웹스크래핑
# 파일 저장하기
soup = BeautifulSoup(browser.page_source,"lxml")
with open("c1023/flight1.html","w",encoding="utf-8") as f:
  f.write(soup.prettify())

# 파일 불러오기
with open("c1023/flight1.html","r",encoding="utf-8") as f:
  soup = BeautifulSoup(f,'lxml')

data = soup.select_one("#__next > main > div.domestic_flight_content__vYDHd")
lists = data.select("div.domestic_inner__8geIy > div.domestic_Flight__8bR_b")
