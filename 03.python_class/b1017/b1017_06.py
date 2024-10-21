# a = ['20', 'alibreyj', '63', '94', '67', '224', '74.6666666667', '1.0']
# b = ['20', '63', '94', '67', '224', '74.6666666667', '1.0']
# c = []

# b의 리스트 float 변경
# b의 형태가 모두 숫자이기 때문에 float으로는 변경 가능
# for i in b:
#   c.append(float(i)) # [20.0, 63.0, 94.0, 67.0, 224.0, 74.6666666667, 1.0]
# print(c)

# # try-except구문을 사용해서 정수, 실수 구분
# def t_float(n):
#   try:
#     int(n)
#     return True # 에러없으면 True 내보내기
#   except:
#     return False # 에러없으면 False 내보내기
  
# # 문자열인지 아닌지 구분
# for idx,i in enumerate(a):
#   if i.isdigit():
#     print(f"{idx}번째 {i}는 숫자입니다.")
#   else:
#     print(f"{idx}번째 {i}는 문자입니다.")

# # 정수로 변경
# for i in b:
#   if t_float(i):
#     i = int(i) # True로 돌아오면 정수형으로 내보내기
#   else:
#     i = float(i) # False로 돌아오면 실수형으로 내보내기
#   c.append(i) # error # '74.6666666667' 요거는 int 로 바꿀 수 없음
# print(c) 

# -------

a = ['20', 'alibreyj', '63', '94', '67', '224', '74.6666666667', '1.0']
b = ['20', '63', '94', '67', '224', '74.6666666667', '1.0']
t_title = ['no','name','kor','eng','math','total','avg','rank']
students = []

def f_float(value):
  if value.isdigit(): # 정수인지, / 실수, 문자열인지
    return int(value)
  else:
    try:
      return float(value) # 실수일때 실수로 변환 리턴
    except:
      return value # 문자열일때 문자열 그대로 리턴

# 숫자로만 구성 - 정수, 실수
for idx, value in enumerate(b):
  if value.isdigit(): # isdigit - 정수이면 True, 실수이면 False
    print(f"{idx}번째 {type(int(value))}")
  else:
    print(f"{idx}번째 {type(float(value))}")

# 문자열,정수,실수로 구성
c = []
for idx, value in enumerate(a):
  c.append(f_float(value))

# students 리스트에 딕셔너리로 저장
students.append(dict(zip(t_title,c)))
print(students)