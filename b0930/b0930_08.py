#### list 추가방법 : append -  제일 뒤에 추가, insert - 원하는 위치에 추가
# a_list = [1,2,3]
# print(a_list)
# a_list.append(4)
# print(a_list)
# a_list.append(10) # append - list에 추가하기
# print(a_list)
# a_list.insert(0,50)
# print(a_list) 
# a_list.insert(3,20) # 3번째에 20 추가


#### 삭제 del - index 위치에 데이터 삭제, remove - 데이터값으로 삭제
# del a_list[0]
# print(a_list)
# del a_list[2]
# print(a_list)

# a_list.remove(4)
# print(a_list)
# a_list.remove(1)
# print(a_list)


stu = [1, '홍길동', 100, 100, 100, 99]
# 합계, 평균 추가

print(stu)
stu.insert(6,stu[2]+stu[3]+stu[4]+stu[5])
stu.insert(7,(stu[2]+stu[3]+stu[4]+stu[5])/4)
print(stu)