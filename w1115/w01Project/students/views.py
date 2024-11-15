from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student


# Create your views here.




### 학생입력페이지 호출
# request 안에 모든 정보가 들어오기 때문에 무조건 request 를 받음
def write(request):
  print("학생등록페이지 호출")
  # students/templates 폴더 생성 후 stuWrite.html 생성
  # wirte() 함수 실행 시, stuWrite.html 이 실행되도록 하는 명령어
  return render(request,'stuWrite.html') # 파일이름이 꼭 동일할 필요는 없음

### 학생 저장
def save(request):
  print("학생정보저장 호출")
  if request.POST == 'POST':
    print("post")
  else: 
    print("get1 : ", request.GET)
  
  if request.GET :
    print("get2 : ", request.GET)

  if request.POST:
    print("post2")
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print(name,major,grade,age,gender)

    qs = Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
    qs.save()

  return HttpResponseRedirect(reverse('index'))
  # return redirect('index')
  # redirect('/')
  # return redirect(reverse('index')) # reverse : app_name


### 학생 전체 리스트 호출
def list(request):
  # 학생전체리스트 전달
  qs = Student.objects.all()
  # 정보 전달 변수 생성
  context = {"list":qs} # 변수 'list' 에 qs 넣기
  # list() 실행될 때, context도 함께 전달
  return render(request,'stuList.html',context) 


# ============================
# 선생님이 한 방식인데 꼭이렇게 할 필요는 없고 이런방식도 있다~ 라는 것

## 1.write페이지 열기,2.write 학생정보 저장
# def write(request):
#   if request.method == "GET":
#     print("write GET방식 호출")
#     return render(request,'write.html')
#   else:
#     print("write POST방식 호출")
#     name = request.POST['name']
#     major = request.POST['major']
#     grade = request.POST['grade']
#     age = request.POST['age']
#     gender = request.POST['gender']
#     print(name,major,grade,age,gender)
#     # qs = Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
#     # qs.save()
#     return redirect('index')