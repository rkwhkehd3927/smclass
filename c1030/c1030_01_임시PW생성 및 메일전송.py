import oracledb
import random
# email 발송관련
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외 발생",e)
  return conn

while True:
  print("[ 커뮤니티 ]")
  print("1. 로그인")
  print("2. 비밀번호 분실")
  print("3. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요. >> ")

  if choice == "1":
    print("[ 로그인 ]")
    user_id = input("아이디를 입력하세요. >>")
    user_pw = input("패스워드를 입력하세요. >>")

    # db 접속
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id and pw=:pw"
    cursor.execute(sql,id=user_id,pw=user_pw)
    # rows = cursor.fetchall()
    row = cursor.fetchone() # None
    # print(rows)
    print(row)
    # if len(rows) == 1:
    if row != None:
      # print("로그인 성공!")
      print(f"로그인 성공! {row[2]} 님 환영합니다.")
    else:
      print("아이디 또는 패스워드가 일치하지 않습니다.")
    cursor.close()


    #  oracledb 에 접속해서 member 테이블에서 검색 후 가져오기
    # if user_id == 'aaa' and user_pw == "1111":
    #   print("로그인 성공")
    # else:
    #   print("로그인 실패")
    #   continue
    print("[ 학생성적 프로그램에 접속합니다. ]")
    #### 프로그램 구현 ####

  elif choice == "2":
    print("[ 비밀번호 찾기 ]")
    search = input("해당 아이디를 입력하세요. >> ")
    # 아이디 있는지 확인
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id"
    cursor.execute(sql,id=search)
    row = cursor.fetchone()
    # print(row)

    if row != None:
      print("아이디가 존재합니다. 임시 패스워드를 발급합니다.")
      # 1. 임시 비밀번호생성
      # 2. 이메일로 전송
      # 3. 비밀번호를 임시비밀번호로 수정
      # 4. 임시번호로 로그인 할 경우, 로그인 성공 출력

      ### 임시 비밀번호 생성 및 임시비밀번호로 pw 변경
      a = random.randrange(0,10000) # 0-9999
      ran_pw = f"{a:04}"
      sql = "update member set pw=:pw where id=:id"
      cursor.execute(sql,id=search,pw=ran_pw)
      conn.commit()
      # print("임시 비밀번호 : ",ran_pw)
      
      ### 이메일로 임시비밀번호 전송
      smtpName = "smtp.naver.com"
      smtpPort = 587
      sendEmail = "rkwhkehd3927@naver.com"
      pw = "MDHHDW1ZDM8R"
      recvEmail = "rkwhkehd3927@naver.com" # 받는사람 메일 : row[3]
      title = "임시 비밀번호 전송"
      content = f"임시 비밀번호 : {ran_pw}"

      msg = MIMEMultipart()
      msg['Subject'] = title
      msg['From'] = sendEmail
      msg['To'] = recvEmail
      msg.attach(MIMEText(content))

      s = smtplib.SMTP(smtpName,smtpPort)
      s.starttls()
      s.login(sendEmail,pw)
      s.sendmail(sendEmail,recvEmail,msg.as_string())
      # print("msg : ")
      # print(msg.as_string)
      s.quit()

      print("메일로 임시 비밀번호를 발송했습니다.")
      print("임시 비밀번호로 로그인해주세요.")

      ### 재로그인
      while True:
        user_id = input("아이디를 입력하세요. >> ")
        user_pw = input("비밀번호를 입력하세요. >> ")
        sql = "select * from member where id=:id and pw=:pw"
        cursor.execute(sql,id=user_id,pw=user_pw)
        row = cursor.fetchone()
        if row != None:
          print(f"로그인 성공! {row[2]} 님 환영합니다.")
          break
        else: 
          print("아이디 혹은 비밀번호가 일치하지 않습니다. 다시 시도해주세요.")
          continue

    else:
      print("아이디가 존재하지 않습니다.")
    cursor.close()

  elif choice == "3":
    pass
  elif choice == "0":
    print("프로그램 종료합니다.")
    break