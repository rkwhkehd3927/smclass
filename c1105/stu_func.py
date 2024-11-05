import oracledb


s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

#### db 연결 함수 선언
def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외처리 : ",e)
  return conn

#### 메인 화면 출력
def main_print():
  print("[ 학생 성적 프로그램 ]")
  print("1. 학생 성적 입력")
  print("2. 학생 성적 출력")
  print("3. 학생 성적 검색")
  print("4. 학생 성적 정렬") # 이름 순차 정렬, 이름 역순 정렬, 합계 순차 정렬, 합계 역순 정렬
  print("5. 등수 처리") 
  print("0. 프로그램 종료")
  print()
  choice = input("원하는 번호를 입력하세요. >> ")
  return choice

####  학생 성적 입력 함수 선언
def stu_insert():
  # no : seq 으로 입력할 거임
  conn = connects()
  cursor = conn.cursor()
  print("[ 학생 성적 입력 ]")
  # sql = "select students_seq.currval from dual" # sql 에서 다음 no 받기
  # cursor.execute(sql)
  # row = cursor.fetchone()
  # cursor.close()
  # no = row[0]
  name = input("학생 이름을 입력하세요.")
  kor = int(input("국어 점수를 입력하세요."))
  eng = int(input("영어 점수를 입력하세요."))
  math = int(input("수학 점수를 입력하세요."))
  total = kor+eng+math
  avg = total/3
  # list
  s_list = [name,kor,eng,math,total,avg]
  # insert,update,delete 의 경우 반드시 conn.commit() 을 해야 반영됨.
      # no: seq
      # 입력 필요 데이터: name, kor, eng, math
      # total: 오라클에서 입력
      # avg: 오라클에서 입력
      # rank: 오라클에서 입력
      # sdate: sysdate 오라클에서 입력
  sql = "insert into students values\
    (students_seq.nextval,:1,:2,:3,:4,\
      :5,:6,0,sysdate)" # rank는 일단 0
  # cursor.execute(sql,name=name,kor=kor,eng=eng,math=math,total=total,avg=avg)
  cursor.execute(sql,s_list)
  conn.commit()
  conn.close()
  print("학생성적이 저장되었습니다.")
  print()
  return conn

#### 학생 성적 출력 함수 선언
def stu_output():
  print("[ 학생 성적 출력 ]")
  for s in s_title:
    print(s,end='\t')
  print()
  print("-"*80)
  # db 연결
  conn = connects()
  cursor = conn.cursor()
  sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
  cursor.execute(sql)
  rows = cursor.fetchall()
  # print("개수 : ",len(rows))
  if len(rows) < 1:
    print("데이터가 없습니다.")
    return
  for row in rows:
    for r in row:
      print(r,end='\t')
    print()
  print()
  print("데이터 출력 완료!")    
  return conn


#### 학생 성적 검색 함수 선언
def stu_search():
  print("[ 학생 성적 검색 ]") 
  print("1. 이름으로 검색") 
  print("2. 등급순으로 검색") 
  choice = input("원하는 번호를 입력하세요. >> ")
  if choice == "1":
    print("[ 이름으로 검색 ]")
    search = input("찾고자 하는 이름을 입력하세요. >> ")
    serach = '%'+search+'%'
    # e.g. 이름에 'search'가 포함되어 있는 학생 검색
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') \
      from students where name like :search"

  # ---------- 출력부분
  
    # db 연결
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql,search=search)
    rows = cursor.fetchall()
    print("개수 : ",len(rows))
    for s in s_title:
      print(s,end='\t')
    print()
    print("-"*80)
    if len(rows) < 1:
      print("데이터가 없습니다.")
      return
    for row in rows:
      for r in row:
        print(r,end='\t')
      print()
    print()
    print("데이터 출력 완료!") 
  return conn




# 학생 성적 정렬 
def order_by():
  choice = input("원하는 번호를 입력하세요. >> ")
  conn = connects()
  cursor = conn.cursor()
  if choice == "1":
    print("이름 순차 정렬")
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by name"
  elif choice == "2":
    print("이름 역순 정렬")
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by name desc"
  elif choice == "3":
    print("합계 순차 정렬")
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by total"
  elif choice == "4":
    print("합계 역순 정렬")
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by total desc"
  cursor.execute(sql)
  rows = cursor.fetchall()
  if len(rows) < 1:
    print("데이터가 없습니다.")
    return
  for s in s_title:
    print(s,end='\t')
  print()
  print("-"*80)
  for row in rows:
    for r in row:
      print(r,end='\t')
    print()
  print()
  print("데이터 출력 완료!")   
  return choice

### 학생 성적 정렬 함수 선언
def stu_desc():
  print("[ 학생 성적 정렬 ]") 
  print("1. 이름 순차 정렬") 
  print("2. 이름 역순 정렬") 
  print("3. 합계 순차 정렬") 
  print("4. 합계 역순 정렬") 
  choice = order_by() 
  return choice

### 등수 처리 함수 선언
def stu_rank():
  print("[ 등수 처리 ]") 
  sql = "update students a set rank = ( \
    select ranks from(\
      select no,name,kor,eng,math,total,round(avg,2),rank() over(order by avg desc) as ranks, \
        to_char(sdate,'yyyy-mm-dd') from students) b \
          where a.no=b.no)"
  # db 연결
  conn = connects()
  cursor = conn.cursor()
  cursor.execute(sql)
  conn.commit()
  print("등수처리가 완료되었습니다.") 
  print()
  # ----------- 등수 처리후 값을 students에 저장
  sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
  cursor.execute(sql)
  rows = cursor.fetchall()
  print("개수 : ",len(rows))
  for s in s_title:
    print(s,end='\t')
  print()
  print("-"*80)
  if len(rows) < 1:
    print("데이터가 없습니다.")
    return
  for row in rows:
    for r in row:
      print(r,end='\t')
    print()
  print()
  print("데이터 출력 완료!") 
  return conn
