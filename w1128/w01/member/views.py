from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from member.models import Member
from django.core import serializers # json 타입

## 로그인
def login(request):
  return render(request,'login.html')

# json 타입으로 실행가능하려면 list,dict 타입으로 바꿔줘야함 
# 로그인 체크 
# @csrf_exempt # 예외처리
def loginChk(request):
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  qs = Member.objects.filter(id=id,pw=pw) # 데이터 없으면 None
  # qs = Member.objects.get(id=id,pw=pw) # set 타입 # 데이터 없으면 에러
  if qs:
    request.session['session_id'] = id
    request.session['session_nicName'] = qs[0].nicName
    qs_list=list(qs.values())
    # json_qs = serializers.serialize('json',[qs]) # json 타입으로 변경
    context={"result":"success","member":qs_list} # list or dict 타입으로 변경 후 전송
    # context={"result":"success","member":json_qs} # list or dict 타입으로 변경 후 전송
  else:
    context = {"result":"fail"}  
  
  return JsonResponse(context)


## 로그아웃
def logout(request):
  request.session.clear() # 모두 삭제
  # del request.session['session_id'] # 1개 삭제
  context = {"outmsg":"1"}
  return render(request,'index.html', context)


# 회원가입 step03
def step03(request):
  return render(request, 'step03.html')


# 아이디 중복 체크
def idChk(request):
  id = request.POST.get("id","")
  qs = Member.objects.filter(id=id)
  qs_list = list(qs.values())
  if not qs:
    context = {"result":"success"}
  else:
    context = {"result":"fail","member":qs_list}
  return JsonResponse(context)