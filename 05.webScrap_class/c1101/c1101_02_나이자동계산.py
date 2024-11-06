import datetime

# 나이 자동계산
# 현재 연도
print(datetime.datetime.now().year)
# print(datetime.datetime.now())
thisYear = datetime.datetime.now().year
# in_year = input("생일 입력: 20020312")
in_year = "20020312"
print(in_year)
print(f"현재 나이: {thisYear-int(in_year[:4])}")

print(datetime.datetime.now().strftime('%y/%m/%d'))