import requests

# res = requests.get("http://www.google.com")
# res = requests.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")

# User-Agent 크롬 브라우저 정보로 변경하여 전달
url ="http://www.melon.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 정상코드

print("코드상태 : ",res.status_code) # 200

# print(res.text)
# 파일 저장
with open("c1021/b.html","w",encoding="utf-8") as f:
  f.write(res.text)
