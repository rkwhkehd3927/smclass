from django.shortcuts import render
from board.models import Board
from member.models import Member
from datetime import datetime
from django.db.models import Q
from django.db.models import F
from django.core.paginator import Paginator

# 글 목록
def blist(request):
  npage = int(request.GET.get('npage',1)) # 넘어온 현재 페이지 정보(?)
  qs = Board.objects.all().order_by("-bgroup","bstep")
   # 하단 페이지 처리(넘버링)
  paginator = Paginator(qs,10) # 10개씩 분할하기
  blist = paginator.get_page(npage) # 1페이지에 있는거 다 갖다줘! = 10개씩 1페이지에 분할해놨으니까 10개 넘어옴
  context = {"blist":blist, 'npage':npage}
  return render(request, 'blist.html',context)


  
# 글 쓰기
def bwrite(request):
  if request.method == "GET":
    return render(request, 'bwrite.html')
  else:
    id = request.session.get('session_id')
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","") # 파일 첨부
    print("파일 정보: ",bfile)

    # 글쓰기 저장
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()



    context = {"wmsg":"1"}
    return render(request, 'bwrite.html', context)


# 글 상세보기
def bview(request,bno):
  # print(bno)
  npage = request.GET.get("npage",1)
  qs = Board.objects.get(bno=bno)

  # 이전글, 다음글
  # bgroup_lt=qs[0].bgroup,bstep_lte=qs[0].bstep <- 이게 한묶음
  prev_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep) | Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by("-bgroup","bstep").first()
  next_qs = ""


  
  # 조회수 마구잡이 증가 방지, 날짜 설정 - 쿠키 기간 사용
  day1 = datetime.replace(datetime.now(),hour=23,minute=59,second=59)
  expires = datetime.strftime(day1,"%a, %d-%b-%Y %H:%M:%S GMT")
  print("날짜: ",expires)
  context = {"board":qs,"prev_board":prev_qs,"next_board":next_qs,"npage":npage}
  response = render(request,'bview.html',context)


  # 쿠키 확인
  if request.COOKIES.get("cookie_boardNo") is not None:
    cookies = request.COOKIES.get("cookie_boardNo") # 1|5|6|2
    cookies_list = cookies.split("|")
    if str(bno) not in cookies_list:
      # 쿠키저장
      response.set_cookie("cookie_boardNo",cookies + f"|{bno}",expires=expires)
      # 조회수 1 증가 
      qs.bhit += 1
      qs.save()
  else:
    # 쿠키저장
    response.set_cookie("cookie_boardNo",bno,expires=expires)
    # 조회수 1 증가 
    qs.bhit += 1
    qs.save()
    
  return response


# 글 삭제
def bdelete(request,bno):
  Board.objects.get(bno=bno).delete()
  context = {"dmsg":bno}
  return render(request, 'blist.html', context)


# 글 수정 페이지, 저장
def bupdate(request,bno):
  if request.method == "GET":
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request, 'bupdate.html', context)
  else:
    bno = request.POST.get("bno")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","") # 파일 첨부

    # 수정한 글 저장
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    if bfile:
      qs.bfile = bfile
    qs.save()

    context = {"umsg":bno}
    return render(request, 'bupdate.html', context)
  



# 답글 쓰기, 저장
def breply(request,bno):
  if request.method == "GET":
    print("test : ",bno)
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request, 'breply.html', context)
  else:
    bno = request.POST.get("bno")
    id = request.session.get("session_id")
    member = Member.objects.get(id=id)
    bgroup = int(request.POST.get("bgroup"))
    bstep = int(request.POST.get("bstep"))
    bindent = int(request.POST.get("bindent"))
    qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
    qs.update(bstep = F('bstep')+1)


    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","") # 파일 첨부
    Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,\
                              bfile=bfile, bgroup=bgroup,bstep=bstep+1,bindent=bindent+1)

    context = {"rmsg":bno}
    return render(request, 'breply.html', context)