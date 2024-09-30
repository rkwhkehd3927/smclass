#  10은 2의 배수입니다. 
# print("%d는 %d의 배수입니다." % (10,2))
# a = 10
# b = 2
# print(a+"은 "+b+"의 배수입니다.") # 이렇게 하면 에러남
# print(a,b)

# 출력 자리수
# print("%d" % b)
# print("%5d" % b) # 5자리의 공간 확보
# print("%05d" % b) # 공백 5자리의 0으로 채우기

# 001 010 100.00 3번 프린트를 사용해서 출력
# num1=1
# num2=10
# num3=100
# print("%03d" % num1)
# print("%03d" % num2)
# print("%.2f" % num3)
# print("%03d %03d %0.2f" % (num1, num2, num3))

# print("%5d" % (-10))


# 10*2=20
# print("%d * %d = %d" % (a,b,a*b))

# 사용표시 - %s: 문자열, %c: 문자 1개. %f: 실수, %d: 정수
# name = "홍길동"
# kor = 100
# eng = 100
# math = 99
# 홍길동 총합 : 299, 평균 : 99.3333
# print("%s 총합 : %d, 평균 : %.2f" %(name,kor+eng+math,(kor+eng+math)/3))


# 자리수 표시
# print()



#### print 사용 형태 ####
# print 1. 쉼표, %, .format, f
# print(a,"은",b,"의 배수입니다.") # 쉼표로 구분하여 출력
# print("%d은 %d의 배수입니다." % (a,b)) # %
# print("{}은 {}의 배수입니다." .format(a,b)) # .format 중괄호 사용
# print(f"{a}은 {b}의 배수입니다.") # f


# 소수점 둘째자리까지 출력
num1 = 758.12345678
print("%.2f" % num1)

# 총 10자리, 빈칸은 0으로 채워 소수점 2자리까지 출력
num2 = 25.05
print("%010.2f" % num2)
print("%013.2f" % num2) # 소수점도 한자리를 차지함

# 변수 150.15를 정수, 실수, 문자열로 출력
num3 = 150.15
print("%d" % num3)
print("%f" % num3)
print("%s" % num3)

# *dmf 10개 출력
num4 = "*"
print(num4 * 10)

# print("숫자 :" +10) # 타입이 다른 것끼리 "+" 할 수 없음
print(10+10)
print("안녕"+"hello")
print("숫자 :" ,10,20,0.5,"이상") # 다른 타입끼리는 쉼표로 구분
print("-"*20)
print("-------------")
print("%5.1f" % (123456789.123)) # 양수부분은 자리수와 관계없이 전부 출력
