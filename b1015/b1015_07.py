# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

# stu_1 = "6,홍길자,100,100,100,300,100.0,0"
# key_1 = ["no","name","kor","eng","math","total","avg","rank"]
# sArr = stu_1.split(",") # stu_1 을 리스트형태로 변경
# print(sArr) 

# # 딕셔너리 형태로 바꾸는 방법
# dict_1 = {"no":int(sArr[0]),"name":int(sArr[1])}
# print(dict_1)
# # zip
# dict_list = dict(zip(key_1,stu_1))
# print(dict_list)

# -----------
stu_1 = "6,홍길자,100,100,100,300,100.0,0"
sArr = stu_1.split(",") # stu_1 을 리스트형태로 변경
print(sArr) # ['6', '홍길자', '100', '100', '100', '300', '100.0', '0']

# s = "11"
# print(str.isdigit(s)) # 문자열이 숫자이면 True, 아니면 False # True
# ss = "a"
# print(str.isdigit(ss)) # False


# 문자열을 리스트로 변경하고 타입을 변경하여
for i,s in enumerate(sArr):
  print(type(s))
  if str.isdigit(s): # int로 타입이 변경가능한지?
    sArr[i] = int(s)
sArr[6] = float(sArr[6])

students.append(sArr) # [6, '홍길자', 100, 100, 100, 300, 100.0, 0] 이형태로 students에 추가됨

print(students)

# print(sArr) # [6, '홍길자', 100, 100, 100, 300, 100.0, 0]



