import oracledb
import datetime

def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외처리 : ",e)
  return conn

# 회원수 확인
def member_count():
  conn = connects()
  cursor = conn.cursor()
  ## oracle db - mem 테이블의 count 가져오기
  sql = "select count(*) from mem"
  # employees 테이블 부서번호가 50번인 사원수 가져오기
  # sql = "select count(department_id) from employees"

  # employees 테이블 부서번호가 50번인, 부서인원, 부서번호, 부서명 가져오기
  # sql = "select count(*) no,a.department_id dept,\
  #   department_name deptname from employees a, departments b \
  #     where a.department_id = b.department_id and a.department_id=50 \
  #       group by a.department_id,department_name"
  cursor.execute(sql)
  row = cursor.fetchone()
  print(row)
  conn.close()
  return row


  

### 회원수 확인값을 리턴
all_member = member_count()

print("[ 커뮤니티 ]")
print(f"현재 회원수: {all_member[0]}")
print()
print("1. 로그인")
print("2. 회원가입")
print("3. 회원정보수정")
choice = input("원하는 번호를 입력하세요. >> ")
thisYear = datetime.datetime.now().year

if choice == "2":
  id = input("아이디를 입력하세요. >> ")
  pw = input("패스워드를 입력하세요. >> ")
  name = input("이름 입력하세요. >> ")
  birth = input("생년월일을 입력하세요.(e.g. 20020312) >> ")
  age = thisYear-int(birth[:4]) # 나이 자동계산
  gender = input("성별을 입력하세요.(Male,Female) >> ")
  hobby = input("취미를 입력하세요. >> ")

  my_list = [id,pw,name,age,birth,gender,hobby]
  print(my_list)

  # db 접속
  conn = connects()
  cursor = conn.cursor()
  # sql = "insert into mem (id,pw,name,age,birth,gender,hobby) values (:1,:2,:3,:4,:5,:6,:7)"
  # cursor.execute(sql,my_list)
  sql = "insert into mem (id,pw,name,age,birth,gender,hobby) values (:id,:pw,:name,:age,:birth,:gender,:hobby)"
  cursor.execute(sql,id=id,pw=pw,name=name,age=age,birth=birth,gender=gender,hobby=hobby)
  conn.commit()
  conn.close()
  print("저장되었습니다.")

elif choice == "3":

  # db 접속
  conn = connects()
  cursor = conn.cursor()
  id = "aaa"
  sql = "select * from mem where id=:id"
  cursor.execute(sql,id=id)
  row = cursor.fetchone()
  print(f"아이디:{id}, 현재 취미 : {row[6]}")
  hobby = input("수정할 hobby를 입력하세요. >> ")
  sql = "update mem set hobby=:hobby where id=:id"
  cursor.execute(sql,hobby=hobby,id=id)
  conn.commit()
  print("수정 완료!")
  # sql = "insert into mem (id,pw,name,age,birth,gender,hobby) values (:1,:2,:3,:4,:5,:6,:7)"
  # cursor.execute(sql,my_list)
  conn.close()