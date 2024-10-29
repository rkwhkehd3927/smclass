# employees 테이블에서 a 가 포함된 이름의 모든 컬럼 출력

import oracledb

# db연결 함수 선언
def connetions():
  try:
    conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    # print("db연결 : ",conn.version)
  except Exception as e: print("예외 발생 : ",e)
  return conn

# 함수 호출
conn = connetions()
cursor = conn.cursor()

# ------------------
# 입력한 값을 가지고 이름이 포함되어 있는 데이터를 출력하시오.
# search = input("이름을 입력하세요. >>") 
# search = "%"+search+"%" # 문자의 경우
# search = input("번호검색. >>")

### 문자 키워드
# sql = "select * from employees where emp_name like :search" # 이름 입력
# cursor.execute(sql,search=search)
### 키워드(숫자)
# sql = "select * from employees where employee_id>=:search" # 번호 검색
# cursor.execute(sql,search=search)
### 번호로 검색, 순서
# sql = "select * from employees where employee_id>=:1" # 번호 검색
# cursor.execute(sql,[search])
# ------------------


# 월급 4000~8000 사이의 사원을 모두 출력
# sql = "select distinct employee_id,emp_name,salary from employees where salary >= 4000 and salary <= 8000 order by salary"
# cursor.execute(sql)

# 범위를 입력받아서 그 사이의 사원을 출력
num = input("시작 숫자를 입력하세요. >> ")
num2 = input("마지막 숫자를 입력하세요. >> ")
sql = "select distinct employee_id,emp_name,salary from employees where salary >= :num and salary <= :num2 order by salary"
cursor.execute(sql,num=num,num2=num2)


title = ['employee_id','emp_name','salary']
a_list = [] # dict 타입으로 변경해서 저장
rows = cursor.fetchall()
for row in rows:
  a_list.append(dict(zip(title,row)))
  print(row)
print(a_list)

cursor.close()
