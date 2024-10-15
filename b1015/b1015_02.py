# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] # 전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 # 성적처리변수

# 학생성적입력 함수선언
def stu_input(stuNo,students):
  while True: # 무한반복
    print("[ 학생성적입력 ]")
    no = stuNo + 1
    name = input(f"{no}번째 학생 이름을 입력하세요.(0. 이전화면 이동)")
    if name == "0":
      print("이전 화면으로 이동합니다.")
      break

    score = [] # 과목수가 많아지면 이런 형태로 써주는게 편함
    total = 0
    for i in range(3):
      k = int(input(f"{s_title[i+2]}점수를 입력하세요. >> ")) # i = 0 / 국어, 영어, 수학
      total += k # 입력되자마자 total에 추가됨
      score.append(k)

    # kor = int(input("국어점수를 입력하세요. >> "))
    # eng = int(input("영어점수를 입력하세요. >> "))
    # math = int(input("수학점수를 입력하세요. >> "))

    # total = score[0]+score[1]+score[2]
    avg = total/3
    rank = 0

    s = {"no":no,"name":name,"kor":score[0],"eng":score[1],"math":score[2],"total":total,"avg":avg,"rank":rank}
    students.append(s)
    stuNo += 1
    print(f"{name} 학생성적이 저장되었습니다.")
    print()

    print(students)
  return stuNo # 값을 돌려받기


#### 실제 프로그램 시작 부분 ####
choice = input("원하는 번호를 입력하세요. >> ")

if choice == "1":
  stuNo = stu_input(stuNo,students) # 전역변수(여기서는 stuNo)를 함수 안쪽으로 가져올수 있는 방법 - 1. 매개변수형태로 넣어주기 2. global # stu_input(매개변수)
  # students 값도 함께 넘겨줄거기 때문에 매개변수에 함께 넣어주기
  # 함수에서 return stuNo 으로 돌려받은 값을 stuNo= 로 다시 넣어줘야 값이 저장됨
  print("현재 학생번호 : ",stuNo) # 기본매개변수라서 함수안에서 return 후 "stuNo = "로 값을 전달해야함
  print(students) # 복합매개변수라서 return 안해도 값이 넘어옴