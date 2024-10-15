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

#### 메뉴출력 함수선언
def title_program():
  print("\t\t\t[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
  return choice

#### 학생성적입력 함수선언
def stu_input(stuNo):
  while True:
    print("\t\t\t[ 학생성적 입력 ]")
    no = stuNo +1
    name = input(f"{no}번째 학생 이름을 입력하세요.(0.이전화면) >> ")
    if name == "0":
      print("성적입력을 취소합니다.")
      print()
      break
    kor = int(input("국어성적을 입력하세요. >> "))
    eng = int(input("영어성적을 입력하세요. >> "))
    math = int(input("수학성적을 입력하세요. >> "))
    total = kor+eng+math
    avg = total/3
    rank = 0
    ss = {"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank}
    students.append(ss)
    stuNo += 1
    print(f"{name}학생의 성적을 저장합니다.")
    print()
  return stuNo

#### 학생성적출력 함수선언
def stu_output(students):
  print("\t\t\t[ 학생성적출력 ]")
  print()
  # 상단출력
  for st in s_title:
    print(st,end="\t")
  print(); print("-"*60)
  # 학생성적출력
  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  print()

#### 학생성적수정 함수선언
def stu_update(students):
  print("[ 학생성적 수정 ]")
  name = input("찾고자 하는 학생의 이름을 입력하세요.(0.이전화면) >> ")
  flag = 0
  for s in students:
    if s['name'] == name:
      print(f"{name}학생을 찾았습니다.")
      print()
      print("[ 수정 과목 선택 ]")
      print("1.국어")
      print("2.영어")
      print("3.수학")
      choice = input("원하는 번호를 입력하세요. >> ")
      if choice == "1":
        print(f"이전 국어 점수 : {s['kor']}")
        s['kor'] = int(input("수정할 국어점수를 입력하세요. >> "))
      elif choice == "2":
        print(f"이전 영어 점수 : {s['eng']}")
        s['eng'] = int(input("수정할 영어점수를 입력하세요. >> "))
      elif choice == "3":
        print(f"이전 수학 점수 : {s['math']}")
        s['math'] = int(input("수정할 수학점수를 입력하세요. >> "))
      s['total'] = s['kor']+s['eng']+s['math']
      s['avg'] = s['total']/3
      print(f"{name} 학생 성적이 수정되었습니다.")
      print()
      # 수정된 학생 성적 출력
      for title in s_title:
        print(f"{title}\t",end="")
      print()
      print("-"*60)
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\n")
      print()
      flag = 1
  # 모든 학생 비교가 끝난 후, flag 확인
  if flag == "0":
    print(f"{name} 학생이 없습니다.")
  print()


#### 학생성적검색 함수선언
def stu_select(students):
  while True:
    flag = 0
    print("[ 학생성적 검색 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요.(0.이전화면 이동) >> ")
    if name == "0":
      break
    sArr = []
    for idx, s in enumerate(students):
      if s['name'].find(name) != -1:
        print(f"{idx} 번째, {name} 학생을 찾았습니다." ,s['name'])
        sArr.append(s) 
        flag = 1

    if flag == 0:
      print("찾는 학생이 없습니다.")
    else:
      print(f"{name} 이름으로 {len(sArr)}명의 학생이 검색되었습니다.")
      stu_output(sArr)



while True:
  choice = title_program()
  if choice == "1":
    stuNo = stu_input(stuNo)
  elif choice == "2":
    stu_output(students)
  elif choice == "3":
    stu_update(students)
  elif choice == "4":
    stu_select(students)
    
  elif choice == "5":
    pass
  elif choice == "6":
    pass
