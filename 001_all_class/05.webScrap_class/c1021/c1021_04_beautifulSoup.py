import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
# print(res.text)

with open("c1021/1.html","w",encoding="utf-8") as f:
  f.write(res.text)

# soup.prettify() 정보 저장
# with open("c1021/2.html","w",encoding="utf8") as f:
  # soup.prettify() : 소스가 정리되어 저장됨
  # f.write(soup.prettify())

print("완료")

# html,css 정보를 가진 소스 변경
soup = BeautifulSoup(res.text,"lxml") # str -> html태그, css태그 사용될 수 있는 형태로 변경

# BeaurifulSoup 사용
# 태그 출력, 태그 글자 출력
# print(soup.title) # title 태그 # <title>랭킹뉴스 : 네이버 뉴스</title>
# print(soup.title.get_text()) # = print(soup.title.text) # title 태그 속 문자열을 출력

# print("없는 태그 : ",soup.titletitletitle) # 없는 태그 입력 시 None 으로 출력
# print("없는 태그 : ",soup.titletitle.get_text()) # Error

# print(soup.a) # 제일 첫번째 a 태그 찾아줌 # <a href="#lnb" tabindex="1"><span>메인 메뉴로 바로가기</span></a>
# print(soup.a.next) # 뒤에 계속 .next 붙일 수 있음 # next : 찾은 태그 바로 다음 태그를 찾아줌
# print(soup.a.attrs) # 태그의 속성값을 가져옴 - 딕셔너리 형태 # {'href': '#lnb', 'tabindex': '1'}
# print(soup.a["href"]) # 태그의 href 속성값을 가져옴

# 특정정보를 출력
print(soup.find("div",attrs={"id":"header"})) #  = print(soup.find("div",{"id":"header"}))
print(soup.find("h2",{"class":"rankingnews_tit"}).text)  # h2 태그 중 class="rankingnews_tit" 출력
print(soup.find_all("div")) # 모든 div 태그 검색 후 출력
print(len(soup.find_all("div"))) # 모든 div 태그 개수 출력
print(type(soup.find_all("div"))) # 모든 div 태그 type 출력 # ResultSet = 객체의 리스트
