# stu_print() # 모듈
# if choice == "1":
#   stu_input()
# elif choice == "2":
#   stu_output()
# elif choice == "3":
#   stu_update()

# ---------------------------------

# aArr = [1,2,3,4,5]
# a_list = []
# # 1줄 for 문으로 a_list = [1,4,9,16,25]
# a_list = [i*i for i in aArr]
# print(a_list)


# # 1-20 중에 3의 배수만 리스트에 추가하시오
# a_list = []
# for i in range(1,21):
#   if i%3 == 0:
#     a_list.append(i)
# print(a_list)

# # 리스트 내포
# # [ 값, for문, 조건식 ] - 한줄 조건문일때 가능
# b_list = [ i for i in range(1,21) if i%3 == 0]
# print(b_list)

# ---------------------------------
#### 있다, 없다 확인하기

# 단어 '타입' 찾기
ss = "파이썬 수업중 타입 문자열 타입, 정수형 타입, 실수형 타입, 논리형 타입이 있습니다"
i_str = input("글자를 입력하세요.")
# if i_str in ss:
#   print("있습니다.")
# else:
#   print("없습니다.")

# 위치값 - find 없을때 -1
# idx = ss.find(i_str)
# print("위치값 : ", idx)
# index - 위치값이 없을때는 에러
# idx = ss.index("위치 : ", i_str)
# print("위치값 : ", idx)


# 검색 글자 개수 
# idx = ss.count(i_str)
# print("개수 : ", idx)


# 타입의 위치값을 모두 출력하시오
idx = 0
search = "타입"
a_list = []
for s in range(5): # ss.count("타입") = 5
  # idx = ss.find("타입")+1 # 8
  num = ss.find(search,idx) # 0 번 부터 시작 - 8,15,23,31,39
  a_list.append(num)
  # print(ss.find("타입"),idx) # 15
  print(num)
  idx = num+1

print(f"검색개수 : {len(a_list)}, 위치값 : {a_list}")


# ---------

sss = ss.replace("타입","atype") # 글자 대체 / "타입" -> "atype"
print(sss)
# 파이썬 수업중 atype 문자열 atype, 정수형 atype, 실수형 atype, 논리형 atype이 있습니다

a_str = "파이썬"
a = "-".join(a_str) # 글자 사이사이에 넣기 / 파-이-썬
print(a)