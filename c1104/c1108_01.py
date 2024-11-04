# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students 테이블을 사용하여 
# 시퀀스 students_seq 생성
# 번호,'김유신',99,98,96,합계,평균,등수 입력일(sdate) 까지 입력하여 생성

import oracledb

# db 연결 함수 선언
def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외처리 : ",e)
  return conn

while True:
  print("[ 학생 성적 프로그램 ]")
  print("1. 학생 성적 입력")
  print("2. 학생 성적 출력")
  print("3. 학생 성적 검색")
  print("0. 프로그램 종료")
  print()
  choice = input("원하는 번호를 입력하세요. >> ")
  if choice == "1":
    # no : seq 으로 입력할 거임
    conn = connects()
    cursor = conn.cursor()
    sql = "select students_seq.currval from dual" # sql 에서 다음 no 받기
    cursor.execute(sql)
    row = cursor.fetchone()
    cursor.close()
    print("[ 학생 성적 입력 ]")
    no = row[0]
    name = input(f"{no}번 학생 이름을 입력하세요.")
    kor = int(input("국어 점수를 입력하세요."))
    eng = int(input("영어 점수를 입력하세요."))
    math = int(input("수학 점수를 입력하세요."))
  elif choice == "2":
    pass
  elif choice == "3":
    pass
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break
