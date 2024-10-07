# 1차원 리스트 - 25개
a_list = []
for i in range(25): # 0-25
  a_list.append(i+1) # 1-25
print(a_list)

# 1차원 리스트 -> 2차원리스트로 변경
b_list = []
for i in range(5):
  a = []
  for j in range(5):  
  # y = 5*i + (j+i)
    a.append(5*i+(j+i)) 
b_list.append(a)
print(a_list)


# 1차원 리스트 -> 2차원리스트로 변경
# (0,25) 5씩 증가
b_list = []
for i in range(0,len(a_list),5):
  b_list.append(a_list[i:i+5]) # 0:5 (0부터 5까지), 5:10, 10:15 ... 
print(b_list)