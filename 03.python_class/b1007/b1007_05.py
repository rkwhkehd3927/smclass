import random

#### 1-25까지 랜덤 숫자 25개를 중복없이 추출하여 [5,5] 2차원 리스트에 입력하여 출력하시오.

# 내가 엉망으로 한거ㅋㅎ
# a_list = []
# for i in range(25):
#   num = random.randint(1,25)
#   if num not in a_list():
#     for j in range(5): 
#       a = []
#       for k in range(5):
#         a.append(5*j+(k+j))
#     a_list.append(num)
# print(a_list)

# ---------------
# 몰라 이해가 안됨 흑흑ㅠㅠ
# a_list = []
# while len(a_list)<25:
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)

# b_list = []
# for i in range(5):
#   a = []
#   for j in range(5):
#     a.append(a_list[5*i+j]) # a_list[0], a_list[1], a_list[2], a_list[3], a_list[4],
#   b_list.append(a)
# print(b_list)

# --------


#### random.shuffle()
a_list = []
for i in range(25):
  a_list.append(i+1)

print(a_list)

random.shuffle(a_list) # 섞임
print(a_list)

# (0,25,5)
b_list = []
for i in range(0,len(a_list),5): # 0 부터 25(len(a_list))까지, 5씩 증가 라는 의미
  b_list.append(a_list[i:i+5])

print(b_list)

# b_list 랜덤으로 섞어서 1-25까지 [5,5] 2차원 리스트
while True:
  print("\t0\t1\t2\t3\t4")
  print("-"*50)
  for i in range(5):
    print(i,end="\t")
    for j in range(5):
      print(b_list[i][j],end='\t')
    print()
  input1 = input("좌표를 입력하세요.[0,1]>> ")
  input2 = input1.split(",") # input2에 배열(리스트)로 넘어감
  print(input2)
  print(f"{input1}좌표 값 : ",b_list[int(input2[0])][int(input2[1])])
