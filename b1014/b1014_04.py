# 함수선언
def calc(num,num2,op):
  if op == "+":
    result = num+num2
    return num+num2
  elif op == "-":
    result = num-num2
    return num-num2
  elif op == "*":
    result = num*num2
    return num*num2
  elif op == "/":
    result = num/num2
    return num/num2


num = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))
op = input("+,-,*,/ 중 하나를 선택하세요.")


print("결과값 : ", calc(num,num2,op))