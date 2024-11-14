# a = ["홍길동","유관순","이순신"]
# b = [100,90,80]
# c = zip(a,b)
# # print(list(c)) # [('홍길동', 100), ('유관순', 90), ('이순신', 80)]
# print(dict(c)) # {'홍길동': 100, '유관순': 90, '이순신': 80}


# a = ["no","name","kor","eng"]
# b = [1,"홍길동",100,100]
# print(dict(zip(a,b))) # {'no': 1, 'name': '홍길동', 'kor': 100, 'eng': 100}

# --------------------------

students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
# students 딕셔너리파일을 메모장에 csv파일형태로 저장하시오.

f = open('students.txt','w',encoding='utf-8')

# students.txt
# 1,홍길동,100,90,80,270,90.0,0
# 2,강감찬,80,100,100,280,93.33333333333333,0

for s in students:
  f.write(f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n")

f.close()


# -------------------

# member = [
#   {"id":"aaa","pw":"1111","name":"홍길동","nickName":"길동스","address":"서울시","money":1000000000},
#   {"id":"bbb","pw":"2222","name":"유관순","nickName":"관순스","address":"부산시","money":700000000},
#   {"id":"ccc","pw":"3333","name":"이순신","nickName":"순신스","address":"경기도","money":100000000},
#   {"id":"ddd","pw":"4444","name":"강감찬","nickName":"감찬스","address":"인천시","money":500000000},
#   {"id":"eee","pw":"5555","name":"김구","nickName":"구스","address":"대구시","money":2000000000}
# ]

# # member.txt 파일을 생성해서 csv형태의 문자열로 저장하시오.

# f = open('member.txt','w',encoding='utf-8')
# for s in member:
#   f.write(f"{s['id']},{s['pw']},{s['name']},{s['nickName']},{s['address']},{s['money']}\n")
# f.close()

