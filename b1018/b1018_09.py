# Student 클래스 생성 후
# 데이터를 직접 입력 받아, 클래스 선언 후 저장
# 번호 - 자동 부여, 이름, 국어, 영어,수학, 합계, 평균, 등수
# 클래스 전체 출력
# 클래스 수정

# [ 학생 성적 프로그램 ]
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적수정

class Student:
  
  count = 1
  students = []
  def __init__(self,name,kor,eng,math):
    self.no = Student.count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    Student.count += 1
    Student.students.append(self)

  
  def __str__(self): # input으로 받아서 Student.students에 넣은 객체를 문자열로 바꿔야 print가능
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}"
  

  # 클래스 함수 선언 
  @classmethod
  def stu_print(cls):
    for s in cls.students:
      print(str(s))




# ------------
#### 프로그램 시작 ####

s_title = ['번호','이름','국어','영어','수학','합계','평균'] # 전역변수
s_t = ['no','name','kor','eng','math','total','avg']


while True:
  print("[ 학생 성적 프로그램 ]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  choice = int(input("원하는 메뉴 번호를 입력하세요. >> "))

  if choice == 1:
    print("[ 학생 성적 입력 ]")
    name = input("이름을 입력하세요. >> ")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]} 점수를 입력하세요. >> ")))
    Student(name,*score)

    for s in Student.students:
      print(s)

  elif choice == 2:
    print("[ 학생 성적 출력 ]")
    print(*s_title,sep="\t")
    print("-"*70)
    Student.stu_print()

  elif choice == 3:
    print("[ 학생 성적 수정 ]")
    print("1. 국어")
    print("2. 영어")
    print("3. 수학")
    name = input("찾고자 하는 학생의 이름을 입력하세요. >> ")

    flag = 0
    for s in Student.students:
      if name == s.name: # s.name : 참조변수명.변수명
        print(f"{name}학생을 찾았습니다.")
