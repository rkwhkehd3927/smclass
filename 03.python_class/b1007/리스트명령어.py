# a,b,c,d,e,f,g = 0,0,0,0,0,0,0
# total = 0

# # a,b,c,d,e 의 변수에 숫자를 입력받아 합계를 출력하시오.
# a = int(input("1번째 숫자를 입력하세요."))
# b = int(input("2번째 숫자를 입력하세요."))
# c = int(input("3번째 숫자를 입력하세요."))
# d = int(input("4번째 숫자를 입력하세요."))
# e = int(input("5번째 숫자를 입력하세요."))
# f = int(input("6번째 숫자를 입력하세요."))
# g = int(input("7번째 숫자를 입력하세요."))
# total = a+b+c+d+e+f+g

# print("합계 : ",total)

# ----------------------------------------
# a_list = [0,0,0,0,0,0,0] # 이렇게 말고 아래 방법도 있음
# total = 0
# for idx,a in enumerate(a_list):
#   a = int(input(f"{idx+1}번째 숫자를 입력하세요."))
#   total += a

# print("합계 : ", total)

# a_list = []
# total = 0
# for i in range(10): 
#   j = int(input(f"{i+1}번째 숫자를 입력하세요.>> "))
#   a_list.append(j)
#   total += j

# print("합계 : ", total)

# ------------------------------------

# a_list = []
# total = 0
# # 1-100 까지의 리스트의 합계를 출력

# for i in range(100): # i = 0 부터 시작
#   a_list.append(i+1)
#   total += i+1
# print("합계 : ", total)

# ----------------------------------------

# 문자열, 숫자-정수형, 숫자-실수형, 논리형
# a_list = [1,2,3.0,"안녕",True,False]
# print(a_list[0])
# print(a_list[3])
# print(a_list[-1]) # - 는 거꾸로임! -6,-5,-4,-3,-2,-1

# -----------------------------------------

# a_list = [1,2,3,4,5]

# 순차 출력
# for i in a_list:
#   print(i)

# 역순으로 출력하는 방법1
# for i in range(len(a_list)):  #### len(a_list) 의 갯수 : 5 = [0],[1],[2],[3],[4]
#   print(a_list[-(i+1)]) #### i 는 0부터 시작이니까 -1,-2,-3,-4,-5

# 역순으로 출력하는 방법2
# for i in range(1,len(a_list)+1):
#   print(a_list[-i])
# -------------------------------

#### 얕은 복사, 깊은 복사

# a_list = [1,2,3,4,5]

# b_list = a_list[::-1]
# print(a_list)
# print(b_list)
# a_list[0] = 100
# print(a_list)
# print(b_list)


# b_list = a_list # 얕은 복사
# a_list[0] = 100 # a_list만 수정했는데 b_list도 같이 수정되어 버림
# print(a_list)
# print(b_list)


# b_list = a_list[:] # 깊은 복사
# a_list[0] = 100 # a_list의 값을 변경해도 b_list의 값 변경 안됨
# print(a_list)
# print(b_list)

# ---------------------------------

# 리스트 출력 방법
# a_list = [1,2,3,4,5]
# b_list = [50,100]
# print(a_list[0:3]) # 1,2,3
# print(a_list[2:4]) # 3,4
# print(a_list[:3]) # 1,2,3
# print(a_list[3:]) # 4,5
# print(a_list+b_list) # 1,2,3,4,5,50,100
# print(b_list * 3) # 50,100,50,100,50,100
# print(a_list[::2]) # (2씩 뛰어넘기) 1,3,5
# print(a_list[::-2]) # (뒤에서 부터 2씩 뛰어넘기) 5,3,1
# print(a_list[::-1]) # (역순 출력) 5,4,3,2,1
# print(a_list[:]) # (전부 출력) 1,2,3,4,5
# print(a_list) # (전부 출력) 1,2,3,4,5

# --------------------------

# 리스트 수정 방법
# a_list = [1,2,3,4,5,6,7]
# a_list[3] = 50        # 1개 변경
# a_list[1:2] = [20,30] # (1-2번 바꾸기) 2개 변경
# a_list[4] = [10,20]   # 리스트 안에 리스트로 변경


# # print(a_list[3]) # 4
# print(a_list)

# -------------------------------------

# 리스트 삭제
# a_list = [1,2,3,4,5]
# a_list = None # 전체 삭제 - None 타입
# a_list = [] # 전체 삭제
# a_list[1:3] = [] # 2,5 - 2개 삭제

# print(a_list)

# del 명령어 사용
# del(a_list) # a_list 자체를 삭제해버림 (거의안씀)
# del a_list[0] # 2,3,4,5 - 0번째 리스트 삭제

# --------------------------------------------

#### 리스트 함수
a_list = [1,2,3,4,5,60,3,70,3]
# 리스트 함수 - 추가
a_list.insert(0,100) # 0번째에 데이터 "100" 입력 (index 위치에 해당값 저장)
a_list.append(200) # 뒤쪽에 값 추가
# 리스트 함수 - 삭제
a_list.pop(2) # 해당 index의 위치 삭제
a_list.remove(3) # 입력된 값의 리스트 삭제
a_list.clear() # 전체삭제 (함수형태 전체 삭제인거임)
 
del(a_list[3])      # 해당위치(3번) 리스트 삭제
print(len(a_list)) # 리스트 개수
print(a_list.count(3)) # 입력된 값의 존재 개수 
print(a_list)