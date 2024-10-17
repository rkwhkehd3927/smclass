# 예외처리 : try - except 구문을 사용해서 처리
# print("프로그램 시작") 
# print(list_a)

# try:
#   # print("프로그램 시작) # 구문오류 - 프로그램이 실행전에 오류
#   print(list_a) # 런타임 오류 - 프로그램 실행 중에 오류

# except:
#   print("에러가 발생되었습니다.")

# print("프로그램 종료")

# -------------------

# n_str = input("반지름을 입력하세요. >> ")
# # if n_str.isdigit():
# try:
#   num = int(n_str)
#   # 원 넓이, 원 둘레
#   print("원 넓이 : ",(num**2)*3.14)
#   print("원 둘레 : ", 2*num*3.14)
# except Exception as e :
#   print("정수가 아닙니다. 정수를 입력하세요.",e)

# -------------------
# list_a = [1,2,3,4,5,"홍길동"]
# list_b = []
# # 숫자에 *2를 하는 프로그램을 구현하시오.
# # "홍길동" 이 에러가 났어야하는데 안보여주고 걍 억지로 실행시킴
# try:
#   for a in list_a:
#     list_b.append(a**2)
# except Exception as e: # 어디가 에러났는지 보여주기
#   print(e)

# print(list_b)
# -------------------
# try - except : try에 에러가 발생하면 except 실행
# try - except - else : else는 try구문에 에러가 없으면 실행
# try - except - else - finally : try에서 에러가 발생하든 안하든 finally는 무조건 실행

# print("1")
# try: # try구문에 에러가 발생해야 except를 실행시킴
#   print("2")
#   print(3/0) # error
#   print("3") # 위에서 에러나면 실행안시켜버림
#   print("4") # 위에서 에러나면 실행안시켜버림
# except:
#   print("5")
#   print("6")
# else:
#   print("프로그램 에러가 발생하지 않으면 실행")
# finally:
#   print("finally 실행됨.")

# print("7")
# print("8")

# -------------------
# print("파일 open")
# try:
#   print("글쓰기1")
#   print("글쓰기2")
#   print("글쓰기3")
#   print("str -> 딕셔너리 입력 4") # 에러
#   print("글쓰기5")
#   print("글쓰기6")
# except:
#   print("잘못된 타입이 들어왔습니다.")
# finally:
#   print("파일 close")

# print("프로그램을 종료합니다.")
# -------------------
# f = open("b1017/a.txt","w",encoding="utf-8")
# try:
#   f.write("안녕하세요.1\n") 
#   f.write("안녕하세요.2\n") # 여기까지만 들어감
#   f.write({"a":1}) # 에러 
#   f.write("안녕하세요.3") # 위에서 에러나서 실행안됨
# except Exception as e:
#   print(e)
# finally:
#   f.close()
# -------------------

numbers = [52,273,32,103,90,10,275,1,2,1,2,12]
# a = "12351200"
try:
  print(numbers.index(52)) # 0 : 0번째에 있다는 뜻
  print(numbers.index(1)) # 7 : 7번째에 있다는 뜻
  print(numbers.index(3))
  print(numbers.index(32))
  print(numbers.index(90))
except Exception as e: # Exception : 모든 예외의 가장 상위
  print("찾는 번호가 없습니다", e)
# print(numbers.index(3)) # 없으면 error
# print(a.find("52")) # -1 : 없다는 뜻
