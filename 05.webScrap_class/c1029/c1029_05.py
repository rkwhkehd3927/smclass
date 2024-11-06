# a = 1
# b = 2

# a_list = [a,b]
# print(type(a_list)) # <class 'list'>

# b_list = [b]
# print(type(b_list)) # <class 'list'>

# tuple을 1개만 지정할 때는 뒤에 ','를 반드시 넣어야함
# a_tuple = (a,b)
# print(type(a_tuple)) # <class 'tuple'>

# b_tuple = (a,)
# print(type(b_tuple)) # <class 'tuple'>

# ==================

# select * from employees where emp_name like '%a%';
# name = "홍길동"
# # 문자 변수 # % 는 값을 할당
# a = '안녕하세요. 이름은 %s'%name
# print(a)

# # format 함수
# print("Hello. my name is {}".format(name))

# # 문자 f함수
# print(f"Hello. my name is {name}")

# ==================

# title = ['e_id','e_name','salary']
# a = [192, 'Sarah Bell', 4000.0]

# print(type(a)) # <class 'list'>
# print(dict(zip(title,a))) # {'e_id': 192, 'e_name': 'Sarah Bell', 'salary': 4000.0}

# =========
title = ['e_id','e_name','salary']
a = [192, 'Sarah Bell', 4000.0]
aa = [
  (196, 'Alana Walsh', 3100.0),
  (125, 'Julia Nayer', 3200.0),
  (180, 'Winston Taylor', 3200.0),
  (194, 'Samuel McCain', 3200.0),
  (138, 'Stephen Stiles', 3200.0)
]

# dict 타입으로 aa 안에 저장하기
a_list = [] 
for i in aa:
  a_list.append(dict(zip(title,i)))
print(a_list)
