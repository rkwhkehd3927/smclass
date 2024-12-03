from django.shortcuts import render
from member.models import Member
from event.models import Attendance


def calendar(request):
  if request.method == "GET":
    return render(request, 'calendar.html')
  else:
    date = request.POST['date']
    names = Member.objects.all()
    # qs = Member.objects.filter(id=id)
    context = {'date':date,'names':names}
    return render(request, 'calendar.html', context)

def chk(request):
  id = request.POST['id']
  attendance = Attendance.objects.filter(id=id)
  attendance.name = request.POST['name']
  attendance.attendance = request.POST['attendance']
  attendance.date=request

