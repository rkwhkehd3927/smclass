# 함수 - 매개변수(일반변수, 복합변수) #### 1번과 3번 외우기

# 1. 함수 일반매개변수 - return이 아니면 값이 함수 밖으로 나올 수 없음 # 대부분(90%는) 이렇게 씀
# def calc(h):
#   h += 100
#   return h # 일반변수는 return 이 없으면 None

# h = 20
# h = calc(h) # 값 : 120 # 호출만 하고 일반변수 값(h =) 을 넣어주지 않으면 값이 변경되지 않음
# # calc(h) # 값 : 20 # 호출만 하면 값이 변경되지 않음
# print(h)


# 2. 전역변수 - "일반매개변수" : return 없이 함수 밖으로 값을 사용할 수 있음 
# def calc():
#   global h # global일때만 h에 20이 할당됨 # 근데 웬만하면 global 함수는 잘 쓰지 말라고함ㅋㅎ # 누가 변경했는지 잘모르기 때문
#   h += 100

# h = 20 # 전역 변수
# calc() # 함수 호출 후 h에 값을 할당할 필요 없음
# print(h) # 120


# 3. 함수 복합매개변수 - return 없이 함수 밖의 값을 사용
# def calc(hArr):
#   for i in range(len(hArr)):
#     hArr[i] += 100

# hArr = [1,2,3,4,5] # 복합변수 - 변수에 주소값이 저장됨
# calc(hArr)
# print(hArr)

# ==========================
a = 10 # 전역변수

def calc(a):
  a += 10
  print(a)

calc(a)