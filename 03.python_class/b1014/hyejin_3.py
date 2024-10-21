
import random

a_num = []
i = 0 # 초기값
num1 = random.randint(1,100) #### while문 안에 있으면 while 조건이 돌 때마다 랜덤숫자도 같이 변경됨. 그래서 바깥에 있어야함.
count = 0
#### for
# for i in range(10):  # 새로운 변수를 계속해서 만들 수 있음
#   a_num = int(input("숫자를 입력하세요."))
#   if num1<a_num:
#     print("숫자가 큽니다.")
#   elif num1>a_num:
#     print("숫자가 작습니다.")
#   elif num1 == a_num:
#     print("정답입니다.")
#     break  

#### while
while i<10: # 조건식 # while 문은 True, False 만 판단가능
  a_input = int(input("숫자를 입력하세요.")) 
  a_num.append(a_input)
  if num1<a_input:
    print("숫자가 큽니다.")
  elif num1>a_input:
    print("숫자가 작습니다.")
  elif num1==a_input:
    print(num1, "정답입니다. 지금까지 입력한 숫자 : ",a_num)
    count = 1
    break
  i += 1 

# 10번 도전에서 실패했을 경우
if count == 0:
  print("10번 도전에 실패하셨습니다. 정답번호 : ",num1)
  print("지금까지 입력된 숫자 목록: ", a_num)