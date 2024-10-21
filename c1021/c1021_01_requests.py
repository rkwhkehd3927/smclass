import requests
# res = requests.get("https://www.google.com") # html 소스 가져오기
res = requests.get("https://www.naver.com") # html 소스 가져오기
# res = requests.get("https://www.melon.com/index.htm") # html 소스 가져오기
res.raise_for_status() # 에러시 종료


# print(res.text) # html 소스 출력
# if res.status_code == 200:
#   print(res.text)
# else:
#   print("접근할 수 없습니다.")
# print("응답코드 : ",res.status_code) # 200 # 406
# print(res.text)

### 웹소스코드 파일 저장
# f = open("a.html","w",encoding="utf-8")
# f.write(res.text)
# f.close()

# f.close() 안써도 되는 방식
# with open("c1021/a.html","w",encoding="utf-8") as f:
#   f.write(res.text)

print("총 문자 길이 : ", len(res.text))

# requests 로 정보를 가져올 시 제이쿼리,자바스크립트,외부페이지,reack,vue... 등은 못 가져옴
                              # ↑ 비공기식으로 작동되는 소스는 가져오지 못함