import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")
sum = 0

# 기준점
data = soup.select_one("#container > div.aside > div > div.aside_area.aside_popular")
print(f"[ {data.select_one("span").text} ]") # 인기 검색 종목

# 인기 검색 종목
print(soup.select_one("h3.h_popular>span")) # <span>인기 검색 종목</span>

# 1-5위

pops = data.select("tbody>tr")
print("개수 : ",len(pops)) # 개수
for pop in pops:
  print("회사 이름 : ",pop.select_one("th>a").text)
  print("현재가 : ",pop.select_one("td").text)
  # 합계를 구하시오
  sum += int(pop.select_one("td").text.replace(",","")) # replace -> , 를 공백으로 대체
  # next_sibling : 형제관계, find_next_sibling : 형제관계 중 검색해서 가져옴
  # print("변동 : ",pop.select_one("td").find_next_sibling("td").text)
  # print("변동1 : ",pop.select_one("td").find_next_sibling("td").select_one("span").text)
  # print("변동액 : ",pop.select_one("td").find_next_sibling("td").select_one("span").next.next.next.strip())
  sps = pop.select_one("td").find_next_sibling("td").select("span")
  tit = ["변동","변동액"]
  for idx,sp in enumerate(sps):
    print(tit[idx],":",sp.text.strip())
  # print("개수 : ",len(sps))
  print("-"*50)

print(f"합계 : {sum:,}")

# -----
# pops_down = data.select("tbody>tr.down")
# pops_up = data.select("tbody>tr.up")
# for p_down in pops_down:
#   print("회사 이름 : ",p_down.select_one("th>a").text)
#   for p_up in pops_up:
#     print("회사 이름 : ",p_up.select_one("th>a").text)
# print("완료")
    