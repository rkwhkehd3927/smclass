from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse


from students.models import Student
# Create your views here.

def write(request):
  print("학생등록페이지 호출")
  return render(request, 'stuWrite.html')

# stuWrite.html 입력창에 정보를 입력하고 '저장'을 누르면 save() 함수 실행
def save(request):
  print("학생정보저장 호출")
  if request.POST == 'POST':
    print("post")
  else:
    print("get1 : ", request.GET)
  if request.GET : 
    print("get2 : ", request.GET)
  

  if request.POST:  # 넘어온 정보를 각 변수에 저장
    print("post2")
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print(name,major,grade,age,gender)

    # 각 변수들에 저장된 정보를 Student 테이블? 클래스? 로 받아온 다음, qs에 저장
    qs = Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
    qs.save()
    
  return HttpResponseRedirect(reverse('index'))


def list(request):
  qs = Student.objects.all()
  context = {"list":qs}
  return render(request,'stuList.html',context)
