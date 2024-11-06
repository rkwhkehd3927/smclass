# oracledb에서는 자동 형변환해줘서
# 문자형(숫자)타입 + 숫자 사칙연산 됨
# 파이썬에서 호출한 타입의 결과값이 어떻게 되는지 확인

import oracledb

def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"

  try:
    conn = oracledb.connect(user=user, password=password, dsn=dsn)
  except Exception as e:
    print("예외처리", e)

  return conn

conn = connects()
cursor = conn.cursor()

# chartable : number, number, varchar2, varchar2
# chartable2 : number, number, number, number
sql = "select no, kor, to_char(kor , '00000000'), to_char(kor, '999,999,999') from chartable"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
  # print(f"두 수의 합 : {row[1] + row[2]}")  # 오라클에서는 자동형변환이되어 계산됨 하지만 파이썬은 안 됨
  print(row)

print("검색완료")

conn.close()