import random

# 25개가 들어있는 1차원리스트가 있다.
# 25개중 1을 5개, 나머지는 0으로 입력해서 출력하시오.
# print([0]*20+[1]*5)
# a_list = [0]*20+[1]*5
# random.shuffle(a_list)
# print(a_list)

# 0 - 20개, 1 - 5개 생성
# a_list = []
# for i in range(25):
#   if i<20: # 20번 까지는 0으로
#     a_list.append(0)
#   else:
#     a_list.append(1)

#  --------------------------
# [5,5] 2차원 리스트에 a_list의 값을 입력한 후 출력하시오.
a_list = [0]*20+[1]*5
random.shuffle(a_list)
print(a_list)

#### 엉망으로 내가 한거ㅠ
# a_list = []
# for i in range(25):
#   a_list.append(i+1)

# b_list = [] 
# for i in range(5):
#   a = []
#   for j in range(5):
#     a.append(5*i+j)
#     b_list.append(a)
# print(a_list)



b_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(a_list[5*i+j]) # 0,1,2,3...24 # a_list(1차원) 5개를 리스트에 추가
  b_list.append(a) # a 리스트를 b_list 리스트에 추가 (5개씩 잘라서)
print(b_list)

# [5,5] 출력
while True: # 무한 반복시키기
  print("\t0\t1\t2\t3\t4")
  print("-"*50)
  for i in range(5):
    print(i,end="\t")
    for j in range(5):
      print(b_list[i][j],end="\t") # 옆쪽으로 출력
    print() # 5개씩 나눠서 출력

  num = input("좌표를 입력하세요.(0,0) >> ")
  num2 = num.split(",")
  print(f"{num}좌표 값 : {b_list[int(num[0])][int(num2[1])]}")

