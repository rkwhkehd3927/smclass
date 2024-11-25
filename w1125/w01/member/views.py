from django.shortcuts import render, redirect
from member.models import Member


# 로그인 페이지열지, 로그인
def login(request):
  if request.method == "GET":
    return render(request, 'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw)

    if qs: # member 있을 경우
      request.session['session_id'] = qs[0].id
      request.session['session_nickname'] = qs[0].nickname
      context = {"lmsg":"1"}
    else: # member 없을 경우
      context = {"lmag":"0"}
    return render(request,'login.html',context)
  
def logout(request):
  request.session.clear()
  return redirect("/")
      