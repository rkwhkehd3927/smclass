from django.shortcuts import render
from member.models import Member

# 회원 전체리스트
def mlist(request):
  qs = Member.objects.all()
  context = {'mlist':qs}
  return render(request, 'mlist.html', context)


# 로그인1
def login(request):
  if request.method == "GET":
    print("쿠키정보 : ",request.COOKIES)
    print("cookinfo 쿠키정보 : ",request.COOKIES.get('cookinfo'))

    print("saveId: ",saveId)
    saveId = request.COOKIES.get('saveId','')
    context = {"saveId":saveId}
    response = render(request, 'login.html', saveId)

    # 쿠키정보 검색 request.COOKIES.get('key')
    if not request.COOKIES.get('cookinfo'): # 쿠키가 없을때만 쿠키 설정시키기

      # 쿠키 설정(저장) response.set_cookie('key','value)
      response.set_cookie('cookinfo','1111',max_age=60*60) # cookinfo 에 1111 넣기 # max_age=시간설정
        # max_age=60초*60분 -> 브라우저 닫아도 한시간은 저장 # max_age가 없으면 브라우저 종료시 삭제
        # 1달 = 60초*60분*24시간*30일 # 1년 = 365일
    # 쿠키 삭제 = response.delete_cookie('key')
    return response
    
  else:
    print("쿠키정보: ",request.COOKIES)
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    saveId = request.POST.get("saveId","") # checkbox(다중선택)는 getlist 로 받는데 얘는 하나만 있으니까 걍 get
    # radio는 단일 선택이기 때문에 get으로 받음
    print("전달받은 정보: ", id,pw,saveId)
    response = render(request, 'login.html')

    # ID 저장 체크박스에 정보가 있으면 
    if saveId is not None:
      response.set_cookie('saveId',id,max_age=60*60) # ID 저장에 체크가 있으면 쿠키 저장 
      # max_age=60*60 ID 저장기간
    else:
      response.delete_cookie('saveId') # ID 저장에 체크가 없으면 쿠키 삭제

    return response


# 로그인 기능 다시하기
def login2(request):
  if request.method == 'GET':

    cookId = request.COOKIES.get('cookId','')
    context = {"cookId":cookId}
    return render(request,'login2.html',context)
  
  else:
    response = render(request, 'index.html')
    # 3개의 정보
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId')
    if saveId is not None: # saveId 가 채워져 있을때(?)
      response.set_cookie('cookId',id,max_age=60*60)
    else: # 데이터 없으면 쿠키 삭제
      response.delete_cookie('cookId')
    
    return response
  
# 상품구매
def product(request):
  if request.method == 'GET': # 쿠키에 저장된 정보를 입력창에 텍스트로 뜨게하기
    cId = request.COOKIES.get('cId','')
    cName = request.COOKIES.get('cName','')
    cOption = request.COOKIES.get('cOption','')
    context = {'cId':cId,'cName':cName,'cOption':cOption}
    return render(request, 'product.html', context)
  else:
    response = render(request, 'index.html')
    pId = request.POST.get('pId')
    pName = request.POST.get('pName')
    pOption = request.POST.get('pOption')
    saveProduct = request.POST.get('saveProduct')
    if saveProduct is not None:
      # response.set_cookie('pCookie',pId,pName,pOption)
      response.set_cookie('cId',pId,max_age=60*60)
      response.set_cookie('cName',pName,max_age=60*60)
      response.set_cookie('cOption',pOption,max_age=60*60)
    else:
      # response.delete_cookie('cID','cName','cOption')
      response.delete_cookie('cId')
      response.delete_cookie('cName')
      response.delete_cookie('cOption')
    return response


# 회원권구매
def m2(request):
  if request.method == 'GET':
    c_mId = request.COOKIES.get('c_mId','')
    c_money = request.COOKIES.get('c_money','')
    c_option = request.COOKIES.get('c_option','')
    context = {"c_mId":c_mId,"c_money":c_money,"c_option":c_option}
    return render(request, 'm2.html', context)
  else:
    response = render(request, 'm2.html')
    mId = request.POST.get('mId')
    money = request.POST.get('money')
    option = request.POST.get('option')
    saveMember = request.POST.get('saveMember')
    if saveMember is not None:
      response.set_cookie('c_mId',mId,max_age=60*60)
      response.set_cookie('c_money',money,max_age=60*60)
      response.set_cookie('c_option',option,max_age=60*60)
    else:
      response.delete_cookie('c_mId')
      response.delete_cookie('c_money')
      response.delete_cookie('c_option')
    return response







#### 쌤이 하신 상품구매
# def product(request):
#   if request.method == 'GET':
#     # 쿠키 읽어오기
#     c_pId = request.COOKIES.get('c_pId','')
#     c_pName = request.COOKIES.get('c_pName','')
#     context = {'c_pId':c_pId,'c_pName':c_pName}
#     return render(request, 'product.html',context)
#   else:
#     # 쿠키 저장하기
#     pId = request.POST.get('pId')
#     pName = request.POST.get('pName')
#     pOption = request.POST.get('pOption')
#     saveProduct = request.POST.get('saveProduct')
#     response = render(request,'index.html')
#     if saveProduct is not None: # 체크가 되어있으면
#       # 쿠키 저장
#       response.set_cookie('c_pId',pId)
#       response.set_cookie('c_pName',pName)
#     else:
#       response.delete_cookie('c_pId')
#       response.delete_cookie('c_pName')
#     return response