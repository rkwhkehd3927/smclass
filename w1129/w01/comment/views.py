from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers # json 타입
from comment.models import Comment
from member.models import Member
from board.models import Board

# 하단댓글 저장
def cwrite(request):
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno",1)
  board = Board.objects.get(bno=bno)
  cPw = request.POST.get("cPw","")
  cContent = request.POST.get("cContent","")

  print("확인 : ",cPw,cContent)
  qs = Comment.objects.create(member=member,board=board,cPw=cPw,cContent=cContent)
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())

  print("qs확인 : ",list_qs)
  context = {"result":"success","comment":list_qs}
  return JsonResponse(context)


# 하단 댓글 삭제
def cdelete(request):
  cno = request.POST.get("cno")
  print("확인 : ",cno)
  Comment.objects.get(cno=cno).delete()
  context = {"result":"success"}
  return JsonResponse(context)


# 하단 댓글 수정 저장
def cupdate(request):
  id = request.session['session_id']
  cno = request.POST.get("cno")
  cContent = request.POST.get('cContent')
  print("확인 : ",cno,cContent)
  # 수정
  qs = Comment.objects.get(cno=cno)
  qs.cContent = cContent
  qs.save()
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print("qs확인 : ",list_qs)
  context = {"result":"success","comment":list_qs}
  return JsonResponse(context)

