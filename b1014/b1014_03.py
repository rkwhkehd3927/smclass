# def num_sum(st,end): # def 함수(매개변수,매개변수)
#   sum = 0 # 지역변수
#   for i in range(st,end):
#     sum += i
#   return sum #### 원하는 위치값으로 돌려준다. 호출하는 곳으로 되돌려준다.

# total = 0
# num_sum(1,10)
# num_sum(1,100)
# total = num_sum(1,10)+num_sum(1,100) # ****
# # 1,10까지의 합과 1,100까지의 합의 총합을 출력하시오.
# print("합계 : ", total)

# print("프로그램 종료")

# ~~~~~~~~~~

# # 1-10까지 합계를 출력하시오.
# num_sum(1,10)

# # 1-100까지 합계를 출력하시오.
# num_sum(1,100)


# # 2-50까지 합계를 출력하시오.
# num_sum(2,50)

# # 100-1000까지 합계를 출력하시오.
# num_sum(100,999)

# # 전역변수
# sum = 0

# -----------------------
# 두 수를 입력받아, 그 사이의 숫자합을 구하시오.
# num1,num2
# 함수를 사용해서 계산하시오.\
# num1 = int(input("숫자1을 입력하세요. >> "))
# num2 = int(input("숫자2를 입력하세요."))
# num_sum(num1,int(input("숫자를 입력하세요. >> ")))
# def num_sum2():
#   for i in range(num1,num2):
#     num1 += i
    
# ----------------------------

# 2-50 합 3-7 합 5-50합을 모두 더해서 출력하시오.

# def num_sum():
#   sum = 0
#   for i in range(st,esnd):
#     sum += 1
#   return sum

# total = 0
# print(f"2-50까지의 합 : {num_sum(2,50):,d}") #.2f
# print("3-7까지의 합 : ",num_sum(3,7))
# print("5-50까지의 합 : ",num_sum(5,50))
# num_sum(2,50)
# num_sum(3,7)
# num_sum(5,50)
# total = num_sum(2,50)+num_sum(3,7)+num_sum(5,50) # ****
# # 1,10까지의 합과 1,100까지의 합의 총합을 출력하시오.
# print("합계 : ", total)

# -------------------------------

def plus(n1,n2):
  result = n1+n2
  return result
def plus2(n1,n2):
  result = n1+n2
  return n1+n2

# print(plus(1,2))
# print(plus(55,45))
# print(plus(50,50))

# 두 수를 입력받아 더하기를 출력하시오.
num = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))
print(plus(num,num2))