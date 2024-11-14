
# 
# 학생성적 입력부분을 구현하시오.
# dict 타입으로 입력을 할 것
# 번호,이름,국어,영어,수학,합계,평균,등수
# 입력이 안료되면 출력이 바로 되도록 하시오.


# students 리스트 타입
students = [ 
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
no = len(students)+1
choice = 0  # 전역변수
stuNo = 0   # 학생번호 생성 
chk = 0     # 체크변수
count = 1   # 성적처리
stuNo = len(students) # 추후에 리스트에 학생이 생기면, 그 인원수로 변경시켜줘야함
no = 0; name=""; kor=0; eng=0; math=0; total=0; avg=0; rank=0 # 성적처리변수 # 함수처리 할거라서 미리 선언



# 학생성적프로그램
while True:
  print("[ 학생성적프로그램 ]")
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

  if choice == "1":
    while True:
      print("[ 학생성적 입력 ]")
      # 학생성적 직접 입력
      no = stuNo + 1 # 리스트 - 학생수
      name = input(f"{no}번째 학생 이름을 입력하세요.(0.이전화면) >>") 
      if name == "0":
        print("성적입력을 취소합니다.")
        print()
        break
      kor = int(input("국어점수를 입력하세요."))
      eng = int(input("영어점수를 입력하세요."))
      math = int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      s = [no,name,kor,eng,math,total,avg,rank] # s: list 타입
      students.append(s) # 리스트에 추가
      stuNo += 1 # 학생수 1 증가
      print(f"{name} 학생의 성적이 저장되었습니다.")
      print()


  elif choice == "2":
    print("[ 학생성적 출력]")
    print
    # 상단 타이틀 출력
    for title in s_title:
      print(f"{title}",end='\t')
    print()
    print("-" * 60)
    # print(f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}\t")
    
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
    print()
    
  elif choice == "7":
    while True:
      print("[ 학생성적 정렬 ]")
      print("1. 이름으로 순차정렬")
      print("2. 이름으로 역순정렬")
      print("3. 합계 순차정렬")
      print("4. 합계 역순정렬")
      print("5. 번호 순차정렬")
      print("0. 이전페이지 이동")
      print("-"*40)
      choice = input("원하는 번호를 입력하세요.>> ")

      if choice == "1":
        print("[ 이름으로 순차정렬 ]")
        students.sort(key=lambda x:x['name'])
      elif choice == "2":
        print("이름으로 역순정렬")
        students.sort(key=lambda x:x['name'],reverse=True)
      elif choice == "0":
        print("이전페이지로 이동합니다.")
        break
        

      print("정렬이 완료되었습니다.")

# 학생성적 입력부분을 구현하시오
# dict 타입으로 입력
# 번호, 이름, 국어, 영어, 수학, 합계, 평균, 등수
# 입력 후 출력
# students = []
# s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
# no = 1
# while True:
#   name = input("이름을 입력하세요(취소 : 0) >> ")
#   if name == '0':
#     break
#   kor = int(input("국어 점수를 입력하세요 >> "))
#   eng = int(input("영어 점수를 입력하세요 >> "))
#   math = int(input("수학 점수를 입력하세요 >> "))
#   total = kor + eng + math
#   avg = total / 3
#   rank = 0
#   s = [no, name, kor, eng, math, total, avg, rank]
#   s_dic = dict(zip(s_title, s))
#   print(s_dic)