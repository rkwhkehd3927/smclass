import random

# 1,25 사이의 랜덤숫자를 생성해서 출력하시오.
# num = int(random.random()*25)+1
# num2 = random.randint(1,25)
# ---------------------


# a_list = []
# 25번 반복해서 1,25까지의 랜덤숫자를 입력, 중복은 제거하고 출력하시오.

# for i in range(25):
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)

# print(a_list)


# -------------------------------
# 1-25까지 랜덤으로 배치, 25개를 채울때까지

# b_list = []
# i = 0
# while i<25:
#   r_num = random.randint(1,25)
#   if r_num not in b_list:
#     b_list.append(r_num)
#     i += 1
# print(b_list)


# b_list = []
# while len(b_list)<25:
#   r_num = random.randint(1,25)
#   if r_num not in b_list:
#     b_list.append(r_num)
# print(b_list)
# print(len(b_list))

# -------------------------------------

# 1-25까지 랜덤으로 배치
a_list = []
for i in range(25):
  a_list.append(i+1)


# random.sample() - 범위 리스트, 25개 추출(중복 추출 안됨), 위에 명령이랑 같은 의미
# b_list = random.sample(a_list,25) 
# print(b_list)


# random.choices() - 범위 리스트, 25개 추출(중복 추출 가능!), 위에 명령이랑 같은 의미
b_list = random.choices(a_list,k=25)
print(b_list)
