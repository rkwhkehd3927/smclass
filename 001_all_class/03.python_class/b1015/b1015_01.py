# 함수선언
# def calc(st,end):
#   # 구구단
#   for i in range(st,end+1): 
#     print(f"[ {i}단 ]")
#     for j in range(1,10):
#       print(f"{i}x{j}={i*j}")
  

# # 2-9단
# st = 2
# end = 9
# calc(2,9) # 함수호출

# # 3-7단
# st = 3
# end = 7
# calc(3,7) # 함수호출

# # 5-9단
# st = 5
# end = 9
# calc(5,9) # 함수호출

# =========================

# 함수 - 기본매개변수,가변매개변수,키워드매개변수

# 1. 함수 - 기본매개변수
# def plus(n1,n2): # 함수선언
#   sum = n1 + n2
#   print("합계 : ", sum)

# # 함수호출 - 매개변수의 갯수를 정확히 맞춰줘야함
# plus(10,20)


# ~~~~~~~~
# 2. 함수 - 가변매개변수 (*n1)
# def plus(*n1): # 2개를 넘겨줘도 1개를 출력가능(갯수상관없이 모두 받을수있는 형태)
# def plus(a,*n1): # a = 1 , *n1 = 2,3,4,5,6,7,8,9,10 / 기본매개변수와 함께 함께쓸 수 있으나 기본매개변수를 앞쪽에 배치해야함
#   print("a : ",a) # *n1을 먼저배치하면 *n1에 먼저 다 배치되어버려서 에러가 남
#   for i in n1:
#     print(i)
#   print(type(n1)) # tuple
# # tuple - 수정이 불가능한 리스트

# plus(1,2,3,4,5,6,7,8,9,10) # 이거를 갯수에 상관없이 *n1 이 하나의 리스트형태로 전부 받음


# ~~~~~~~~
# 3. 함수 - 키워드 매개변수
# def plus(k=10,m=5): # 값을 미리 할당해줌
#   print("k :",k)
#   print("m :",m)

# plus() # 기본매개변수는 매개변수 개수가 일치하지 않으면 에러가 나는데, 키워드 매개변수는 상관없음
# #   ↑ 여기에 데이터가 들어오지 않으면 k=10,m=5 을 사용하게됨

# plus(1) # k=1 m=5
# plus(m=1,k=2) # 순서가 바꿔서 넣어도 됨


# ~~~~~~~~~~

# print(1,2,3,4,5,sep=" ", end="\n") # 1,2,3,4,5 - 가변형매개변수, sep=" ", end="\n" - 키워드매개변수
# print(1)
# 키워드매개변수를 뒤에 배치


# 함수 - 가변형매개변수, 키워드매개변수 동시 사용시 키워드매개변수를 무조건 뒤에 배치, 안그럼 에러남
def plus(*n,k=10): # *n = 1,2,3,4,5
  print("k :", k) # k=10
  for i in n:
    print(i)

plus(1,2,3,4,5,k=50) # *n으로감
# plus(k=10,1,2,3,4,5) # error
