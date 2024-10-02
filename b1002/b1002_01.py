# input_str = input("글자를 입력하세요.")

# 문자가 입력되지 않았을 때
# if input_str == "":
#   print("글자를 입력하셔야 합니다.")

# if input_str != "": # 빈공백이 아니냐?
#   print("입력문자 : ",input_str)
#   print("프로그램이 종료됩니다.")
# else: 
#   print("글자를 입력하셔야 합니다.")



# 문자열

# 문자열 숫자
a = "123"
# int(a)  # 숫자형으로 타입이 바뀜
print(type(a))
print(type(int(a)))
print(type(float(a)))

b = "12.3"
# print(type(int(b))) # 에러 - 소수점이 있는 "문자열 숫자"는 int가 아닌 float 으로 변경해야함
print(type(float(b))) 

s1 ="안녕"
s2 ="안녕하세요"
print(s1+s2)
print(a+b) # 문자열 연결 연산자
# print(a*b) # 에러 - 문자열은 -,* 안됨

# 문자열 *2 # 문자열 반복 연산
print("안녕"*10)
print("-.-"*30)


# 문자열 슬라이싱
str1 = "안녕하세요. 반갑습니다." # 문자열 자체를 리스트 형태로 보는 것
print(str1[0]) # 해당번호 넣으면 해당되는 문자출력
print(str1[7])
print(str1[2:5]) # 2-4 까지 출력 가능, [시작점:끝점 한칸 뒤]
print(str1[:5]) # [처음:끝점 한칸 뒤]
print(str1[2:]) # [시작점:끝까지]
print(str1[1:10:2]) # [시작점:끝점 앞:2칸씩]
print(str1[1:10:3]) # [시작점:끝점 앞:3칸씩]
print(str1[::-1]) # [처음:끝까지:역순으로]


# [] - 배열 : 배열은 한 번 범위가 정해지면 수정이 불가능 : c, 자바
# [] - 리스트 : 범위상관없음 



c = 12.3
print(type(int(c))) # 실수는 int로 타입 변경 가능
print(int(c))

