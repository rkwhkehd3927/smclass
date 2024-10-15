# def func(v):
#   return v*2
# # 위,아래 두개가 동일
# lambda v:v*2 # lambda는 1줄만 가능함

# ---------------------------
# 기본적인 함수사용
# print(func(2)) # 4
# aArr = [1,2,3,4]
# print(aArr)

# bArr = []
# for a in aArr:
#   bArr.append(func(a))
# print(bArr) # [2, 4, 6, 8]
# -----------------------------

# 리스트 내포
# aArr = [1,2,3,4]
# print(aArr)
# bArr = [ a*2 for a in aArr] # 위에거를 한줄로 간단하게 만든 것
# print(bArr) # [2, 4, 6, 8]

# -----------------------------

# map 함수 - map(함수,리스트) : 리스트의 내용을 1개씩 함수에 전달해서 결과값을 리스트로 저장 
# aArr = [1,2,3,4]
# bArr = list(map(func,aArr)) # 맵 뒤에 함수, 리스트 혹은 연속되는 값 # 반드시 리스트타입으로 변경해줘야함
# print(type(bArr)) # list
# print(bArr) # [2, 4, 6, 8]

# bArr = list(map(lambda x:x*2,aArr)) # lambda는 함수의 줄임

# ------------------------------

# filter(함수,반복가능한자료형) - 리스트,튜플,딕셔너리

# 기본함수사용방법
# def func(v):
#   if v%2 == 0:
#     return v
#   else:
#     return False

# aArr = [1,2,3,4]
# bArr = []
# for i in aArr:
#   if func(i) != None:
#     bArr.append(func(i))
# print(bArr)

####
# filter 함수 사용, lambda식 사용
# def func(v):
#   if v%2 == 0:
#     return True
#   else:
#     return False

# aArr 값중에 2의 배수인 경우만 리턴
# aArr = [1,2,3,4]
# bArr = list(filter(func,aArr)) # 위 조건(함수 func())에 맞는 값만 bArr로 넘겨줌
# print(bArr) # [2, 4]


## lambda 식 변경
# aArr = [1,2,3,4]
# bArr = list(filter(lambda x:x%2==0,aArr)) # x:x%2==0 이 조건에 맞는 값들만 bArr에 넣음
# print(bArr) # [2, 4]


# --------------

# zip 함수 : 2개 리스트를 1개로 변경
# a = [1,2,3,4]
# b = [10,20,30,40]
# print(list(zip(a,b))) # tuple 형태 # [(1, 10), (2, 20), (3, 30), (4, 40)]
# print(dict(zip(a,b))) # dict 형태 # {1: 10, 2: 20, 3: 30, 4: 40}

# -------

# def func(v1,v2):
#   return v1*v2

# lambda v1,v2:v1*v2

# --------------------

#### a+b = [11,22,33,44]

# 기본함수
# a = [1,2,3,4]
# b = [10,20,30,40]
# aArr = []
# def func(a,b):
#   for i,j in zip(a,b): # 리스트 2개보낼때 zip으로 묶어서 보내기
#     aArr.append(i+j)
#   return aArr
# print(func(a,b))  # [11,22,33,44]

# def func(a):
#   for i in a: # 리스트 1개 보낼때는 이런식의 for문
#     aArr.append(i*i)
#   return aArr
# print(func(a))

# 리스트내포
# a = [1,2,3,4]
# b = [10,20,30,40]
# aArr = [i+j for i,j in zip(a,b)]
# print(aArr)  # [11,22,33,44]

# lambda 식
# a = [1,2,3,4]
# b = [10,20,30,40]
# 순서 - map(lambda 매개변수1, 매개변수2: 리턴값(수식), 복합자료형1, 복합자료형2)
# aArr = list(map(lambda i,j:i+j,a,b))
# print(aArr)  # [11, 22, 33, 44]

# ------------------------------

# 퀴즈
a = [1,2,3,4,5]
# a 리스트에 전부 10을 더해서 리스트에 담아 출력하시오.
# 리스트 내포, map lambda식 사용

# 리스트 내포
aArr = [ i+10 for i in a ]
print(aArr) # [11, 12, 13, 14, 15]

# lambda 식
# map() - 리스트에 모두 동일한 형태를 적용시킬때
aArr = list(map(lambda x:x+10,a)) # list로 변환시켜줘야함
print(aArr) # [11, 12, 13, 14, 15]

# =============

# 재귀함수 - 자신이 자신을 호출 (for문 보다 속도가 느려서 잘 사용 안함)
# 4 * 3 * 2 * 1

result = 1
for i in range(1,5):
  result *= i
print(result) # 24