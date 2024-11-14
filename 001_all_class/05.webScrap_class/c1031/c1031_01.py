import func

# 나중에 func1, func2 이런식으로 따로 저장하는게 관리에 용이함.

while True:
  # 시작화면 출력
  choice = func.screen()

  # 로그인
  if choice == "1":
    func.memLogin()

  # 비밀번호 찾기 
  elif choice == "2":
    func.search_pw()
    
  # 회원가입
  elif choice == "3":
    pass
  elif choice == "4":
    pass
  