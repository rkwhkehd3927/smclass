from django.shortcuts import render, redirect
from board.models import Board
from django.db.models import Max
from django.contrib import messages
from django.db.models import F

# 게시판 글 목록
def blist(request):
  qs = Board.objects.all().order_by("-bgroup",'bstep') # bgroup 은 역순, bstep 은 순차
  context = {"blist":qs}
  return render(request, 'blist.html', context)

# 글쓰기 페이지, 글 저장
def bwrite(request):
  if request.method == "GET":
    return render(request,'bwrite.html')
  else:
    id = request.POST.get("id")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    # no = Board.objects.aggregate(max_bno = Max('bno'))
    # no['max_bno']+1
    # Oracle sequence.nextval, sequence.currval

    ## DB 저장
    # bno, bdate = 자동, bstep, bindent, bhit = 0
    # id,btitle,bcontent,bgroup(차후입력) = 입력필요
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    messages.success(request,message='게시글이 저장되었습니다.')

    # return redirect('board:blist')
    return render(request, 'bwrite.html', {'w_msg':'1'})


# 게시글 상세페이지
def bview(request,bno):
  print("게시글 번호: ",bno)
  print("게시글 번호: ",int(bno))

  # 조회수 1 증가 = get() 이용하는 방법
  # qs = Board.objects.get(bno=bno)
  # qs.bhit += 1
  # qs.save() # get 으로 할때는 save() 필요


  # 조회수 1 증가 = filter() 이용하는 방법
  qs = Board.objects.filter(bno=bno)
  qs.update(bhit=F('bhit')+1) # 값을 가져와서 컬럼=항목(bhit)에 저장하기

  context = {'board':qs[0]}
  return render(request,'bview.html',context)


# 글 수정 페이지, 저장
def bmodify(request,bno):
  print("게시글 번호: ",bno)
  if request.method == "GET":
    qs = Board.objects.filter(bno=bno)
    context = {"board":qs[0]}
    return render(request, 'bmodify.html',context)
  else: # post
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    qs.save()
    # return redirect("board:blist")
    return render(request, 'bmodify.html', {'u_msg':bno})
  

# 글 삭제
def bdelete(request,bno):
  print("게시글 번호: ",bno)
  Board.objects.get(bno=bno).delete()
  return render(request, 'blist.html', {"d_msg":bno} )


# 답변 달기
def breply(request,bno):
  if request.method == 'GET':
    print("게시글 번호: ", bno)
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request,'breply.html',context)
  else:
    bgroup = int(request.POST.get('bgroup')) # str타입 -> int타입으로 변경
    bstep = int(request.POST.get('bstep'))
    bindent = int(request.POST.get('bindent'))
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    print("bgroup 번호: ", bgroup)

    ## 다른 답변 달기에 bstep을 1씩 증가시켜줌
    qs = Board.objects.filter(bgroup=bgroup, bstep__gt=bstep) # bstep = 부모보다 더 큰거 찾아야함(?) 
    qs.update(bstep = F('bstep')+1) # 자식('bstep)에 해당되는거 찾아서 +1 하고

    ## DB 저장
    # bgroup: 부모의 bgroup 입력
    Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bgroup=bgroup,\
                              bstep=bstep+1,bindent=bindent+1)

    # return redirect('board:blist')
    return render(request, 'blist.html', {"r_msg":"1"})