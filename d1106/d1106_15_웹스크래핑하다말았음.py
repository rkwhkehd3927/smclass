# [영화 순위] = 웹스크래핑
# 2020~2023년 영화내용 저장
# -csv 파일로 저장
# -이미지 저장
# -제목,
# -관객수: 숫자 입력
# 1,312 -> 1312
# -날짜

# DataFrame 변경
# 관객수
# -> 최대값
# -> 최소값
# -> 평균
# -> 최대관객수 5개
# -> 최소관객수 5개 출력

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
from selenium.webdriver.chrome.options import Options
import pyautogui

# html 파일 생성
# browser = webdriver.Chrome()
# browser.maximize_window()
# for i in range(4):
#   url = f"https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=202{i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
#   time.sleep(2)
#   browser.get(url)
#   time.sleep(2)
#   soup = BeautifulSoup(browser.page_source,"lxml")
#   with open(f"d1106/movie{i}.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())

# html 파일 읽기
for i in range(4):
  with open(f"d1106/movie{i}.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

  data = soup.select_one("#mor_history_id_0 > div > div.flipsnap_view > div > div.flipsnap_item")
  areas = data.select("c-flicking-item > c-layout > div > c-list-doc > ul > li")
  # print(len(areas)) # 개수를 한번 체크해보고 다음으로 넘어갈 것


  for idx, area in enumerate(areas):
    try:
      title = area.select_one("div.item-title > c-title > strong > a").text.strip()
      people = int(area.select_one("c-doc > div > div.item-bundle-mid > div.item-contents > c-contents-desc > p > a").text.strip()[3:-1].replace(",",""))
      # if '만' in people:
      #   people = people*10000
      # else:
      #   people
      mdate = area.select_one("c-doc > div > div.item-bundle-mid > div.item-contents > c-contents-desc-sub > span").text.strip()[:-1]

      print("영화 제목: ",title)
      print("누적 관객수: ",people)
      print("날짜: ",mdate)

    except Exception as e:
      print(f"{idx+1}번째 에러",e)
      print("-"*30)
      