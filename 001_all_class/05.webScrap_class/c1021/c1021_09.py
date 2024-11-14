import requests
from bs4 import BeautifulSoup
url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text,"lxml")
# print(soup.find("div",{"id":"bestPrdList"}).find("h3").text)

# 제목 출력
# print(soup.find("div",{"id":"bestPrdList"}).find("ul",{"class":"cfix"}))


cfix = soup.find("div",{"id":"bestPrdList"}).find("ul",{"class":"cfix"})
cfixLists = cfix.find_all("li")
print("1-28위 개수 : ", len(cfixLists)) # 28
for i, cfixList in enumerate(cfixLists):
  # print(f"{i+1} : {cfixList.find("div",{"class":"pname"}).p.text}")
  # print(f"{i+1} : {cfixList.find("p").text}")
  p_title = cfixList.find("p").text # cfixList.find("div",{"class":"pname"}).p.text
  p_price = cfixList.find("strong",{"class":"sale_price"}).text
  print(f"{i+1} : {p_title}, 금액 : {p_price} 원")

print("완료")

