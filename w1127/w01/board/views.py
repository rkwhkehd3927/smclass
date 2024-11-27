from django.shortcuts import render
from member.models import Member
from board.models import Board
from datetime import datetime
from django.db.models import Q
from django.db.models import F

# 글 목록
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request, 'blist.html',context)

# 글 작성
def bwrite(request):
  if request.method == "GET":
    return render(request, 'bwrite.html')
  else:
    id = request.session['session_id']
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","")
    print("파일정보: ",bfile)
    
    # 글 저장
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()

    context = {"wmsg":"1"}
    return render(request, 'bwrite.html', context)
  

# 글 보기
def bview(request,bno):
  qs = Board.objects.get(bno=bno)

  # 조회수 마구잡이 증가 방지, 날짜 설정 - 쿠키 기간 사용
  day1 = datetime.replace(datetime.now(),hour=23,minute=59,second=59)
  expires = datetime.strftime(day1,"%a, %d-%b-%Y %H:%M:%S GMT") # 당일 23시 59분 59초에 만료?
  print("날짜: ",expires)
  context={"board":qs}
  response = render(request, 'bview.html', context)

  # 쿠키 확인
  if request.COOKIES.get("cookie_boardNo") is not None:
    cookies = request.COOKIES.get("cookies_boardNo") # e.g. 1|5|6|2
    cookies_list = cookies.split("|")
    if str(bno) not in cookies_list:
      # 쿠키 저장
      response.set_cookie("cookies_boardNo",cookies + f"|{bno}",expires=expires)
      qs.bhit += 1
      qs.save()
  else:
    # 쿠키 저장
    response.set_cookie("cookie_boardNo",bno,expires=expires)
    # 조회수 1 증가
    qs.bhit += 1
    qs.save()
  
    

