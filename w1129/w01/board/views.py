from django.shortcuts import render
from board.models import Board
from comment.models import Comment


# 게시판 글 목록
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request, 'blist.html', context)

# 글 상세보기
def bview(request,bno):
  qs = Board.objects.filter(bno=bno)
  # 하단 댓글 가져오기
  c_qs = Comment.objects.filter(board=qs[0]).order_by("-cno")
  print("확인: ", c_qs, c_qs.count)
  context = {"board":qs[0],"clist":c_qs}
  return render(request, 'bview.html', context)

