from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv

# email 발송관련
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

smtpName = "smtp.naver.com"
smtpPort = 587

# 자신의 네이버메일주소, pw, 받는사람이메일주소
sendEmail = "rkwhkehd3927@naver.com"
pw = "MDHHDW1ZDM8R" # 자기거
recvEmail = "rkwhkehd3927@naver.com"
title = "제목 : 파이썬 이메일보내기 안내"
content = "저도 이메일을 보내고 싶습니다."


# 설정
msg = MIMEMultipart()
msg['Subject'] = title
msg['From'] = sendEmail
msg['To'] = recvEmail
msg.attach(MIMEText(content))

# url = "https://news.naver.com/main/ranking/popularDay.naver"
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)
# time.sleep(2)
# soup = BeautifulSoup(browser.page_source,"lxml")
# with open("c1025/news.html","w",encoding="utf-8") as f:
#   f.write(soup.prettify())

with open("c1025/news.html","r",encoding="utf-8") as f:
  soup = BeautifulSoup(f,"lxml")

data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking")
lists = data.select("div.rankingnews_box")
# print(len(lists))

f = open('c1025/news.csv','w',encoding='utf-8-sig',newline='')
writer = csv.writer(f)

for idx, area in enumerate(lists):
  name = area.select_one("strong.rankingnews_name").text.strip()
  titles = area.select("ul > li")
  print(f"{idx+1}. 언론사 : ",name)
  for i, t in enumerate(titles):
    ranking = t.select_one("em").text.strip()
    title = t.select_one("a").text.strip()
    print(f"{ranking}위, ",title)
    n_list = [idx+1,name,ranking,title]
    writer.writerow(n_list)
  print("-"*30)

f.close()



# 파일 첨부
with open("c1025/news.csv","rb") as f:
  attachment = MIMEApplication(f.read())
  attachment.add_header('Content-Disposition','attachment',filename="naverNews.csv")
  msg.attach(attachment)


s = smtplib.SMTP(smtpName,smtpPort)
s.starttls() # 보안인증
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
print("msg : ")
print(msg.as_string)

s.quit()
print("메일 발송 완료")