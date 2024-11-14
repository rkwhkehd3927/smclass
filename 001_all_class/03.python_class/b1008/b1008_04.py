# 리스트 타입
# 튜플 타입 - 수정불가
# 딕셔너리 타입


dic1 = {"번호":1,"이름":"홍길동","kor":100,"eng":100} # key:value
# print(dic1)
print(dic1["이름"]) # 출력 방법 - key를 입력하면 value 출력
# print(dic1["합계"]) # 없는 키를 입력하면 에러
dic1["math"] = 90 # 딕셔너리 추가 - 새로운 키를 입력하면 추가됨
dic1['kor'] = 50 # 딕셔너리 수정 - 이미 있는 키의 값을 입력하면 수정됨
del(dic1['eng']) # 딕셔너리 삭제 - del(키) 입력하면 삭제
print(dic1)

# a_list = [1,2,3,"홍길동"]
# print(a_list[0])
# 추가
# append,insert,extend

a_list = [1,"홍길동",100,100,100,300,100.0,1]

print(dic1["이름"])
# print(dic1["학번"]) # get 없이 key만 입력하면 error
# print(dic1.get["이름"])
# print(dic1.get["학번"]) # 존재하지않는 키 입력시 None, 에러는 나지 않음

if dic1.get("이름") != None:
  print(dic1.get("이름"))

print(dic1.keys()) # 모든 key 출력

# type : class 객체
print(type(dic1.keys()))
# class 객체 -> list type 으로 변경
print(dic1.keys())
# print(dic1.keys()[0]) # class 객체 타입이기에 index 값이 없음
list(dic1.keys())
print(list(dic1.keys()))
print(list(dic1.keys())[0])


# 모든 key 출력 - keys()
for key in dic1.keys():
  print(key,dic1[key])

# 값만 출력 - values()
# values() : class 객체 타입
print(dic1.values())
print(list(dic1.values))

# 키, 값을 모두 출력
print(dic1.items())
print(list(dic1.items()))

# 키만 추출
for i in dic1:
  print (key)

# 값만 추출
for key in dic1:
  print(dic1[key])

# 키, 값을 추출
for key,val in dic1.items():
  print(key,val)


# 평균이라는 key가 없을때만 평균(key)을 추가
if '평균' not in dic1:
  dic1['평균'] = 99.0