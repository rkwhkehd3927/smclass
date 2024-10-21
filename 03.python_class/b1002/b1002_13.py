import random # 항상 이걸 먼저 선언해야만 랜덤 추출 가능
aArr = []
# 0-9까지 10개의 랜덤 숫자 추출해서 aArr 안에 10번 추가하시오.
# 같은 숫자가 있으면 제외하고 입력해보세요.

# for i in range(10): # i를 10번 할거임 / range() = 범위
#   r_num = random.randint(0,9) # r_num은 0-9사이의 랜덤한 숫자
#   if r_num not in aArr: # 여기서 나온 숫자가  ## 중복 숫자가 없을때 추가시켜야하기 때문에 "not" 으로 물어봐야함
#     aArr.append(r_num) # 여기서 또 나온다는 보장이 없기 때문에 변수 선언(r_num)
# print(aArr)
# 중복이면 추가가 안되기 때문에 10개가 채워지지 않을 확률이 높음
# for 문에서는 i += 1 필요없음 반복시키기 때문...?


# i = 0 # = count?
# while i<10: # 무조건 10개(i=10)일 때만 종료
#   r_num = random.randint(0,9) # 0-9 사이의 랜덤한 숫자
#   if r_num not in aArr: # 만약 aArr 안에 r_num이 없으면(0-9 사이의 랜덤한 숫자 중복이 아니면)
#     aArr.append(r_num) # aArr에 r_num(랜덤 추출된 숫자)를 추가해라
#     i += 1 # i+1 : 다음 횟수 카운트?

# print("aArr 개수 : ",len(aArr))
# print(aArr)



# 나 혼자 해보기
i = 0
while i<10:
  r_num = random.randint(0,9)
  if r_num not in aArr:
    aArr.append(r_num)
    i += 1 # 얘가 if 문 밖으로 나오면 10개가 안채워짐 
print("aArr 개수 : ",len(aArr))
print(aArr)