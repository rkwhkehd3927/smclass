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

# selenium 화면을 숨김처리
options = Options()
options.add_argument("--headless") # 숨김
options.add_argument("--window-size=1920,1080") # 숨겼지만 크기는 1920 x 1080
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")

# -------------- 

# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
# browser = webdriver.Chrome(options=options)
# browser.maximize_window()
# browser.get(url)

# soup = BeautifulSoup(browser.page_source,"lxml")
# data = soup.select_one("#detected_value").text
# print("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
# print("-"*50)
# print(data)
# browser.get_screenshot_as_file("gmarket.png") # 숨겨진 화면을 캡쳐해서 저장
# input("엔터키 입력완료 >> ")


for i in range(3):
  url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i+1}"
  # 브라우저 열기
  browser = webdriver.Chrome(options=options)
  # 창 최대화
  browser.maximize_window()
  # url 입력
  browser.get(url)
  time.sleep(3)

  # html 로 파일 저장하기
  soup = BeautifulSoup(browser.page_source,"lxml")
  browser.get_screenshot_as_file(f"c1024/gmarket{i+1}.png") # 숨겨진 화면을 캡처해서 저장

  with open(f'c1024/gmarket{i+1}.html','w',encoding='utf-8') as f :
    f.write(soup.prettify())
print("완료")

# # 파일 불러오기
# for i in range(3):  
#   # 저장한 파일 읽기(파일 불러와서 soup으로 파싱)
#   with open(f'c1024/gmarket{i+1}.html','r',encoding='utf-8') as f :
#     soup = BeautifulSoup(f,"lxml")

