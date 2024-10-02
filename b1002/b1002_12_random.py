import random

# 랜덤숫자 생성 - random
# random() : 0<= x <1 의 실수값을 추출해줌, 소수점 16번째자리까지.
# 0-9
print(random.random()) 
print(int(random.random()*10)) # 0-9 까지의 랜덤 숫자 
# 1-10
print(int(random.random()*10)+1) # 1-10 까지의 랜덤 숫자 

# randint - 랜덤 int 추출 1-10 (10 포함)
print(random.randint(1,10)) # 1-10까지 중 랜덤 숫자 추출

# randrange - 랜덤 범위 추출 - 1,3사이(3 포함하지 않음)
print(random.randrange(1,3)) # 1-3까지 범위 중 무작위 추출

# choice - 리스트를 활용한 랜덤 추출 (1개)
a = [1,4,5,9]
print(random.choice(a))  # a 안 숫자 중 하나 랜덤 추출

# choices - 리스트에서 여러개 랜덤 추출 (중복 추출 가능)
print(random.choices(a,k=2)) # k=2 이므로 2개 추출
print(random.choices(a,k=3)) # k=2 이므로 2개 추출

# sample - 리스트에서 여러개 랜덤 추출 (중복 추출 불가)
print(random.sample(a,2)) # 2개 추출
