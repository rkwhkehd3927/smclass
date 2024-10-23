import os
import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# 기준점
data = soup.select_one("#contentarea > div.box_type_l > table")
stocks = data.select("tr")
# print(len(stocks)) # 50

# list 생성 방법 1
# sts = stocks[0].select("th") # 그냥 출력하면 text가 안찍히는 형태
# st_list = []
# for st in sts:
#   print(st.text)
#   st_list.append(st.text)
# print(st_list)

#### 1. 상단 타이틀
f = open('c1023/stock.csv','w',encoding='utf-8-sig')
writer = csv.writer(f)
# list 생성 방법 2 (위와 같은방법임)
st_list = [st.text for st in stocks[0].select("th")]
writer.writerow(st_list)
# print(st_list)
# print(len(st_list)) # 상단 타이틀 항목 : 12개

#### 2.
# print(stocks[1].select("td")) # 항목 : 1개
# print(stocks[2].select("td"))
# print(len(stocks[2].select("td"))) # 12 
# sto_list = [sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[2].select("td")]
# sto_list2 = [sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[3].select("td")]
# print(sto_list) # ['2', 'SK하이닉스', '3.81%', '191,700', '상승3,900', '+2.08%', '928,154', '188,500', '192,300', '188,000', '55.86', '-15.61']   


# 30개 주식정보를 csv파일로 저장하시오.
# print(len(stocks)) # 50

for stock in stocks:
  sts = stock.select("td")
  if len(sts) < 1: continue
  sto_list = [st.text.strip().replace("\t","").replace("\n","") for st in sts]
  # print(sto_list)
  writer.writerow(sto_list) # writerow - 리스트타입을 저장
  # with open("c1023/st.csv","w",encoding="utf-8-sig") as f:
  #   writer = csv.writer(f)
  #   writer.writerow(st)
f.close()

print("완료")
  

