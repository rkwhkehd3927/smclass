# fruit = []
# a=0 # 초기값

# while a<10: #### 조건식, false가 되기 전까지 실행
#   a += 1 #### 증감식
#   print(a)

# while True: # 무한반복
#   print(a)
#   a += 1 # 조건이 없어서 계속 True이기 때문에 무한대로 실행됨

# 반복문 종료
# while True:
#   break # 반복문 종료 break, continue 는 반복문에서만 사용
# print("프로그램 종료")


#### 이해안되면 걍 외워...ㅠㅠ

fruit = []
while True:
  # strip() : 앞쪽여백, 뒤쪽여백 제거 trim ' 사과' → '사과' / '사과 ' → '사과
  # '사 과' → '사 과' 문자 가운데의 공백은 제거해주지 않음

  # replace(" ","") : 문자 대체 함수, 얘는 문자 가운데 공백을 제거(대체)해줌
  search = input("과일 이름을 입력하세요.(종료:x)").replace(" ","")
  # search = input("과일 이름을 입력하세요.(종료:x)").strip()
  if(search == 'x'):
    break
# 입력된 과일 이름을 리스트에 추가하시오.
  if search in fruit:
    print("같은 이름이 있습니다.")
    print("모든 과일이름 :",fruit)
  else:
    print(f"{search}을(를) 추가합니다.")
    fruit.append(search)
    print("모든 과일이름 :",fruit)
