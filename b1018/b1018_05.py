class Circle:
  def __init__(self,length):  
    self.__length = length # 내부클래스에서만 변수에 접근하여 수정가능

  # 원의 넓이 
  def get_area(self):
    return 3.14 * self.__length**2
  # 원의 둘레
  def get_circum(self):
    return 3.14 * 2 * self.__length

  # getter, setter
  def get_length(self):
    return self.__length
  def set_length(self,length):
    self.__length = length

  # 참조변수를 출력할 때 리턴되는 함수 : __str__()
  def __str__(self):
    c_str = "원의 반지름 : {}, 원의 넓이 : {}, 원의 둘레 : {}".format(self.__length,self.get_area(),self.get_circum())
    return c_str

# 클래스 선언
# "__" 내부적으로 캡슐화하겠다고 선언
# c1 = Circle(10)                         # 1. 선언 - 값을 입력
# print("c1 길이 : ",c1.get_length()) ## 10  # 2. getter 값 출력
# c1.set_length(200)                     # 3. setter 값 입력
# print("c1 길이 변경 : ",c1.get_length()) ## 200  # 4. getter 값 출력
# c1.__length = 100 # 변경                        # 5. 변수 직접입력
# print("직접 변경 : ",c1.__length) ## 100         # 6. 변수 직접출력
# print("get 읽어온 length : ",c1.get_length()) ## 200    # 7. getter 값출력

c1 = Circle(10)
print(c1)