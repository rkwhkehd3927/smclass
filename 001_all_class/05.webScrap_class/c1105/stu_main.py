# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# 4. 학생성적정렬
# 5. 등수처리
# students 테이블을 사용하여 
# 시퀀스 students_seq 생성
# 번호,'김유신',99,98,96,합계,평균,등수 입력일(sdate) 까지 입력하여 생성

import oracledb
import stu_func


while True:
  choice = stu_func.main_print() ## 메인 화면 출력

  if choice == "1":
    stu_func.stu_insert() ## 학생성적 입력

  elif choice == "2":
    stu_func.stu_output() ## 학생 성적 출력

  elif choice == "3":
    stu_func.stu_search() ## 학생 성적 검색

  elif choice == "4":
    stu_func.stu_desc() ## 학생 성적 정렬
 
  elif choice == "5":
    stu_func.stu_rank() ## 등수 처리

  elif choice == "0":
    print("프로그램을 종료합니다.")
    break
