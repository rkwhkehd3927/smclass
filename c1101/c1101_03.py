# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students 테이블을 사용하여 
# 시퀀스 students_seq 생성
# 번호,'김유신',99,98,96,합계,평균,등수 입력일(sdate) 까지 입력하여 생성

import oracledb
import datetime


def connect():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외처리: ",e)
  return conn

def stu_count():
  conn = connect()
  cursor = conn.cursor()
  sql = "select count(*) from students"
  cursor.execute(sql)
  rows = cursor.fetchall()
  for row in rows:
    len_stu.append(row)
  conn.close()
  return len_stu

while True:
  print("[ 학생 성적 프로그램 ]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적검색")
  choice = input("원하는 번호를 입력하세요. >> ")
  print("-"*30)


 

  if choice == "1":
    len_stu = stu_count()
    print("[ 학생성적입력 ]")
    no = len_stu + 1
    print(no)
    name = input("이름을 입력하세요.")
    kor = int(input("국어 점수를 입력하세요."))
    eng = int(input("영어 점수를 입력하세요."))
    math = int(input("수학 점수를 입력하세요."))
    total = kor+eng+math
    avg = total/3
    rank = 0
    sdate = datetime.datetime.now().strftime('%y/%m/%d')

    stu_list = [no,name,kor,eng,math,total,avg,rank,sdate]
    print(stu_list)

    conn = connect()
    cursor = conn.cursor()
    sql = "insert into students (no,name,kor,eng,math,total,avg,rank,sdate) values (:no, :pw)"
