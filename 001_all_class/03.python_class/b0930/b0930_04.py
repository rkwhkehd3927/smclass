# var1 = 100
# var2 = var1
# var3 = var2
# var4 = var3
# print(var4)

# v4 = v3 = v2 = v1 = 10
# print(v4)

# name = "홍길동"
# print(type(name))

# level = '3레벨'
# print(type(level))

# n = 3.14
# print(type(n))

# num = 100
# print(type(num))

# a_bool = True # True or False 는 대문자로 넣어야함.
# print(type(a_bool))


# name, kor, eng, math, total, avg 출력
# a = '100'
# b = "200"
# print(type(a))
# print(type(b))

# print(a+b) # 문자 연결 연산자 100 200
# print(int(a)+int(b)) # 타입변경

# name = "홍길동"
# print(int(name)) # error - 문자를 숫자로는 변경 불가, 문자숫자는 가능

# c = "3.14"
# print(int(float(c))) # 실수형으로 변경 후 다시 정수형으로 변경
# print(int(c)) # 문자 실수형은 바로 정수형으로는 변경 안됨 
# print(str(c)) # 실수형을 문자열로 변경

# d = "True"
# print(bool(d)) # 문자 bool 형을 bool형으로 변경

# 타입 변경 - str, float, int, boolS


# input으로 홍길동, 100, 100, 99을 입력을 받아
# 이름, 점수, 합계, 평균을 소수점 2자리 까지 1줄에 출력하시오.
# format 사용, f함수

name = input("이름을 입력하세요.")
kor = input("국어점수를 입력하세요.")
# kor = int(input("국어점수를 입력하세요."))
eng = input("영어점수를 입력하세요.")
math = input("수학점수를 입력하세요.")

total = int(kor)+int(eng)+int(math)
avg = total/3

print("{} {} {} {} {} {:.2f}" .format(name,kor,eng,math,total,avg))
print(f"{name},{kor},{eng},{math},{total},{avg:.2f}")