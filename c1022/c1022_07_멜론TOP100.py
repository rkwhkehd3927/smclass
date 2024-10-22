import os
import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

# 1. 기준점
data = soup.select_one("#frm > div > table")
lists = data.select("tr")
print("개수 : ",len(lists)) # 101

# lists[0] : 상단타이틀
# print(lists[0].select("th"))
title = []
tits = lists[0].select("th")
for tit in tits:
  title.append(tit.text.strip())
  # print(tit.text.strip())
# print(title)
# ['', '순위', '순위등락', '앨범이미지', '곡 상세가기', '곡정보', '앨범', '좋아요', '듣기', '담기', '다운', '뮤비']

# 1-100위 순위 출력
for i in range(1,3):
  if not os.path.exists("c1022/melon"): # 폴더 존재하는지 확인하고
    # print("존재하지 않습니다.")
    os.makedirs("c1022/melon") # 폴더 만들기
 
  with open(f"c1022/melon/{i}.jpg","wb") as f:
    lis = lists[i].select("td")
    # print("개수 : ",len(lis)) # 12
    # print(lis[0]) # 곡선택
    print("순위 : ",lis[1].select_one("span").text) # 순위
    print("앨범 이미지 : ",lis[3].select_one("img")["src"]) # 이미지 링크
    img = requests.get(lis[3].select_one("img")["src"])
    f.write(img.content)
    songs = lis[5].select("div.ellipsis")
    # print(len(songs)) # 2
    # singer = songs[1].select_one("a")
    print("제목 : ",songs[0].select_one("span").text.strip(),end="\n")
    singers = songs[1].select("a")
    if len(singers) != 4:
    # if singers[0].text == singers[1].text:
      print("가수 : ",singers[0].text)
    else:
      print("가수 : ",singers[0].text+","+singers[1].text)
      
          # 로제만 브루노마스도 같이 출력하기 ㅠ (내가 하다 망한 것)
          # if singer.next.next.next.text == "":
          #   print(songs[0].select_one("a").text+singer.text)
          # else:
          #   print(songs[0].select_one("a").text+singer.text+singer.next.next.next.text)
            # print(songs[1].select_one("a").next.next.next.text) # bruno mars
    # for song in songs:
    #   print("곡 정보 : ",song.select_one("a").text)
    
    print("-"*50)

      


