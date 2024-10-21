students = []
s_title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
choice = 0 # 전역변수
stuNo = 0 # 학생번호
stuNo = len(students) # 아래에서 리스트에 학생이 생기면, 그 인원수로 변경시켜줘야하기 때문
no=0; name=""; kor=0; eng=0; math=0; total=0; avg=0; rank=0 # 성적처리변수 # 함수처리 할거라서 미리 선언


while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == "1":
    print(" [ 학생 성적 입력 ] ")
    while True:
      no = stuNo + 1
      name = input("이름을 입력하세요. (상위이동 : 0) ")
      if name == "0":
        print("메뉴화면으로 이동합니다.")
        break
      kor = int(input("국어점수를 입력하세요. "))
      eng = int(input("영어점수를 입력하세요. "))
      math = int(input("수학점수를 입력하세요. "))
      total = kor+eng+math
      avg = total/3
      rank = 0 
      students.append([no,name,kor,eng,math,total,avg,rank])
      stuNo += 1 # 학생수 1 증가
      print(f"{name} 학생의 성적이 저장되었습니다.")
  elif choice == "2":
    print("[ 학생 성적 출력 ]")
    for title in s_title:
      print(f"{title}\t",end="")
    print() # 줄단락바꾸기?
    print("-"*60)
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
    print()


  elif choice == "0":
    print("[ 프로그램 종료]")
    print("프로그램을 종료합니다.")
    break

