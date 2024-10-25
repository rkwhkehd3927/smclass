# a = [1,2,3]
# b = [4,5,6,7]
# print(a+b)

# a = "1.7만"
# if '만' in a:
#   print("있어요")
# else:
#   print("없어요")

# ----------------------------

a = ['1만','3,450','1.7만','500','1,000']
b = []
# 데이터를 float 타입으로 변경하여 리스트로 저장하시오.

# 내가 한거
for i in a:
  if '만' in i:
    aa = i.replace("만","")
    aa = float(aa)*10000
    b.append(aa)
  else:
    aa = float(i.replace(",",""))
    b.append(aa)

# 쌤이 한거
def chg(val):
  if '만' in val:
      r_val = float(val[:-1])*10000
  else: r_val = float(val.replace(",",""))
  return(r_val)

a_list = list(map(chg,a)) # 몰라 map 잘 모르겠음
print(a_list)
print(max(a_list)) # 최대값
print(min(a_list)) # 최소값
a_list.sort() # 정렬
print(a_list)
