from django.shortcuts import render, redirect
from board.models import Board
from member.models import Member
from django.db.models import F
from datetime import datetime


# 게시판 리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  print("blist : ",qs)
  context = {"blist":qs}
  return render(request, 'blist.html', context)

# 글쓰기
def bwrite(request):
  if request.method == "GET":
    return render(request, 'bwrite.html')
  else:
    # id = request.POST.get("id")
    # bgroup,bstep,bindent,bhit,bdate 자동 입력
    id = request.session.get('session_id') # session_id에 저장된 id값을 가져옴
    member = Member.objects.get(id=id) # 아이디를 통째로 저장(?)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile",'')
    print("파일이름: ",request.FILES)
    print("파일이름: ",bfile)

    # DB저장 - AutoField: 번호생성
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()
    context = {"wmsg":"1"}

    return render(request,'bwrite.html',context)
  

# 글 상세보기 - 조회수 증가방지, 이전글, 다음글
def bview(request,bno):
  # get() 형태
  # qs = Board.objects.get(bno=bno)
  # qs.bhit += 1
  # qs.save()
  # context = {"board":qs}

  # 쿠키사용기간 - 1일동안 유지
  # 11월 25일 23시 59분 0초
  tomorrow = datetime.replace(datetime.now(),hour=23,minute=59,second=0)

  # 쿠키설정포맷 - strftime: 시간 포맷형태
  expires = datetime.strftime(tomorrow,"%a,%d=%b-%Y %H:%M:%S GMT") # 쿠키에 있는 시간형태로 바꾸는 것

  # filter() 형태 - update() 명령어가 존재함
  # F함수 = 필드 값을 참조
  qs = Board.objects.filter(bno=bno)
  # 이전글
  prev_qs = Board.objects.filter().order_by("-bgroup","bstep").first() 
  # 다음글
  next_qs = Board.objects.filter().order_by("bgroup","-bstep").first() 
  context = {"board":qs[0]}
  # 조회수가 증가하면, cookie_name 에 증가시킨 게시글번호를 추가
  # cookie_name 가 존재하면
  response = render(request, 'bview.html', context)
  print("cookie_name: ",request.COOKIES.get('cookie_name'))
  if request.COOKIES.get('cookie_name') is not None:
    ## 쿠키를 읽어와서 e.g. 안에 1|3|4 일때 -> 2번이면 1 증가, 3번이면(안에 이미 들어있는 숫자) 증가X 
    cookies = request.COOKIES.get('cookie_name')
    cookies_list = cookies.split("|")

    if str(bno) not in cookies_list:
      print("cookie_name 가 있지만, 번호가 없으면")
      # 1|3|4 -> 2('{bno}') = 1|3|4|2
      # 번호가 없으면 번호 추가 + 조회수도 추가
      response.set_cookie("cookie_name",cookies+f'|{bno}', expires=expires)
      qs.update(bhit = F('bhit')+1) # qs의 'bhit' 값 가져와서 +1

  else: # cookie_name 가 존재하지 않으면 - 처음으로 게시글 조회
    print("cookie_name 이 없으면")
    response.set_cookie('cookie_name',bno,expires=expires)
    qs.update(bhit = F('bhit')+1) # qs의 'bhit' 값 가져와서 +1

  return response


# 글 삭제
def bdelete(request,bno):
  qs = Board.objects.get(bno=bno)
  qs.delete()
  context = {"dmsg":bno}
  return render(request,"blist.html",context)


# 글 수정페이지, 글 수정 저장
def bupdate(request,bno):
  if request.method == "GET":
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request,'bupdate.html',context)
  else:
    bno = request.POST.get("bno")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    qs = Board.objects.get(bno=bno)
    qs.btitle=btitle
    qs.bcontent = bcontent
    qs.save()
    return redirect("board:bview",bno)
  

# 답변 달기
def breply(request,bno):
  if request.method == "GET":
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request,'breply.html',context)
  else:
    id = request.POST.get("id")
    print("id : ",id)
    member = Member.objects.get(id=id)
    bgroup = int(request.POST.get("bgroup")) # 답글들 그룹핑
    bstep = int(request.POST.get("bstep")) # 답글의 순서
    bindent = int(request.POST.get("bindent")) # 들여쓰기
    btitle = request.POST.get("btitle") # 제목
    bcontent = request.POST.get("bcontent") # 답글 내용
    

    # 같은 bgroup에 속한 데이터 1씩 증가
    qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
    qs.update(bstep = F('bstep')+1)

    qs = Board(member=member,btitle=btitle,bcontent=bcontent,
               bgroup=bgroup,bstep=bstep+1,bindent=bindent+1)
    qs.save()
    context = {"rmsg":"1"}
    return render(request, 'breply.html',context)