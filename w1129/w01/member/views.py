from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers # json 타입
from member.models import Member


# 로그인 페이지
def login(request):
  return render(request, 'login.html')

# 아이디 확인
def loginChk(request):
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  # db 확인
  qs = Member.objects.filter(id=id,pw=pw)
  print("확인: ", id, pw)
  if qs:
    # 세션 추가
    request.session['session_id'] = qs[0].id
    request.session['session_nickname'] = qs[0].nickname
    list_qs = list(qs.values())
    context = {"result":"success","member":list_qs}
  else:
    context = {"result":"fail"}
  return JsonResponse(context)


# 로그아웃
def logout(request):
  request.session.clear()
  return redirect("/")