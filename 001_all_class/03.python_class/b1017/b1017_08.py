import os

members = []
m_title = ["id","pw","name","nickName","address","money"]

#### member.csv 에서 파일읽기 후 members = [] 에 딕셔너리로 저장하기
f = open("b1017/member.csv","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line: break
  # print(line)
  m = line.strip().split(",")
  m[5] = int(m[5])
  members.append(dict(zip(m_title,m)))
# print(members)
f.close()



#### cart.txt 에서 파일읽기 후 member = [] 에 딕셔너리로 저장하기
cartNo = 0 # 구매상품개수(?) # 구매가 될때마다 1 증가 시켜서 cart에 넣을거임
cart = [] # 나중에 번호,아이디,코드만 넣으면 해결되게 할 예정
c_keys = ["cno","id","name","pCode","pName","price","date"]

# if os.path.isfile("b1017/cart.txt"):

if os.path.exists("b1017/cart.txt"):
  f = open("b1017/cart.txt","r",encoding="utf-8")
  while True:
    line = f.readline()
    if not line: break
    cc = line.strip().split(",")
    cc[0] = int(cc[0])
    cc[5] = int(cc[5])
    cart.append(dict(zip(c_keys,cc)))
  # print(cart)
  f.close()

# --------------
product = [
  # {"pno":1,"pCode":"t001","pCode":"삼성TV","price":2000000,"color":"black"},
  # {"pno":2,"pCode":"r001","pName":"LG냉장고","price":3000000,"color":"white"},
  # {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"black"},
  # {"pno":4,"pCode":"l001","pName":"세탁기","price":1000000,"color":"yellow"},
]
session_info = {}
p_title = ["번호","아이디","이름","코드","상품명","가격","구매일자"]

# product.txt 파일을 생성해서 csv형태의 문자열로 저장하시오.
# f = open("b1017/product.txt","w",encoding="utf-8")
# for p in product:
#   f.write(f"{p['pno']},{p['pCode']},{p['pName']},{p['price']},{p['color']}\n")
# f.close()

p_keys = ["pno","pCode","pCode","price","color"]
if os.path.exists("b1017/product.txt"):
  f = open("b1017/product.txt","r",encoding="utf-8")
  while True:
    line = f.readline()
    if not line: break
    p = line.strip().split(",")
    p[0] = int(p[0])
    p[3] = int(p[3])
    product.append(dict(zip(p_keys,p)))
  f.close()



#### 프로그램 시작 ####

while True:
  print("[ 메인 화면 ]")
  print("1. 로그인")
  print("2. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요. >>")
  if choice == "1":
# 프로그램을 구현하시오
    input_id = input("아이디를 입력하세요.")
    input_pw = input("패스워드를 입력하세요.")
    flag = 0
    for m in members:
      if input_id == m['id'] and input_pw == m['pw']:
        print("로그인이 완료되었습니다.")
        session_info = m
        flag = 1
        break
    if flag == 0:
      print("아이디 또는 패스워드가 일치하지 않습니다.")
    else:
      break

    
  elif choice == "2":
# 프로그램을 구현하시오 (이게 맞아....? 미완)
    print("[ 회원가입 정보 입력 ]")
    new_id = input("아이디를 입력하세요. >> ")
    new_pw = input("패스워드를 입력하세요. >> ")
    new_name = input("이름을 입력하세요. >> ")
    new_nickName = input("닉네임을 입력하세요. >> ")
    new_address = input("주소를 입력하세요. >> ")
    new_money = int(input("충전 금액을 입력하세요. >> "))
    new_input = [new_id,new_pw,new_name,new_nickName,new_address,new_money]
    members.append(dict(zip(m_title,new_input)))
    print("회원가입이 완료되었습니다")
    print(f"아이디 : {new_input[0]}, 비밀번호 : {new_input[1]}, 이름 : {new_input[2]}, 닉네임 : {new_input[3]}, 주소 : {new_input[4]}, 충전 금액 : {new_input[5]}")

  elif choice == "0":
    print("프로그램을 종료합니다.")
    break

# 프로그램을 구현하시오
while True:
  print("           [ SM-SHOP ]")
  print(f"                  닉네임 : {session_info['nickName']}님 환영합니다.")
  print(f"                   금액 : {session_info['money']:,} 원")
  print("1. 삼성 TV - 2,000,000")
  print("2. LG 냉장고 - 3,000,000")
  print("3. 하만카돈스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("7. 내용저장")
  print("8. 구매내역")
  print("9. 금액충전")
  choice = int(input("구매하려는 상품번호를 입력하세요. >> "))

# 프로그램을 구현하시오

