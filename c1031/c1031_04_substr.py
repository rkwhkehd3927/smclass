### 입력한 달 이상(이후) 입사한 사원 출력
import oracledb

def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외 발생",e)
  return conn
  
conn = connects()
cursor = conn.cursor()

# 1.
d_day = int(input("숫자를 입력하세요. >> "))

# 2.
# d_day = input("숫자를 입력하세요. >> ")
# d_day = f"0{d_day}"
sql = "select emp_name,hire_date from employees\
  where substr(hire_date,4,2) > :d_day order by hire_date"
cursor.execute(sql,d_day=d_day)
rows = cursor.fetchall()
for row in rows:
  print(row)
