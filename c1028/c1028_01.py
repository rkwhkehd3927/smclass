import oracledb


# input("엔터키 입력")

# oracle 연결 - sql developer 연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
# 연결확인
print(conn.version)

### sql 실행창 오픈
# 1개의 검색된 데이터 호출
# cursor = conn.cursor()
# sql = "select count(*) from member"
# cursor.execute(sql)
# count1 = cursor.fetchone()
# print("개수 : ",count1)

# 여러개의 검색된 데이터 호출
cursor = conn.cursor()
sql = "select * from member"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
  print(row)

# print(rows[0][0],rows[0][1])
for idx, row in enumerate(rows):
  print(idx+1, row)
conn.close()