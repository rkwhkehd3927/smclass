from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json 타입
from member.models import Member
from board.models import Board
from comment.models import Comment


# 하단 댓글 리스트
def clist(request):
  return render(request, 'clist.html')


# 하단 댓글 작성, 저장
def cwrite(request):
  # 데이터 가져오기(일치하는 정보 찾아서)
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno",1)
  board = Board.objects.get(bno=bno)
  cPw = request.POST.get("pw","")
  cContent = request.POST.get("cContent","")
  print(cPw,cContent) ## 성공

  # 데이터 저장
  qs = Comment.objects.create(board=board,member=member,cPw=cPw,cContent=cContent)
  json_qs = serializers.serialize("json",[qs]) # json 타입으로 변경
  context = {"comment":json_qs,"result":"success"}
  return JsonResponse(context)