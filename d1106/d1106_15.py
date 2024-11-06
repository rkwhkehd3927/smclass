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
  # print(len(areas))


  for idx, area in enumerate(areas):
    try:
      title = area.select_one("div.item-title > c-title > strong > a").text.strip()
      people = area.select_one("c-doc > div > div.item-bundle-mid > div.item-contents > c-contents-desc > p > a").text.strip().replace("\n","").replace(" ","")[2:]
      if '만명' in people:
        people = int(people)*10000
      else:
        people 
      mdate = "."

      print("영화 제목: ",title)
      print("누적 관객수: ",people)

    except Exception as e:
      print(f"{idx+1}번째 에러",e)
      print("-"*30)