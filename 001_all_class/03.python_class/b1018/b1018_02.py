# class 생성방법

# 학생 1명 정보
# 번호,이름,국어,영어,수학,합계,평균,등수
# 학생 클래스 설계도 생성
class Student: # 클래스는 첫글자 대문자로 입력
  # 생성자
  # def __init__(self): # 기본 생성자
  #   None
  def __init__(self,no,name,kor,eng,math): # 매개변수가 있는 생성자
    self.no = no
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0

  def print(self):
    print(f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}")
  

# 클래스 사용방법
# 클래스 선언

# 클래스명.변수명 = 값 : 변수가 생성되어 클래스에 변수가 저장됨.
# 기본 생성자를 사용해서 값을 개별적으로 입력
# s1 = Student()
# s1.no = 1
# s1.name = "홍길동"
# s1.kor = 100
# s1.eng = 100
# s1.math = 100

# 매개변수가 있는 생성자를 
s1 = Student(1,"홍길동",100,100,100)
# print(s1) # 주소값이 출력됨.
s1.print()
# print(s1.no,s1.name,s1.kor,s1.eng,s1.math,s1.total,s1.avg,s1.rank)


# s2 = Student()
# s2.no = 2
# s2.name = "유관순"
# s2.kor= 100
# s2.eng= 100
# s2.math= 100

# sutdents[0]
# s1



# 전체학생리스트 정보
# class Students:
#   pass