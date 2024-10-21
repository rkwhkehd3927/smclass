import requests
from bs4 import BeautifulSoup


url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.div["id"]) # div ["id"]의 속성값 찾아오기

# find : 1개 검색
# rankingnews_wrap = soup.find("div",{"class":"rankingnews_box_wrap"})
# find_all : 여러개 검색
# rankingnews_boxs = rankingnews_wrap.find_all("div",{"class":"rankingnews_box"})
# print(len(rankingnews_boxs)) # 12 
# print(soup.find_all("div",{"class":"rankingnews_box"}))


print(soup.title) # 제일 먼저 찾아지는 것을 출력
print(soup.find("title")) # 특정 위치의 태그와 속성 출력 가능
print(soup.find("div",{"class":"rankingnews_box_wrap"}))
newsLists = soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})
print("여러개 개수 확인 : ",len(newsLists)) # 12

for newsList in newsLists:
  print(newsList.find("strong",{"class":"rankingnews_name"}))