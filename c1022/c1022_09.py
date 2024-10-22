# a = "안녕하세요"
# print(a[1:]) # [1] 부터 끝까지 # 녕하세요
# print(a[1:-1]) # [1] 부터 뒤에서 첫번째(-1)까지 # 녕하세
# print(a[:3]) # 안녕하 # 뒤에서 세번째 까지?

# lists = [1,2,3,4,5,6,7,8,9]
# print(lists[1:-1]) # [2, 3, 4, 5, 6, 7, 8]
# print(lists[:-1]) # [1, 2, 3, 4, 5, 6, 7, 8]
# print(lists[3:]) # [4, 5, 6, 7, 8, 9] # 앞에서 세번째부터 끝까지?
# print(lists[3:5]) # [4, 5] 

# ------------

n_lists = [
  [80,4.2,800]
  [90,4.4,2000]
  [200,4.7,10]
  [30,4.3,30]
]

print("기본 : ",n_lists)
# n_lists 에서 1개(n_list) x대입
n_lists.sort(key=lambda x:x[0])
n_lists.sort(key=lambda x:x[0],reverse=True)
print("금액정렬 :", n_lists) 
