# index 는 위치값(공간번호)

# 문자열 슬라이싱
# str = "좋은 하루되세요. 행복이 가득하세요. 매우 감사! 많은 돈!"
# print(len(str))

# # 뒤쪽에서 5번째 자리 까지 출력
# print(str[:-5])
# print(str[-5:])
# print(str[-1])
# print(str[::-1]) # 거꾸로 출력


# list 뒤쪽 추가 - append, 원하는 위치에 추가 - insert
# 위치로 검색해서 삭제 - del, 값으로 검색해서 삭제 - remove
# a_list = [1,2,3]
# # 10추가
# a_list.append(10) # index 마지막에 10 추가
# print(a_list)

# a_list.insert(2,100) # index 2번째 자리에 100 추가
# print(a_list)

# del a_list[1] # index 1번 삭제
# print(a_list)

# a_list.remove(100) # 100이라는 값을 삭제
# print(a_list)


students = [
  [1,'홍길동',100,100,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99]
]

#   번호,이름,국어,영어,수학
s = [4,'강감찬',100,90,99]
# s list에 합계, 평균을 추가 하시오.
print(s[2]) # 국어 점수
s.append(s[2]+s[3]+s[4])
s.append((s[2]+s[3]+s[4])/3)
print(s)

print(students[0][3])
print(len(students))

# 반복문
for i in range(10): # range(10) : 10번 반복실행해라, 0으로 시작해서 반복함
  print(i)

for i in range(2,5): # 2부터 5 앞까지 반복
  print(i)

for i in range(1,10,2): # 1부터 10 전까지 2칸씩 띄워서 출력
  print(i)

aArr = [1,2,3,4,5]
for i in aArr: # list의 값을 1개씩 가져와서 출력
  print(i)

# enumerate() 함수는 주로 반복문에서 사용됨, 몇 번째 반복되고 있는지 확인할 때 사용
for i,data in enumerate(aArr): # list의 값과 index 횟수만큼 출력
  print(i,":",data)                                                                                                                                                                                                                                                                                                                                                                                                              

aStr = "안녕하세요"
for i in aStr : # 문자열의 값을 1개씩 가져와서 출력
  print(i)
