# title = ['순위', '종목명', '검색비율', '현재가', '전일비', '등락률', '거래량', '시가', '고가', '저가', 'PER', 'ROE']

# # print(",".join(title)+"\t") # 합치기

# a = ",".join(title)+"\n"
# with open("c1022/a.txt","w",encoding="utf8") as f:
#   f.write(a) # ? 뭐야ㅅㅂ


import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# 순위, 사진링크주소, 제목, 가수명 
# print(soup.select_one("#frm > div > table"))
data = soup.select_one("#frm > div > table")
# print(data.select("tr"))
stocks = data.select("tr")
# print(stocks[0].select("th"))

# 상단 타이틀
tits = stocks[0].select("th")
title = []
# print(len(tits)) # 12
for tit in tits:
  title.append(tit.text.strip())
  # print(tit.text.strip())
print(title)
# ['', '순위', '순위등락', '앨범이미지', '곡 상세가기', '곡정보', '앨범', '좋아요', '듣기', '담기', '다운', '뮤비']
print("-"*80)


# print(stocks[1])

ml_lists = []






