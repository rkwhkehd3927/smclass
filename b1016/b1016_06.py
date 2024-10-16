import os

# os.path.exists() : 현재 폴더가 존재하는지 확인
# mkdir : 현재 폴더만 생성
# makedirs : 현재폴더 뿐만아니라 하위폴더까지 생성

if not os.path.exists("c:/ccc/bbb"): # bbb 폴더가 없으면
  print("폴더가 없습니다.")
  # os.mkdir("c:/bbb") # bbb 폴더 생성 명령
  os.makedirs("c:/ccc/bbb") # ccc 폴더 안에 bbb 폴더 생성 명령 (폴더 두개 생성)
else:
  print("폴더가 있습니다.")

f = open("c:/ddd/c.txt","w",encoding="utf-8")
# f = open("c:/aaa/c.txt","w",encoding="utf-8")
# # f = open("c:/bbb/c.txt","w",encoding="utf-8") # 없는 폴더에 억지로 넣으려고하면 에러남
f.write("안녕하세요.")
f.close()