# students 리스트 타입
students = [
  {"no":1,"name":"홍길동"},
  {"no":2,"name":"유관순"},
  {"no":3,"name":"이순신"}
]

stuNo = len(students) # 3명

def stu_input(stuNo,students):
  while True:
    # no = len(students)+1
    no = stuNo + 1
    print("no : ",no) # 4
    name = input(f"{no}번째 학생이름을 입력하세요. (0.이전페이지 이동)")
    if name == "0":
      break
    students.append({"no":no,"name":name})
    # print(students)
    stuNo += 1
  return stuNo # while 문 안에 있으면 반복이 안됨

# 학생성적입력 호출
# stu_input(stuNo)
stuNo = stu_input(stuNo,students)
print("stuNo : ",stuNo) # return 이 없으면 값 : 3
print(students)