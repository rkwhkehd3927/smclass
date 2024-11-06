import oracledb

# sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

# sql 창이 열림
cursor = conn.cursor()

## sql 작성, 실행
num = input("숫자를 입력하세요. >> ")
num2 = input("숫자를 입력하세요. >> ")
num3 = input("숫자를 입력하세요. >> ")

# 1.문자열 함수 f 사용
# sql = f"select * from students where no>={num}"
# cursor.execute(sql)

# 2. execute함수 : 변수 key 값 전달
# sql = "select * from students where no>=:no"
# cursor.execute(sql,no=num)


num = input("숫자를 입력하세요. >>(,해서 입력하시오.) ")
# 10,20,30
n_list = [num.split(",")]

 
# 3. execute함수 : 리스트 값 전달
# n_list = [num,num2,num3]
# sql = "select * from students where no in(:1,:2,:3)"
# cursor.execute(sql,n_list) #### n_list 자리에는 dictionary, list 혹은 tuple 만 올 수 있음

# 4. 
sql = "select * from students where no in(:no1,:no2,:no3)"
cursor.execute(sql,no1=num,no2=num2,no3=num3)


# 데이터 가져오기
rows = cursor.fetchall()
titles = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']
for title in titles:
  if title == '이름':
    print(title,end="\t\t")
    continue 
  print(title,end="\t")
print()
print("-"*80)

for row in rows:
  for i,r in enumerate(row):
    if i == 1:
      print(f"{r:10s}",end="\t") # 이름은 10번째 자리까지만 출력
      continue
    if i == 6:
      print(f"{r:2f}",end="\t") # 평균은 소수점 둘째자리 까지만 출력
      continue
    if i == 8:
      # strftime()함수 : 날짜포맷함수 $Y - 2024, %y - 24
      print(r.strftime("%Y-%m-%d")) 
      continue
    print(r,end="\t")
  print()

  
# 종료(반드시)
conn.close()
