# 사칙연산
def operate(count): # 함수 정의
  for i in range(count):
      print("한국어 인사 : 안녕하세요.") 

while True:
  print("[ 외국어 인사 ]")
  print("1. 한국어 인사")
  print("2. 일본어 인사")
  print("3. 영어 인사")
  print("4. 프랑스 인사")
  choice = input("원하는 번호를 입력하세요.(1) >> ")
  count = int(input("한국어 반복횟수를 입력하세요.(3) >> "))
  if choice == "1":
    operate(count) # 함수 호출
    print("영어 인사 : 헬로우, (Hello)")
  elif choice == "2":
    operate(count) # 함수 호출
    print("일본어 인사 : 오하요우(Ohayo)")
  elif choice == "3":
    operate(count) # 함수 호출 
    print("중국어 인사 : 니 하오,(Ni Hau)")
  elif choice == "4":
    operate(count) # 함수 호출
    print("프랑스 인사 : 봉주르, (Bonjour)")