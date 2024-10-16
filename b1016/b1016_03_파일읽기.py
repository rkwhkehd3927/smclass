# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0}
#   [1,"홍길동",100,90,80,270,90.0,0],
#   [2,"강감찬",80,100,100,280,93.33333333333333,0],
#   [3,"이순신",100,90,80,270,90.0,0]
# ]
stu_key = ["no","name","kor","eng","math","total","avg","rank"]
students = []

# 파일 읽기 - r
f = open('a.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break # 데이터가 하나도 없을때 break
  # students.append(line) # 하나의 묶음으로 들어가버림 # ['1,홍길동,100,90,80,270,90.0,0\n', '2,강감찬,80,100,100,280,93.33333333333333,0\n']
  s = line.strip().split(",")
  # print("1개 : ",s)

  # for i,v in enumerate(s):
  #   if i == 1: continue # 이름
  #   elif i == 6: s[6]['avg'] = float(s[6]) # 평균
  #   else: v = int(v) # 나머지는 int

  s[0] = int(s[0])
  s[2] = int(s[2])
  s[3] = int(s[3])
  s[4] = int(s[4])
  s[5] = int(s[5])
  s[6] = float(s[6])
  s[7] = int(s[7])

  # students.append(s) # [[1, '홍길동', 100, 90, 80, 270, 90.0, 0], [2, '강감찬', 80, 100, 100, 280, 93.33333333333333, 0]]
  students.append(dict(zip(stu_key,s)))
  print(line.strip())
f.close()

print(students)