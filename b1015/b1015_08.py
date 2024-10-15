from urllib import request

target = request.urlopen("http://www.google.com") 
output = target.read() # 웹 스크래핑 # 페이지 소스 전부 불러오기
print(output)



# ----------------------------------------------------------------
# from SS import * # 모듈 파일에서 함수 호출
# import SS # 변수,함수 모두 가져옴
# import math 
# from math import *
# import math as m # 함수호출 앞에 m. 만 붙여도 됨

# 메인파일에 students(중요데이터) 가 있을 경우 함수 호출시 매개변수를 넣어줘야하지만
# 모듈파일에 students(중요데이터) 가 있을 경우 함수 호출시 매개변수 필요없음

# students 리스트 타입
# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
#   {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
#   {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
#   {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
#   {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
# ]


# SS.py 모듈 함수 호출

# stu_output(students)
# print(SS.s_title)
# print(students)
# print(m.floor(1.23)) # 버림
# print(m.ceil(1.23)) # 올림
# print(m.round(1.23)) # 반올림

# time.sleep() # 지정한 시간 동안 멈추기