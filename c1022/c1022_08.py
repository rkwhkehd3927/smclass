import os
import requests
from bs4 import BeautifulSoup
url = "http://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# 링크주소,이미지주소,제목,금액,평점,평가수
# 기준점
# print(soup.select_one("#productList"))
data = soup.select_one("#productList")
# print(data.select_one("ul"))
lists = data.select("li")
# print(len(stocks)) # 개수 : 60


n_lists = []

#### 금액 : 90만원 이상, 평점 4.5 이상, 평가수 100명 이상 
for idx, list in enumerate(lists):
  n_list = [] # 제목,금액,평점,평가수,링크,이미지
  try:
    # price,rating,num 타입 변경
    link = list.select_one("a")["href"]
    name = list.select_one("div.name").text
    price = int(list.select_one("strong.price-value").text.replace(",","")) # 정수형으로 바꾸기
    rating = float((list.select_one("em.rating")).text) # 실수형으로 바꾸기
    num = int(list.select_one("span.rating-total-count").text[1:-1]) # text[1:-1] = 앞뒤 괄호 떼기
    img = list.select_one("img")["src"]
    # 금액,평점,평가수 비교
    if price >= 900000 and rating >= 4.5 and num >= 100: 
      print(f"[ {idx}번째 ]")
      print("1. 제품 링크 : http://www.coupang.com"+link)
      print("2. 제품 이름 : ",name)
      print("3. 가격 : ",price)
      print("4. 평점 : ",rating)
      # print("평가수 : ",lists[0].select_one("span.rating-totla-count").text) # (000) - 평점에 괄호 붙어있음
      print("5. 평가수 : ",num)
      print("6. 이미지 링크 : http:"+img)
      n_list = ["http://www.coupang.com"+link,name,price,rating,num,"http:"+img]
      n_lists.append(n_list)
    else:
      print(f"{idx}번째 : 제외")
  except Exception as e:
    print(f"{idx}번째: 에러 ",e)
    if idx == 59:
        break
print(n_lists)

while True:
  print()
  print("-"*50)
  print("[ 정렬하기 ]")
  print("1. 금액 순차 정렬")
  print("2. 금액 역순 정렬")
  print("3. 평점 순차 정렬")
  print("4. 평점 역순 정렬")
  print("0. 종료")
  choice = int(input("원하는 번호를 입력하세요. >> "))

# 뭔가 이상하다 ㅋㅎㅋ
  if choice == 1:
    print("[ 금액 순차 정렬 ]")
    # for n in n_lists:
    n_lists.sort(key=lambda x:x[2]) # 왜 순차정렬이 안도 ㅐ ....?
    print(n_lists)
  elif choice == 2:
    n_lists.sort(key=lambda x:x[2],reverse=True)
    print(n_lists)
  elif choice == 3:
    pass
  elif choice == 4:
    pass
  elif choice == 0:
    break
