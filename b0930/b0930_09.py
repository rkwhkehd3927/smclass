stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [
  [1, '홍길동', 100, 100, 100, 99],
  [2, '유관순', 99, 99, 100, 99],
  [3, '이순신', 100, 99, 98, 99],
  [4, '김구', 80, 100, 90, 99],
  [5, '김유신', 80, 100, 90, 99],
  ]

# append - 합계,평균 추가해서 출력하시오.

print("                       [학생 성적 프로그램]")

for s_t in stu_title:
  print("{}".format(s_t),end='\t')
print()
print("-"*70)


stu_datas[1].append(stu_datas[1][2]+stu_datas[1][3]+stu_datas[1][4]+stu_datas[1][5])
for s in stu_datas:
  s.append(s[2]+s[3]+s[4]+s[5])
  s.append((s[2]+s[3]+s[4]+s[5])/4)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:/2f}".format(
  s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]))


#### T가 함

# print("                  [ 학생성적 프로그램 ]")
# for s_t in stu_title:
#   print("{}".format(s_t),end='\t')
# print()
# print("-"*70)
# for s in stu_datas:
#   s.append(s[2]+s[3]+s[4]+s[5])
#   s.append((s[2]+s[3]+s[4]+s[5])/4)
#   print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(
#   s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]))
#   ## 학번,이름, 국어, 영어, 수학, 과학, 합계, 평균