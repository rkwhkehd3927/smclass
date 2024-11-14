# dictionary 로  학생을 입력
students = []
subject = ["번호","이름","국어","영어","수학","합계","평균","등수"]
sub = ["no","name","ko","영어","수학","합계","평균","등수"]

f = open("b1017/students.txt","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line: break
  # print(line.strip())
  s = line.strip().split(",")
  # ['20', 'alibreyj', '63', '94', '67', '224', '74.6666666667', '1.0']
  # s[0] = int(s[0])
  # s[2] = int(s[0])
  # s[3] = int(s[3])
  # s[4] = int(s[4])
  # s[5] = int(s[5])
  # s[6] = int(s[6])
  # s[7] = int(s[7])
  for idx, i in enumerate(s):
    if idx == 1: continue
    elif idx == 6:  s[6] = float[i]
    else: s[idx] = int(i)
  students.append(dict(zip(sub,s)))
f.close()
print("프로그램을 종료합니다.")
