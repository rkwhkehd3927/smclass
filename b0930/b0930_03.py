# name = "홍길동"
# num = 100
# num2 = 100
# num3 = 99
# print("%s 합계 : %d" %(name,num+num2+num3))
# print("{} 합계 : {}".format(name,num+num2+num3))
# print("%s 평균 : %.2f" %(name,(num+num2+num3)/3))
# print("{} 평균 : {:.2f}".format(name,(num+num2+num3)/3))


# 숫자 : 12.12345, 456.78940, 2.252525
# 소수점 2자리 출력
# 숫자 : 12.12, 456.79, 2.25
# print("{:.2f} {:.2f} {:.2f}".format(12.12345, 456.78940, 2.252525))

# print("\"") # 특수문자 앞에 \를 넣으면 특수문자도 출력 가능
# print("안녕\n하세요.") # 줄단락바꾸기
# print("안녕\t하세요.") # tab
# print("안녕\b\b하세요.") # backspace

# print("오타니는 30일(이하 한국시간) 미국 콜로라도주 쿠어스필드에서 열린 콜로라도 로키스와의 2024 메이저리그 원정경기에서 \n 1번 지명타자로 선발 출전, 4타수 1안타 1도루를 기록했다.")
# print("""
# 오타니는 30일(이하 한국시간) 미국 콜로라도주 쿠어스필드에서 열린
# 콜로라도 로키스와의 2024 메이저리그 원정경기에서
# 1번 지명타자로 선발 출전, 4타수 1안타 1도루를 기록했다.
#       """) # 있는 그대로 출력
# print("""\
# 1.오타니는 30일(이하 한국시간) 미국 콜로라도주 쿠어스필드에서 열린
# 콜로라도 로키스와의 2024 메이저리그 원정경기에서
# 1번 지명타자로 선발 출전, 4타수 1안타 1도루를 기록했다.
#       """) # 공백 제거시에 \ 가능


print("{} 평균 : {}".format("홍길동", (100+100+99)/3))
name = "홍길동"

# f함수 프린트 소수점 처리 : format을 적용 후 변수 전달
avg = "{:.2f}".format(99.666667)
print(f"{name} 평균 : {avg}")

#### f함수 소수점 자리 출력 
a = 1.1234
print(f"소수점 2자리 출력 : {a:.2f}")