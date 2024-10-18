# 절차적인 형태의 프로그램 규현
# 반지름을 입력받아, 원의 둘레와 넓이를 출력하시오.
# 넓이 : 3.14 * 반지름 * 반지름
# 둘레 : 3.14 * 2 * 반지름


# length = int(input("반지름을 입력하세요. >> "))
# print("넓이 : ", 3.14*length**2)
# print("둘레 : ", 3.14*2*length)

# 클래스 생성
class Circle:
  def __init__(self,length): # 생성자
    self.__length = length # 변수에 직접적으로 접근제한 : "__"
  
  # 원의 넓이 
  def get_area(self):
    return 3.14 * self.__length**2
  # 원의 둘레
  def get_circum(self):
    return 3.14 * 2 * self.__length
  # length = 0

# 클래스 선언
c1 = Circle(int(input("반지름을 입력하세요. >> ")))
c1.__length = 5 # 클래스 생성->함수안에 "__" 로 '변수 직접할당' 에 대한 접근제한을 걸어놓으면 이런식으로 값을 직접 할당해도 적용안됨
print("넓이 : ",c1.get_area())
print("둘레 : ",c1.get_circum())

c2 = Circle(int(input("반지름을 입력하세요. >> ")))
print("넓이 : ",c2.get_area())
print("둘레 : ",c2.get_circum())
# print(c1.length)
