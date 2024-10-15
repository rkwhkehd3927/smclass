# import S_func # 파일 S_func 에서 함수 다 불러오기
from S_func import* # 위의 방식 말고 이렇게 할 수도 있음 * 는 모든 함수에 적용하라는 뜻.
# from S_func import stu_rank(students) # import 뒤의 특정함수에 적용하라는 뜻.


#### students 를 이 파일에 놓을지, 모듈파일에 놓을지에 따라 매개변수로 보내야할지 결정할수있음
#### 이 파일(메인) 에 있으면 매개변수로 보내줘야함(?)
#### S_func(모듈) 에 있으면 매개변수로 안보내줘도됨(?)
# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
choice = 0 # 전역변수
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경

# s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] # 전역변수
# chk = 0    # 체크변수
# count = 1  # 성적처리
# no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 # 성적처리변수

# # 메뉴출력함수 선언
# def title_program():
#   print("[ 학생성적프로그램 ]")
#   print("-"*60)
#   print("1. 학생성적입력")
#   print("2. 학생성적출력")
#   print("3. 학생성적수정")
#   print("4. 학생성적검색")
#   print("5. 학생성적삭제")
#   print("6. 등수처리")
#   print("7. 학생성적정렬")
#   print("0. 프로그램 종료")
#   print("-"*60)
#   choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
#   return choice
# # --------------------
# # 1. 학생성적입력 함수선언 - 일반변수 변경
# def stu_input(stuNo):
#   while True:
#     print("[ 학생성적 입력 ]")
#     # 학생성적 직접 입력
#     no = stuNo + 1  # 리스트 - 학생수
#     name = input(f"{no}번째 학생 이름을 입력하세요.(0.이전화면) >>")
#     if name == "0":
#       print("성적입력을 취소합니다.")
#       print()
#       break
#     kor = int(input("국어점수를 입력하세요."))
#     eng = int(input("영어점수를 입력하세요."))
#     math = int(input("수학점수를 입력하세요."))
#     total = kor+eng+math
#     avg = total/3
#     rank = 0
#     ss = { "no":no,"name":name,"kor":kor,"eng":eng,
#             "math":math,"total":total,"avg":avg,"rank":rank }
#     students.append(ss)
#     stuNo += 1  # 학생수 1증가
#     print(f"{name} 학생성적이 저장되었습니다.!")
#     print()
#   return stuNo
# # --------------------
# # 2. 학생성적출력 함수선언
# def stu_output(students):
#   print("[ 학생성적 출력 ]")
#   print()

#   # 상단출력
#   for st in s_title:
#     print(st,end="\t")
#   print(); print("-"*60)
  
#   # 학생성적출력
#   for s in students:
#     print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
#   print()
# # ------------------------
# # 3. 학생성적수정 함수선언
# def stu_update(students):
#   print("[ 학생성적수정 ]")
#   name = input("찾고자 하는 학생의 이름을 입력하세요.")
#   chk = 0
#   for s in students:
#     if s['name'] == name:
#       # 학생성적 수정
#       print(f"{name} 학생을 찾았습니다.")
#       print()
#       print("[ 수정 과목 선택 ]")
#       print("1. 국어점수")
#       print("2. 영어점수")
#       print("3. 수학점수")
#       choice = input("원하는 번호를 입력하세요.>> ")
#       if choice == "1":
#         print("이전 국어점수 : {}".format(s['kor']))
#         s['kor'] = int(input("변경 국어점수 : "))
#       elif choice == "2":
#         print("이전 영어점수 : {}".format(s['eng']))
#         s['eng'] = int(input("변경 영어점수 : "))
#       elif choice == "3":
#         print("이전 수학점수 : {}".format(s['math']))
#         s['math'] = int(input("변경 수학점수 : "))
#       s['total'] = s['kor']+s['eng']+s['math']  # 합계
#       s['avg'] = s['total']/3          # 평균
#       print(f"{name} 학생 성적이 수정되었습니다.")
#       print()
#       # 학생출력
#       # 상단타이틀 출력
#       for title in s_title:
#         print(f"{title}\t",end="")
#       print()
#       print("-"*60)
#       print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\n")
#       print()
#       chk = 1
#   # 모든 학생 비교가 끝난 후, chk 확인
#   if chk == 0:
#     print(f"{name} 학생이 없습니다. 다시 입력하세요.")
#   print()

