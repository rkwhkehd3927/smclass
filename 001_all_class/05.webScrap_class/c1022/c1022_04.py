import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

# 내가 해보다가 망한 것
data = soup.select_one("#contentarea > div.box_type_l > table")
# print(data.select("th"))
print(data.select("tr>td"))
print(data.select("tr>td>a")) # 회사명
print(data.select("tr>td>span")) # 전일비, 등락률
