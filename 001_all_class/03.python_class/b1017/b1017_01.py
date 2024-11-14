# subject = ["국어","영어"]
# def output(subject):
#   # 출력 함수선언
#   print("과목")
#   print("-"*20)
#   for s in subject:
#     print(s)

# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요. >> ")
#   # list - append
#   subject.append(s_input)
#   output(subject) # 출력 함수호출

# --------------------------
# a = 10 # 전역변수

# # 함수선언
# def func(a):
#   # global a # 전역변수를 가져옴 # 2 - 10
#   # a = 50 # 지역변수 - 함수를 종료하면 모두 제거됨
#   print("함수 내 a : ", a) # 1 - 50
#   # 함수는 1번째는 지역변수가 있는지를 먼저 찾고 없으면 2번째로 전역변수를 찾게됨 / 둘다 없으면 에러
#   a += 50
#   return a

# # 함수호출
# a = func(a)
# print("함수 밖 a :", a) # 1 - 10 # 2 - 60
# --------------------------

# a = 10
# b = 20
# sum = 0

# # 함수선언
# def add(a,b):
#   return a+b

# sum = add(a,b) # 함수호출
# print("a+b 합계 : ", sum) #30
# --------------------------

# a = 10
# b = 20
# c = 30
# # a 함수는 사용해서, a+b+c의 합을 a에 저장해서 출력하시오.

# def a_sum(a,b,c):  # 여기서 a,b,c는 함수 내에 새롭게 선언된 변수임 # 함수 내의 매개변수는 전부 새롭게 지역변수로 선언됨
#   # return a+b+c
#   a = a+b+c
#   print(a)

# # a_sum(a,b,c) # 10
# a = a_sum(a,b,c) # 60
# print(a) # 60

# --------------------------

subject = ["국어","영어"]
score = []

while True:
  print("1. 과목추가")
  print("0. 종료")
  choice = input("원하는 번호를 입력하세요. >> ")
  if choice == "1":
    s_input = input("과목을 추가하세요. >> ")
    subject.append(s_input)
  elif choice == "0":
    break


for i in range(len(subject)):
  score.append(int(input(f"{subject[i]} 점수를 입력하세요. >> ")))

sum = 0
for i in range(len(subject)):
  print(f"{subject[i]} : ",score[i])
  sum += score[i]
print("합계 : ", sum)

