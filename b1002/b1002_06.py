students = [
  [1,'홍길동',100,100,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99]
]

# 이름이 유관순 인것을 출력하시오.

# print(students) # 한번에 모두 출력
# for s in students: # 1개씩 가져와서 출력
#   if s[1] == '유관순':
#     # print("'유관순'이 맞습니다.")
#     print(s)
  # else:
  #   print("'유관순'이 아닙니다.")

# ss = [4,'강감찬',100,90,99]

# students 에 ss를 추가하시오
# students.append(ss)
# print(students)


# 데이터 '이순신' 을 삭제하시오.
# 값을 2개 이상 저장하려면, 주소값을 저장...?

# 삭제 - remove
# for s in students: # [1,'홍길동',100,100,99],[2,'유관순',100,100,99],[3,'이순신',100,100,99]
#   if s[1] == '이순신':
#     # students.remove(s) # remove

# 삭제 - del
for idx,s in enumerate(students):
  if s[1] == '이순신':
    del students[idx] # del

  print(students)