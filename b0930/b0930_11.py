
#### 덜했음 ####

# money = 780
# # 500 - 1
# print("500원 동전 개수 :", money//500)
# # 100 - 2
# print("100원 동전 개수 :", (money%500)//100)
# # 50 - 1
# print("50원 동전 개수 :", (money%500)%100//50)
# # 10 - 3
# print("50원 동전 개수 :", ((money%500)%100)%50//10)


# money = 175987
# # 50000,10000,5000,1000,500,100,50,10
# print("50000원 지폐 개수 :", money//50000)
# print("10000원 지폐 개수 :", (money%50000)//10000)
# print("5000원 동전 개수 :", (money%50000)%10000//5000)
# print("1000원 동전 개수 :", ((money%50000)%10000)%5000//1000)
# print("500원 동전 개수 :", (((money%50000)%10000)%5000)%1000//500)
# print("100원 동전 개수 :", ((((money%50000)%10000)%5000)%1000)%500//100)
# print("50원 동전 개수 :", (((((money%50000)%10000)%5000)%1000)%500)%100//50)

str1 = input("문자를 입력하세요.")
a = len(str1)  # 문자의 길이 .length

if a==5:
  print("a는 5입니다.")
elif a==4:    # elif : else if
  print("a는 4입니다.")
elif a==3:
  print("a는 3입니다.")
else:
  print("a 숫자는 2이하입니다.")


# 175987
# 9870
# 590

int1 = input("금액을 입력하세요.")
b = len(int1)
b_50000 = int1//50000
b_10000 = (int1%50000)//10000
b_5000 = (int1%50000)%10000//5000
b_1000 = ((int1%50000)%10000)%5000//1000
b_500 = (((int1%50000)%10000)%5000)%1000//500
b_100 = ((((int1%50000)%10000)%5000)%1000)%500//100
b_50 = (((((int1%50000)%10000)%5000)%1000)%500)%100//50
b_50 = ((((((int1%50000)%10000)%5000)%1000)%500)%100)%50//10

# print((((((int1%50000)%10000)%5000)%1000)%500)%100//50)
  # print(((((int1%50000)%10000)%5000)%1000)%500//100)
  # print(((int1%50000)%10000)%5000)%1000//500
  # print((int1%50000)%10000)%5000//1000
  # print(int1%50000)%10000//5000
  # print(int%50000)//10000
  # print(int//50000)

if b==6:
  print("50000원",b_50000,"10000원",b_10000,"5000원",b_5000)