# # --------------------------------------------
# # 4. 학생성적검색 함수선언
# def stu_select(students):
#   while True:
#     flag = 0
#     print("[ 학생성적검색 ]")
#     name = input("찾고자 하는 학생의 이름을 입력하세요.(0.이전화면 이동) >> ")
#     if name == "0":
#       break
#     sArr = []
#     for idx,s in enumerate(students):
#       if s['name'].find(name) != -1: # -1(단어없음)이 아니라면
#         # print(f"{idx} 번째,{name} 학생을 찾았습니다." ,s['name'])
#         sArr.append(s) # s = 찾은 학생들
#         flag = 1

#     if flag == 0:
#       print("찾는 학생이 없습니다.")
#     else:
#       print(f"{name} 이름으로 {len(sArr)}명의 학생이 검색되었습니다.")
#       stu_output(sArr) # 검색된 학생들 성적 출력

# # ------------------------------
# # 5. 학생성적삭제 함수선언
# def stu_delete(students):
#   print("[ 학생성적 삭제 ]")
#   name = input("찾고자 하는 학생의 이름을 입력하세요.")
#   flag = 0
#   sArr = []
#   for idx,s in enumerate(students):
#     if s['name'] == name:
#       flag = 1 # break 위쪽에 해야함
#       print(f"{name} 학생성적을 삭제하시겠습니까?( 삭제시 복구 불가 )")
#       print("1.삭제 2.취소")
#       choice = input("원하는 번호를 입력하세요. >> ")
#       if choice == "1":
#         sArr.append(s)
#         del students[idx]
#         print(f"{name} 학생성적이 삭제되었습니다.")
#       else:
#         print("학생성적 삭제가 취소되었습니다.")
#       break
#   # 모든 학생 비교가 끝난 후, flag 확인
#   if flag == 0:
#     print(f"{name} 학생이 없습니다. 다시 입력하세요.")
#   else:
#     stu_output([s]) # 삭제한 사람만 출력

# # --------------------------------------------------
# # 6. 학생성적등수처리 함수선언
# def stu_rank(students):
#   print("[ 등수처리 ]")
#   for s in students:
#     count = 1
#     for st in students:
#       if s['total'] < st['total']:
#         count += 1
#     s['rank'] = count # 등수입력
#   print("등수처리가 완료되었습니다.")
#   print()
#   stu_output(students)

# # --------------------------------------------------
# # 7. 학생성적정렬 함수선언
# def stu_sort(students):
#   while True:
#     print("[ 학생성적 정렬 ]")
#     print("1. 이름 순차정렬")
#     print("2. 이름 역순정렬")
#     print("3. 합계 순차정렬")
#     print("4. 합계 역순정렬")
#     print("5. 번호 순차정렬")
#     print("0. 이전페이지 이동")
#     print("-"*40)
#     choice = input("원하는 번호를 입력하세요.>> ")
#     if choice == "1":
#       students.sort(key=lambda x:x['name']) # 리스트를 1개 가져와서 딕셔너리 중 'name' 을 가져와서 리턴
#     elif choice == "2":
#       students.sort(key=lambda x:x['name'],reverse=True) # 역순정렬
#     elif choice == "3":
#       students.sort(key=lambda x:x['total'])
#     elif choice == "4":
#       students.sort(key=lambda x:x['total'],reverse=True) # 역순정렬
#     elif choice == "5":
#       students.sort(key=lambda x:x['no'])
#     elif choice == "0":
#       print("이전페이지로 이동합니다.")
#       break
#     print("정렬이 완료되었습니다.")



# --------------------프로그램 시작---------------------------------------
# 학생성적프로그램
while True:
  choice = title_program()        # 메뉴출력함수 호출
  if choice == "1":
    stuNo = stu_input(stuNo)      # 학생성적입력함수 호출
  elif choice == "2":            
    stu_output(students)          # 학생성적출력함수 호출 # s_title 은 글자(내용)가 바뀌는 건 아니라서 함수 속 값을 받을 필요없음
  elif choice == "3":
    stu_update(students)          # 학생성적수정함수 호출
  elif choice == "4":  
    stu_select(students)          # 학생성적검색함수 호출
  elif choice == "5":
    stu_delete(students)          # 학생성적삭제함수 호출
  elif choice == "6":
    stu_rank(students)            # 학생성적등수처리 함수 호출
  elif choice == "7":
    stu_sort(students)            # 학생성적정렬함수 호출
    
  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break

# 학생성적 입력부분을 구현하시오.
# dict타입으로 입력을 할것
# 번호,이름,국어,영어,수학,합계,평균,등수
# 입력이 완료되면 출력이 바로 되도록 하시오.