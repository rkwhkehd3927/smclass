# 입력한 숫자가 짝수인지 홀수인지 출력하시오

num = int(input("숫자를 입력하세요."))

# if num%2==0:
#   print("짝수입니다.")
# else:
#   print("홀수입니다.")

# if - else
# if elif else


# 파이썬의 장점: 입력한 숫자가 1이상 10이하일때만 정답입니다. else 오답입니다. 를 출력

# if num>=1 and num<=10:
#   print("정답입니다.")

# if 1 <= num <= 10:  # 파이썬만 가능함
#   print("정답입니다.")
# else:
#   print("오답입니다.")


# 입력한 숫자가 10보다 작거나, 100보다 클 때 정답입니다. else 오답입니다. 를 출력

# if 10>=num or num>=100:
#   print("정답입니다.")
# else:
#   print("오답입니다.")


# 3,4,5 - 봄 / 6,7,8 - 여름 / 9,10,11 - 가을 / 12,1,2 - 겨울 / 그 외는 잘못된 숫자가 입력되었습니다. 출력

# if 3<=num<=5:
#   print("봄입니다.")
# elif 6<=num<=8:
#   print("여름입니다.")
# elif 9<=num<=11:
#   print("가을입니다.")
# elif 1<=num<=2 or num==12:
#   print("겨울입니다.")
# else:
#   print("잘못된 숫자입니다.")



# 100~98 A+ / 97~94 A / 93~90 A-
# 89,88 B+ / 87~84 B / 83~80 B
# 70점대 C / 60점대 D / 60점 미만 F

score = ""

if 90<=num: # 이런식으로 하면 비교문이 아래보다 좀더 줄어듬 # 중첩 if문
  score = "A"
  if 98<=num:
    score += "+"
  elif 90<=num<=93:
    score += "-"
elif 80<=num:
  score = "B"
  if 88<=num:
    score += "+"


# if 98<=num<=100:
#   print("A+입니다.")
# elif 94<=num:
#   print("A입니다.")
# elif 90<=num:
#   print("A-입니다.")
# elif 88<=num:
#   print("B+입니다.")
# elif 84<=num:
#   print("B입니다.")
# elif 80<=num:
#   print("B-입니다.")
# elif 70<=num:
#   print("C입니다.")
# elif 60<=num:
#   print("D입니다.")
# elif num<60:
#   print("F입니다.")
# else:
#   print("재수강입니다.")
