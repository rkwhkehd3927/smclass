# 1. 학생성적입력
# 이름,국어,영어,수학 -> 번호,국어,영어,수학,합계,평균,등수
# 클래스 1개가 생성이 되고
# 클래스의 참조변수(__str__)로 출력해보시오

# 클래스 생성
class Student: # 객체지향언어 : 객체를 만들어서 해결하겠다라는 언어

  # 변수 3종류 : 
  # 지역변수 - 함수 내에 선언된 변수, 함수가 종료되면 사라짐
  # 인스턴스 변수 - 객체 선언할 때 만들어짐, 각각의 객체마다 변수가 생성됨
  ## 참조변수명.변수명
  # 클래스 변수 - 객체가 선언되지 않아도 만들어짐, 모든 객체가 공통으로 사용
  ## 클래스명.변수명


  # 함수 2종류(공용이라 잘 쓰진 않음)
  # 인스턴스 함수 - 객체 선언할 때 만들어짐, 각각의 객체마다 함수가 생성됨
  ## 참조변수명.함수명
  # 클래스 함수 - 객체가 선언되지 않아도 만들어짐, 모든 객체가 공통으로 사용
  ## 클래스명.함수명
  ### @classmethod : 클래스 함수 표시


  # 객체 선언한 참조변수를 출력하면 주소값이 출력됨
  # 참조변수를 출력해서 원하는 데이터를 출력하려면, __str__ 함수를 사용
  # 리턴값은 무조건 문자열이어야함

  count = 1 # 클래스 변수
  students = []


  # 클래스 함수 선언
  @classmethod
  def stu_print(cls): # 클래스 함수 표시
    for s in cls.students:
      print(str(s))

  # kor = 100 # 클래스 변수 - 클래스명.변수명 에 값 집어넣기
  def __init__(self,name,kor,eng,math): # 1. 생성자
    self.no = Student.count # 클래스 변수 : 클래스명.변수명. # self.no (이 함수안에서 만드는 변수, self. 꼭 넣어줘야함)
    self.name = name # 인스턴스 변수 - 참조변수명.변수명 에 값 집어넣기
    self.kor = kor
    self.eng = eng
    self.math = math
    Student.count += 1
    Student.students.append(self)

  def __str__(self):
    return f"{self.no},{self.name},{self.kor},{self.eng},{self.math}" # 리턴값은 무조건 문자열이어야함

  # no getter를 사용하지 않으면 접근 불가
  # def get_no(self):
  #   return self.no
  # def set_no(self,no):
  #   if no<0: raise "0이하는 입력할 수 없습니다."
  #   self.no = no


# ---------

s1 = Student("홍길동",100,100,90)
# s1.__no = -100
# s1.set_no(100)
# print(s1.get_no())
print(s1)
s2 = Student("유관순",90,90,80)
print(s2)
s3 = Student("이순신",80,100,90)
print(s3)
s4 = Student("김유신",88,100,99)
print(s4)
print("-"*50)

# 클래스 __str__
# print(Student.students[0]) # 1,홍길동,100,100,90 # 한줄 출력함
# print("-"*50)
for s in Student.students:
  print(s)
Student.stu_print()
# Student.students 리스트






# 객체선언
# 참조변수명 = 클래스명():
# print("최초 : ",Student.kor) # 100

# s1 = Student(10)
# print(s1.no) # 10
# Student.kor = 50 # 클래스변수 : Student. 으로 명령하면 모든 kor 변수 값이 다 50으로 바뀜

# s2 = Student(20)
# print(s2.no) # 20

# print("최종 : ", Student.kor) # 50



# ---------

# s1 = Student() # 객체선언
# s1.no = 1
# s1.name = "홍길동" # 참조변수명.변수명 = "홍길동"
# print(s1) # 주소값만 출력
# print(s1.name)

# s2 = Student(2,"유관순")
# print(s2.no)