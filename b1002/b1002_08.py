#### 배열
# fruit = ['사과','배','딸기','포도','복숭아','배','사과','배','딸기'] 
# if '배' in fruit: # 1번의 비교로 있는지 확인, 2개 있든 3개 있든 유무만 체크
#   print("배가 있어요.")
# else:
#   print("배가 없어요.")

#### 문자열
# fruit = "사과, 배, 딸기, 포도, 복숭아, 배, 사과, 배, 딸기"
# if '배' in fruit:
#   print("'배' 라는 글자가 있어요.")
# else:
#   print("'배' 라는 글자가 없어요.")


# 글을 입력받아 입력한 과일이 있으면 "있어요", else "없어요" 출력

# f = input("과일을 입력하세요.")
# if f in fruit:
#   print(f"{f}는 있어요")
# else:
#   print(f"{f}는없어요")


# 리스트
# in - 데이터가 있는지 없는지 확인
# count - 데이터 개수 확인 가능
# find - 데이터가 있는 위치를 알려줌, 없으면 -1
# index - 데이터가 있는 위치를 알려줌, 없으면 에러(Not found)

# '배' 의 개수 찾기 / count 리스트에서 개수 확인 (배열, 문자열 둘다 가능)
# print(fruit.count('배'))
# print(fruit.count('사과'))


# 과일 이름을 입력받아, 있으면 "과일 이름이 있습니다" and 과일검색개수 출력, 없으면 "없습니다" 출력

# search = input("과일을 입력하세요.")
# if search in fruit:
#   print(f"{search}가 있습니다. \t 과일 검색 개수 : ",fruit.count(search))
#   print(fruit.find(search))
#   # print(fruit.index(search)) # 배가 있는 위치의 index
# else:
#   print(f"{search}가 없습니다.")
#   print(fruit.find(search))
#   # print(fruit.index(search)) # 없으면 에러(Not found)가 남


# range() : 말 그대로 “범위”를 만들 때 사용하는 함수, 좀 더 정확히 얘기하면 정수로 이뤄진 범위를 만들어줌



# '배'가 있는 위치를 모두 출력하시오. for문 사용

fruit = "사과, 배, 딸기, 포도, 복숭아, 배, 사과, 배, 딸기"
search = input("과일을 입력하세요.")

# idx = 0
# if fruit.count('배')>0:
#   for i in range(fruit.count('배')): # 3번('배'의 개수) 실행
#     for i in range(idx,len(fruit)):
#       print(fruit.find('배')) # = 3
#       idx = fruit.find('배')+1 # 3+1 = 4
#       break # 찾았으면 멈추고(4인 상태), 이 for문 빠져나가기, 바깥 for문 실행
# else:
#   print("'배' 라는 글자는 없습니다.")


idx = 0
if fruit.count(search)>0:
  print(f"{search} 글자가 있습니다.")
  for i in range(fruit.count(search)): # 3번('배'의 개수) 실행
    # for i in range(idx,len(fruit)):
    print(f"{search}가 있는 위치 : ", fruit.find(search,idx)) # find(찾을 문자, 시작 index , 끝 index)
    idx = fruit.find(search,idx)+1 # 3+1 = 4
    # break # 찾았으면 멈추고(4인 상태), 이 for문 빠져나가기, 바깥 for문 실행
else:
  print(f"{search}(이)라는 글자는 없습니다.")







  