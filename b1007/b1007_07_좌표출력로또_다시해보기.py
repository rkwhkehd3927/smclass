
# 이걸로 먼저 해서 이해하기
# a_list = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ] 
import random

# 이거는 나중에 추가된 것
lotto = [0]*6+[1]*3
random.shuffle(lotto)
print(lotto)
a_list = [
  [0,1,0],
  [0,0,1],
  [1,0,0]
]

#### 이게 뭔뜻이야?....
for i in range(3):
  for j in range(3):
    a_list[i][j] = lotto[3*i+j]
    #      0  0            0
    #      0  1            1
    #      0  2            2
    #      1  0            3
    #      1  1            4 ...

aa_list = [
  ["로또","로또","로또"],
  ["로또","로또","로또"],
  ["로또","로또","로또"]
]

while True: # 무한대로 돌아감
  myMoney = int(input("얼마를 투자하시겠습니까?"))

  print("   [i,j 좌표]")
  print("\t0\t1\t2")
  print("-"*30)
  for i in range(3):
    print(i,"|",end="\t")
    for j in range(3):
      # print(a_list[i][j],end="\t") # 3번 찍고 나서 for문 빠져나가기 # end="\t" 옆으로 늘어놓기
      print(aa_list[i][j],end="\t")
    print() # 여기에는 \n 이 숨겨져있다. 한칸 내려가기
  
  
  code = input("좌표를 입력하세요.(0.0)>> ")
  codeArr = code.split(".") # codeArr[0].codeArr[1]
  # print(codeArr) 
  print(f"{codeArr} 좌표값 : ",a_list[int(codeArr[0])][int(codeArr[1])]) # 좌표값 출력하기

  # if codeArr==1:
  #   print("당첨")
  # else:
  #   print("꽝")

  if a_list[int(codeArr[0])][int(codeArr[1])] == 1:
    aa_list[int(codeArr[0])][int(codeArr[1])] = "당첨"
    print(f"{codeArr} 당첨금 : 당첨 = {myMoney*10:,d}")
  else: 
    aa_list[int(codeArr[0])][int(codeArr[1])] = "꽝"
    print(f"{codeArr} 다음 기회에 : {myMoney}")
