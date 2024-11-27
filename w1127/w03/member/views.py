from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from member.models import Member

# 로그인
def login(request):
  return render(request, 'login.html')


# ajax 통신
# @csrf_exempt # csrf_token 예외처리
def loginChk(request):
  # {"name":"kim","age":20}
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  print("html에서 넘어온 데이터:", id, pw)
  qs = Member.objects.filter(id=id,pw=pw)
  
  # 변수 보내는 방법
  # qs = Member.objects.filter(id=id,pw=pw)
  # if qs:
  #   context = {"id":qs[0].id, "nickname":qs[0].nickname,"result":"success"}
  # else:
  #   context = {"result":"fail"}
  # return JsonResponse(context)

  # filter로 검색하여  객체 보내는 방법
  qs = list(Member.objects.filter(id=id,pw=pw).values()) # qs를 리스트 타입으로 변경 후
  # 변경하지 않으면 에러 발생
  if qs:
    context = {"member":qs,"result":"success"}
  else:
    context = {"result":"fail"}
  return JsonResponse(context)

  # get으로 검색하여 객체 보내는 방법
  # qs = Member.objects.get(id=id,pw=pw) # qs를 리스트 타입으로 변경 후
  # json_qs = serializers.serialize('json',qs)
  # 변경하지 않으면 에러 발생
  # if qs:
  #   context = {"member":json_qs,"result":"success"}
  # else:
  #   context = {"result":"fail"}
  # return JsonResponse(context)


################

def join01(request):
  return render(request, 'join01.html')


def join02(request):
  return render(request, 'join02.html')


# ajax 통신
def idChk(request):
  id = request.POST.get("id","")
  print("id: ",id)
  context = {"id":id,"result":"success"}
  return JsonResponse(context)
