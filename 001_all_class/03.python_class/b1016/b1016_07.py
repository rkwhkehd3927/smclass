# while True:
#   score = 100
#   print("[ 나눗셈 프로그램 ]")
#   nstr = input("숫자만 입력가능. >> ")
#   # print("입력된 숫자 : ",nstr)

#   # if nstr.isdigit():

# # try-except : 프로그램에 예외를 처리하는 명령어
# # try - 예외가 발생할 가능성이 있는 코드, except - 예외가 발생했을때 실행할 코드
#   # 숫자가 아닌것 and 0을 입력하면 에러
#   try: # 잘안씀ㅋ
#     # print("숫자로 변환이 가능합니다.")
#     num = int(nstr)
#     print("입력된 숫자로 100을 나눔 : ",score/num)
#   # else:
#   except:
#     print("숫자로 변환 안됨.")

try:
  print("입력된 숫자 : ",int(input("숫자를 입력하세요.> ")))
except:
  pass