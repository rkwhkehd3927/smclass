# class 생성
class Car:

  def __init__(self,color,tire,gear,speed):
    self.color = color
    self.tire = tire
    self.gear = gear
    self.__speed = speed

  # color = "흰색"
  # speed = 0

  def upSpeed(self,value):
    if value > 0: self.__speed += value
    else:
      raise "값을 잘못 넣었습니다."
  
  def downSpeed(self,value):
    self.__speed -= value

c1 = Car("흰색",4,"auto",0)
c1.color = "블루"
print(c1.color)
c1.__speed = 300
print(c1.__speed)

# 클래스 사용하려면 클래스 선언!! 을 꼭 해야함
# c1 = Car()
# print(c1.color) # 흰색S
# print(c1.tire)

# 속도 = 0 -> 100

# c2 = Car()
# c2.color = "빨강"
# print(c2.color)
# print(c1.color)

# speed 변수에 직접 값을 할당
# 리스트, 딕셔너리 변수에 직접 값을 할당하는 방식
# c1.speed = 100
# print(c1.speed)

# 함수를 활용해서 값을 할당(보통 이렇게 씀)
# c1.upSpeed(100)
# print(c1.speed) # 100