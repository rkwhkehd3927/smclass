from django.shortcuts import render, redirect
from member.models import Member

# 로그인
def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw)
    if qs: # 로그인 성공
      msg = "로그인 되었습니다."
      print(msg)
      request.session['session_id'] = id
      request.session['session_nickname'] = qs[0].nickname
      
      return redirect('index') # 로그인되면 메인페이지로 넘어감 
    
    else: # 로그인 실패
      msg = "아이디 또는 패스워드가 일치하지 않습니다."
      print(msg)
      return render(request,'login.html',{"login_msg":msg})

# 로그아웃
def logout(request):
  request.session.clear() # 전체세션삭제
  return redirect("/")


# 회원가입 - join01
def join01(request):
  return render(request, 'join01.html')