# [4,5] 2차원 리스트
# a_list = []

# for i in range(20):
#   a_list.append(i+1)
# print(a_list)

# for i in range(4):
#   a = []
#   for j in range(5):
#     # a.append(5*i+(j+1))
#     a.append(5*3*i+(3*j))
#   a_list.append(a)

# for i in range(4):
#   for j in range(5):
#     print(a_list[i][j],end="\t")


# [0,3,6,9,12...57]
aArr = []

for i in range(20):
  aArr.append(3*i)
print(aArr)

# [4,5] 2차원 리스트
a_list = []
for i in range(4):
  a = []
  for j in range(5):
    a.append(aArr[j]) # index 0,1,2,3,4 / 5*i+j
  a_list.append(a)
print(a_list)


