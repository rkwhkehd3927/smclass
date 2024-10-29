import oracledb

# sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
# sql 창이 열림
cursor = conn.cursor()
# sql 작성, 실행
sql = "select * from students"
cursor.execute(sql)

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
