# 함수사용
# def calc(num,num2):
#   print(f"두 수 더하기 : {num+num2}")
#   print(f"두 수 빼기 : {num-num2}")
#   print(f"두 수 곱하기 : {num*num2}")
#   print(f"두 수 나누기 : {num/num2}")

# num = [10,20,30]
# num2 = [5,7,3]

# for i in range(len(num)): # len(num) = 3
#   calc(num[i],num2[i])


# for문을 활용한 계산
# for i in range(len(num)): # len(num) = 3
#   print(f"두 수 더하기 : {num[i]+num2[i]}")
#   print(f"두 수 빼기 : {num[i]-num2[i]}")
#   print(f"두 수 곱하기 : {num[i]*num2[i]}")
#   print(f"두 수 나누기 : {num[i]/num2[i]}")

# -----------------------------------------

# num = int(input("숫자를 입력하세요."))
# num2 = int(input("숫자를 입력하세요."))

# def calc(r_num,r_num2,r_num3): # 2. 여기도 2개여야함
#   print(f"두 수 더하기 : {num+num2}")
#   print(f"두 수 빼기 : {num-num2}")
#   print(f"두 수 곱하기 : {num*num2}")
#   print(f"두 수 나누기 : {num/num2}")

# numStr = input("숫자를 입력하세요.(12,5)") # 12,5
# numStr2 = numStr.split(",") # 리스트로 나눠주기 # 문자열 타입

# 문자열을 숫자로 변경하여 num,num2에 넣어야함
# num = numStr2[0] # 문자열 -> 숫자형
# num2 = numStr2[1]

# calc(num,num2)  # 1. 여기서 매개변수가 2개이면 


# 3개의 숫자를 입력받아 숫자를 계산하시오. 12,5,3

# def calc(r_num,r_num2,r_num3): # 2. 여기도 2개여야함
#   print(f"세 수 더하기 : {num+num2+num3}")
#   print(f"세 수 빼기 : {num-num2-num3}")
#   print(f"세 수 곱하기 : {num*num2*num3}")
#   print(f"세 수 나누기 : {num/num2/num3}")

# def calc(numStr2): # 배열
#   s1 = 0
#   s2 = 0
#   for i in range(len(numStr2)):
#     s1 += numStr2[i]
#     s2 -= numStr2[i]
#     s3 *= numStr2[i]
#     s4 /= numStr2[i]
#   print(f"두 수 더하기 : {s1}")
#   print(f"두 수 빼기 : {s2}")
#   print(f"두 수 곱하기 : {s3}")
#   print(f"두 수 나누기 : {s4}")

# numStr = input("숫자 세개를 입력하세요.(12,5,3)")
# numStr2 = numStr.split(",")
# numStr3 = [int(i) for i in numStr2 ] # 리스트 내포 
# print(numStr2)
# calc(numStr2)

# r_num = int(numStr[0])
# r_num2 = int(numStr[1])
# r_num3 = int(numStr[2])

# ----------------

# def calc(*n): # 가변 매개변수
#   print(n)
#   print (len(n))

# calc(1,2,3,4,5,6,7)

# # 기본 매개변수 - 매개변수의 개수가 동일
# def calc(n1,n2):
#   print(n1,n2)
# calc(1,2)

# # 키워드 매개변수
# # def calc(n1 = 10,n2 =20):
# #   print(n1)
# #   print(n2)

# calc() # 매개변수가 없으면 기본값으로 출력됨
# calc(20) # n1) 20,20 # 키가 없으면 무조건 1번째로 전달이 됨
# clac(300) # 키가 없으면 무조건 1번째로 전달이 죔
# clac(n2=100) # 키가 있으면 키값으로 전달이 됨.

# print(1,2,3,sep="$",end="\t") # 가변매개변수
# print("안녕")

# -------------
# 함수 내에 선언된 변수는 (함수라는 지역외에) 외부에서 사용할 수 없음
# def calc(v1,v2):
#   global sum # 전역변수
#   # sum = 0 # 지역변수
#   for i in range(v1, v2+1):
#     sum += i
#   # return sum # return 이 있어야함 값이 밖으로 나갈 수 있음(?)

# sum = 100 # 외부의 변수를 사용해서 함수안에서 계산을 하고 싶을 경우 함수 안에 'global'
# sum = calc(1,10)
# print(sum)

# -----------


# def calc(n1,n2):
#   s1 = n1+n2
#   s2 = n1-n2
#   s3 = n1*n2
#   s4 = n1/n2
#   s5 = [s1,s2,s3,s4]
#   return s5


# s5 = calc(10,5)
# # print(s1)
# # print(s2)
# # print(s3,s4)
# print(s5)
# print("프로그램 종료")

# ~~~~~~~~~~~~~
# 매개변수가 일반변수일 경우 return 하지 않으면 변수값이 변동 없음
# hh = 100

# def add(hh):
#   hh = hh +100
# add(hh)
# print(hh)


# def add(h):
#   for i in range(len(h)):
#     h[i] = h[i]+100


# kim = []
# kim = hong
# kim[0] =100
# print(hong)


# 복합매개변수 - 리스트, 딕셔너리
# hong = [1,2,3,4,5]

#### 매개변수가 복합변수일 경우, return이 없어도 값이 변경되어 전달됨

# def add(h):
#   for i in range(len(h)):
#     h[i] = h[i]+100 # 리턴 안했음

# add(hong)
# print(hong)

# ============================

# 전역변수인 경우 함수 내에서도 사용이 가능하고, 함수외부에서도 사용이 가능함
# 지역변수는 return 없이는 값이 함수 밖으로 나오지 못함
def calc():
  global sum  # 전역변수인 경우, 함수에서 변경시 외부에서도 같이 변경됨. # sum = 10
  sum = 200

sum = 10
calc() # 함수에서 sum이 200으로 변경됨
print(sum) # 결과값 : sum이 200 이됨