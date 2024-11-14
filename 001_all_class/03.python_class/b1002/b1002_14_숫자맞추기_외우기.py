# 1-100까지의 랜덤숫자를 생성해서 입력한 숫자가 랜덤숫자보다 크면 "숫자가 큽니다." else "작습니다." 출력
# 10번 도전하도록 하시오
# 정답을 맞추면 "정답입니다." 후 프로그램 종료(break)

import random

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
  a_num = int(input("숫자를 입력하세요.")) # 타입 꼭! 숫자형(int)으로 변경! # 매번 질문하도록 해야하기때문에 while문 안쪽에 넣기
  if num1<a_num:
    print("숫자가 큽니다.")
  elif num1>a_num:
    print("숫자가 작습니다.")
  elif num1==a_num:
    print("정답입니다.",num1)
    count = 1
    break
  i += 1 # while문에만 증감식 넣음, 안넣으면 맞출때까지 계속됨, 증감식을 넣어주지 않으면 i는 계속 0이기 때문!
         # if문 바깥쪽에...?

# 10번 도전에서 실패했을 경우
if count == 0:
  print("10번 도전에 실패하셨습니다. 정답번호 : ",num1)