class Student:
  # no = 0  # 인스턴스 변수 : 객체 선언을 하면 변수는 개별적으로 생성됨
  count = 0   # 클래스 변수 : 모든 객체가 동일한 변수를 사용 (거의 사용 안하긴 함)
  students = [] # 클래스 리스트

  def __init__(self,name,kor,eng,math):
    Student.count += 1
    self.no = Student.count # 클래스 변수 - 공용으로 변수를 사용
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0
    # 클래스 리스트에 추가
    Student.students.append(self)
  
  # 객체를 문자열로 리턴 함수 : 리턴이 항상 문자열이 되어야함
  def __str__(self):
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"
  
  def print(self): # 딕셔너리 타입으로 리턴
    return {"no":self.no,"name":self.name,"kor":self.kor,"eng":self.eng,\
            "math":self.math,"total":self.total,"avg":self.avg,"rank":self.rank}
  
  # 클래스 함수 선언
  @classmethod # 클래스 함수표시
  def stu_print(cls):
    for s in cls.students:
      print(str(s))


#### 프로그램 시작 ####
# s1 = Student()
# s1.students
# s2 = Student()
# s2.students

# s1 = Student("홍길동",100,100,90)
# print(s1.name)
# print("s1.count : ",s1.count) # 1
# s2 = Student("유관순",90,100,99)
# print(s2.name)
# print("s2.count : ",s2.count) # 2
# print("s1.count : ",s1.count) # 2


# students리스트 딕셔너리로 저장
# students = []
# s1 = Student("홍길동",100,100,90)
# print(s1.print())
# students.append(s1.print())
# s2 = Student("유관순",90,80,90)
# print(s2.print())
# students.append(s2.print())

# 클래스 - 변수,함수의 집합체
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] # 전역변수
s_t = ['no','name','kor','eng','math','total','avg','rank']

# students리스트 딕셔너리로 저장 
students = []
s1 = Student("홍길동",100,100,90)
# print(s1) # 0x000 -> __str__() 문자열로 정의된 형태로 출력

while True:
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 홍길동, 유관순 비교")
  choice = int(input("원하는 번호를 입력하세요. >> "))

  if choice == 1:
    print("[ 학생성적 직접입력 ]")
    name = input("이름을 입력하세요. >> ")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]} 점수를 입력하세요. >>")))
    Student(name,*score) # 전개연산자

    # 클래스 변수 접근 방법
    for s in Student.students:
      print(s)
    # print(s1.students[0])


    # 인스턴스 변수 : 참조변수.변수명, 참조변수명.함수명
    # 클래스 변수 : 클래스명.변수명, 클래스명.함수명
    # s1 = Student(name,*score) # 전개연산자 # *score = score[0],score[1],score[2]
    # s2 = students.append(Student(name,*score)) # Class 를 저장 

  elif choice == 2:
    print("[ 학생성적 출력 ]")
    print(*s_title,sep="\t")
    print("-"*70)
    Student.stu_print() # 클래스 함수 호출

  elif choice == 3: # 홍길동 학생 합계, 유관순 학생 합계
    s1 = Student("홍길동",100,100,90)
    s2 = Student("유관순",90,100,90)
