# 25개 1차원 리스트 -> 1, 25 입력한 후 랜덤으로 다시 출력
# [5,5] 2차원 리스트 입력 후 출력
import random

aArr = []
for i in range(25):
  aArr.append(i+1) # i+1 -> 1부터 25까지 / 를 aArr에 넣음

random.shuffle(aArr) # 섞음
print(aArr) # [24, 14, 20, 7, 12, 6, 2, 8, 5, 10, 16, 11, 25, 1, 3, 23, 21, 4, 17, 9, 19, 15, 18, 13, 22]

a_list = [] # a_list 라는 배열 선언
for i in range(5): # i를 5번 반복? 하여 0,1,2,3,4 라는 방 5개 만듬
  a = [] # 그 안에 a 라는 배열 선언?
  for j in range(5): # a_list 안에 5개 방있는데 그안에 또 위와 같은 방식으로 방 5개 만듬
    a.append(aArr[5*i+j]) # a 안에 aArr 안에 있는 숫자를 for문 한번 돌때마다 숫자 하나 들어가는 방식으로 5번 반복하여 "순서대로" 넣음
    # print(a)
    #### a 가 이런식으로 들어가는 거임
    # [13] 
    # [13, 1]
    # [13, 1, 4]
    # [13, 1, 4, 6]
    # [13, 1, 4, 6, 15] / 한 방 다 채우면 요런식
    # [22]
    # [22, 7]
    # [22, 7, 16]
    # [22, 7, 16, 5]
    # [22, 7, 16, 5, 2] / 그 다음 방도 다 채우면 요런식
  a_list.append(a) # 위처럼 5개씩을 5개 방에 다 채운 a를 a_list에 넣기
print(a_list) # [[13, 1, 4, 6, 15], [22, 7, 16, 5, 2], [21, 3, 25, 23, 14], [24, 12, 11, 8, 20], [10, 18, 17, 19, 9]] 



# 위의 1차원 리스트를 2차원으로 바꾸기
# 5,5 리스트 출력하시오.
while True:
  print("\t0\t1\t2\t3\t4")
  print("-"*60)
  for i in range(5):
    print(i,"|",end="\t")
    for j in range(5):
      print(a_list[i][j],end="\t")
    print()


# 좌표를 입력하여 값 내기 
  # re = input("좌표를 입력하세요.(0.0) >> ")
  # result = re.split(".")
  # print("좌표값 : ",a_list[int(result[0])][int(result[1])])

# 값을 입력하면, 해당좌표를 출력하기
  re = int(input("값을 입력하세요.(1-25) >> "))
  if 0>re or re>26:
    print("1에서 25사이의 값을 입력하셔야 합니다.")
    continue # 다시 입력받기

  for i in range(5):
    for j in range(5):
      if a_list[i][j] == re:
        print(f"좌표값 : [{i,j}]")
        a_list[i][j] = "-"
        break
