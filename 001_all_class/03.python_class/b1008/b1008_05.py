# students = []
# students = {} # 딕셔너리 선언

# 리스트보다는 딕셔너리가 웹으로 전송할 때 표준타입임
# 리스트 안에 딕셔너리의 구조로 넣음

# students['no'] = 1
# students['name'] = input("이름을 입력하세요.")
# students['kor'] = int(input("국어점수를 입력하세요."))
# students['eng'] = int(input("영어점수를 입력하세요."))
# students['math'] = int(input("수학점수를 입력하세요."))
# students['total'] = students['kor']+students['eng']+students['math']
# students['avg'] = students['total']/3
# students['rank'] = 0

# print(students)


students = [] # 리스트
stu = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,
       "total":300,"avg":100.0,"rank":0} # 딕셔너리
stu1 = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,
       "total":300,"avg":100.0,"rank":0} # 딕셔너리

students.append(stu) # 리스트 안에 딕셔너리 넣기
students.append(stu1)

print(students)