members = []
m_keys = ["id","pw","name","nickName","address","money"]
f = open("b1017/member.csv","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line: break
  # print(line)
  m = line.strip().split(",")
  m[5] = int(m[5])
  members.append(dict(zip(m_keys,m)))
# print(members)
f.close()



flag = 0
mmm = []
# a_id = []


# 아이디 검색
# members의 리스트에서 
# 입력한 문자로 검색된 데이터를 모두 출력 - a가 들어가 있는 아이디 모두 출력
#### 내가 한 것 
# print(members)
# for idx,mm in enumerate(members):
#   # print(mm['id'])
#   if mm['id'].find("b") != -1:
#     a_id.append(mm)
#     flag = 1
#   # else: break # 이거 안해도 됨
# if flag == 0:
#   # print(f"{search}가 포함된 ID가 없습니다.")
#   print("b가 포함된 ID가 없습니다.")
# else:
#   print("총 검색된 인원: ",len(a_id))
#   print(a_id)


# members 리스트출력
while True:
  print("1.회원등록")
  print("2.회원검색")
  choice = input("원하는 번호를 입력하세요. >> ")
  if choice == "1":
    id = input("ID를 입력하세요. >> ")
    flag = 0
    for m in members:
      if m['id'] == id:
        print(f"{id} 는 동일한 아이디가 있습니다. 다시 입력하세요.")
        flag = 1
        break # 여기만 break가 있으면 id 중복은 break가 걸리지만 pw는 묻게됨
    if flag == 1:
      continue # for문 밖으로 나와서 pw 등록으로 넘어가지 말고 처음으로 돌아가기
    else :
      print(f"{id} 는(은) 사용가능합니다.")
      print()
    pw = input("PW를 입력하세요. >> ")
    name = input("이름을 입력하세요. >> ")
    nickName = input("닉네임을 입력하세요. >> ")
    money = int(input("충전금액을 입력하세요. >>"))
    m_list = [id,pw,name,nickName,money]
    members.append(dict(zip(m_keys,m_list)))
    print(f"{id} 님 회원가입이 완료되었습니다.")
    print(m_list)
    # print(members)
  elif choice == "2":
    # 회원 검색 - 선생님이 한 것
    search = input("검색할 회원아이디를 입력하세요. >> ")
    for m in members:
      if m['id'].find(search) != -1:
        print("검색회원을 찾았습니다.")
        mmm.append(m)
        flag = 1 
    if flag == 0:
      print("찾는 회원이 없습니다.")
    else:
      print("총 검색된 인원: ",len(mmm))
      print(mmm)