from django.shortcuts import render, redirect
from member.models import Member


# 로그인페이지 열기, 로그인 버튼 클릭시
def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
      msg = "로그인 되었습니다"
      print(msg)
      ## 세션 연결
      request.session['session_id'] = id
      request.session['session_nickname'] = qs[0].nickname

      return redirect('index')
    else:
      msg = "아이디 또는 패스워드가 일치하지 않습니다."
      print(msg)
      return render(request,'login.html',{"login_msg":msg})
    

# 로그아웃
def logout(request):
  request.session.clear() # 전체 세션 삭제
  ## del request.session['session_id'] 해당 세션 삭제
  return redirect("/")


# 회원리스트
def mlist(request):
  id = request.session['session_id']
  if id == 'admin':
    qs = Member.objects.all()
  else:
    qs = Member.objects.filter(id=id)
  context = {'mlist':qs}
  return render(request, 'mlist.html', context)

# 회원상세
def mview(request,id):
  print("아이디: ",id)
  qs = Member.objects.filter(id=id)
  context = {"mem":qs[0]}
  return render(request, 'mview.html',context)

# 회원정보수정
def mupdate(request,id):
  if request.method == "GET":
    print("회원정보 : ", id)
    qs = Member.objects.filter(id=id)
    context = {'mem':qs[0]}
    return render(request,'mupdate.html',context)
  else:
    print("id: ",id)
    id = request.session['session_id'] # 아이디가 admin이 아니면 session 정보 가져와서 저장
    # 관리자 로그인이면 id 정보를 가져와서 저장 # 근데 원래는 관리자 페이지는 따로 만들어서 따로 관리함
    if request.session['session_id'] == 'admin':
      id = request.POST.get('id')

    pw = request.POST.get('pw')
    name = request.POST.get('name')
    nickname = request.POST.get('nickname')
    tel = request.POST.get('tel')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)
    qs = Member.objects.get(id=id) # 아이디는 안바꿀거기 때문에 그대로 있는 데이터에서 찾기
    qs.pw = pw
    qs.name = name
    qs.nickname = nickname
    qs.tel = tel
    qs.gender = gender
    qs.hobby = hobby
    qs.save()

    return redirect('member:mlist')



# 회원정보입력
def mwrite(request):
  if request.method == "GET":
    return render(request,'mwrite.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    name = request.POST.get("name")
    nickname = request.POST.get("nickname")
    tel = request.POST.get("tel")
    gender = request.POST.get("gender")
    hobbys = request.POST.getlist("hobby")
    hobby = ','.join(hobbys) # 쉼표로 분리?

    # Member.objects.create(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby)
    qs = Member(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby)
    qs.save()
    return redirect('member:mlist')
  


# 회원정보삭제
def mdelete(request,id):
  print("회원정보: ",id)
  Member.objects.get(id=id).delete()
  # return render(request,'mlist.html') # render로 전송하면 주소가 reload 가 안됨
  return redirect('member:mlist')