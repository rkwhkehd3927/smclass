
# 1. 함수 선언 - 기본 매개 변수
def func(num1,num2):
  print(num1)
  print(num2)

# 함수 호출
func(10,20)

# 함수의 매개변수 개수를 정확히 맞춰야 에러가 나지 않음
# func(10,20,30) # error
# func(10) # error

# 2. 함수 선언 - 가변 매개 변수
def func(*num): # tuple type
  print(num)
# 개수를 맞추지 않아도 알아서 맞춰줌
# 함수 호출
func(10)
func(10,20)
func(10,20,30)