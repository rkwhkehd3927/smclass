# fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
#        0 1 234 5 67 8910

# 딸기
# print(fruit.find("딸기")) # 5번 (0번 부터 찾음)
# # print(fruit.find("딸기",0)) # 5번 (0번 부터 찾음)
# print(fruit.find("딸기",6)) # 22번 (6번 부터 찾음)
# print(fruit.find("딸기",fruit.find("딸기")+1)) # 22번 (6번 부터 찾음) / fruit.find("딸기")+1 = 5

# 배  / fruit.find('배',0) -> 요게 index 번호가 되는거임
# print(fruit.find('배',0)) # 3
# print(fruit.find('배',3+1)) # 15
# print(fruit.find('배',fruit.find('배',0)+1)) # 15
# print(fruit.find('배',15+1)) # 20
# print(fruit.find('배',fruit.find('배',fruit.find('배',0)+1)+1)) # 20

fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
fruits = fruit.split(",")
# print(fruits)
# print(len(fruits))

# 리스트 인 경우 검색해서 해당되는 index를 출력
# '배' 에 해당되는 index 번호를 출력

search = input("과일을 입력하세요.")
count = 0


for idx,fru in enumerate(fruits):
  if fru == search:
    print(idx)
    # count = 1
    # break
  # else:
  #   print("과일이 없습니다.")
  # if count == 0:  # 뭐야 모르겠음
  #   print("과일이 없습니다.")