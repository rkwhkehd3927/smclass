# sm shop


# members.txt 파일 쓰기
# while True:
#   print("회원정보 입력을 시작합니다.")
#   db_id = input("아이디를 입력하세요.(0. 정지)")
#   if db_id == "0": break
#   db_pw = input("비밀번호를 입력하세요.")
#   db_name = input("이름을 입력하세요.")
#   db_nickName = input("닉네임을 입력하세요.")
#   db_address = input("주소를 입력하세요.")
#   db_money = int(input("가진 금액을 입력하세요."))
#   # csv파일 형태
#   data = f"{db_id},{db_pw},{db_name},{db_nickName},{db_address},{db_money}\n"
#   f = open("members.txt","a",encoding="utf-8")
#   f.write(data)
#   f.close()

p_title = ["번호","아이디","이름","코드","상품명","가격","구매일자"]
choice = 0

# member.txt 에서 파일읽기 후 member = [] 에 딕셔너리로 저장하기
member = []
m_keys = ["id","pw","name","nickName","address","money"]
f = open("members.txt","r",encoding="utf-8") # members.txt 파일 열어서 읽은걸 f에 넣음
while True:
  line = f.readline() # line에 f를 넣음?
  if not line: break 
  m = line.strip().split(",")
  m[5] = int(m[5])
  member.append(dict(zip(m_keys,m)))
print("회원정보", member)
print()
f.close()

# -----------------------
# cart.txt 에서 파일읽기 후 member = [] 에 딕셔너리로 저장하기
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]
f = open("cart.txt","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line: break
  c = line.strip().split(",")
  c[0] = int(c[0])
  c[5] = int(c[5])
  cart.append(dict(zip(c_keys,c)))
# print("구매내역", cart)
f.close()
# -----------------------

while True:
  print("2. 구매내역")
  choice = int(input("구매내역 확인을 원하면 2 를 입력하세요. >>"))
  if choice == "2":
    print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]:15s}\t{p_title[5]}\t{p_title[6]}")
    print("-"*70)
    sum = 0
    for c in cart:
      sum += c['price'] # c=cart 속 구매내역들의 가격만 계속 sum에 넣어서 합치기 
      print(f"{c['cno']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t{c['pName']:15s}\t{c['price']}\t{c['date']}\t")
    print(f"총 구매 금액 : {sum:,}")
    print(f"총 구매 건수 : {len(cart)}")








