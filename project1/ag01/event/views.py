from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json 타입
from django.utils import timezone
from member.models import Member
from event.models import Attendance


def calendar(request):
  if request.method == "GET":
    return render(request, 'calendar.html')
  else:
    # qs = Member.objects.filter(id=aId)
    aId = request.session['session_id']
    today = timezone.now().date()
    print(aId)
    attendance = Attendance.objects.get(aId=aId)
    if attendance.last_checked != today:
      attendance.count += 1
      attendance.last_checked = today
      attendance.aDate = today    
      attendance.save()
      return JsonResponse({"result":"success","count":attendance.count})
    else:
      return JsonResponse({"result":"already_checked"})



  