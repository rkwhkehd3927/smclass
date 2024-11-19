from django.shortcuts import render, redirect
from students.models import Student

# 학생 정보 등록
def write(request):
  if request.method == 'POST': # 학생 등록시 입력한 데이터들 POST 방식으로 받아오기
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    # hobby = request.POST['hobby']
    hobbys = request.POST.getlist('hobby')

    print(name)
    # print('hobby 1개 : ', hobby)
    print('hobby 복수 : ', hobbys)

    qs = Student(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobbys) 
    qs.save() # qs 에 저장

    return redirect('/students/list/') # 리스트로 전송 # 나중에 리스트로 가도록 바꿀거임 
  
  else: # GET 호출 
    return render(request, 'write.html') # 입력받기 전, 등록 창 띄우기

# 학생 전체 리스트
def list(request):
  qs = Student.objects.all() # 입력받은 데이터 전부 
  context = {"slist":qs} # 'slist' 에 qs 넣기
  return render(request, 'list.html', context)


# 학생 정보 상세 페이지
def view(request,name):
  qs = Student.objects.get(name=name)
  context = {'stu':qs} # 'stu' 에 qs 넣기
  return render(request, 'view.html', context)


# 학생 정보 수정 및 저장
def update(request):
  if request.method == 'GET':
    name = request.GET['name'] # view 에서 이름 정보 받아와서
    print(name)
    qs = Student.objects.get(name=name) # 같은 이름의 데이터 찾은 다음,
    context = {"stu":qs} # 'stu' 에 qs 넣기
    return render(request, 'update.html', context) # 찾은 데이터들 update.html 로 내보내기
  else: # 수정한 정보 받아오기
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')

    # 받아온 새로운 데이터들 qs에 저장하기
    qs = Student.objects.get(name=name)
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.hobby = hobby
    qs.save() 

    return redirect('students:view',name)  # 저장한 정보들 view.html 로 전송
    # name은 urls로 전송하기 위해 return함
    # path('view/<str:name>/', views.view, name='view'), <- 여기의 name으로 전송되는 거임


# 학생 정보 삭제
def delete(request,name):
  print("삭제정보 이름: ", name) 
  Student.objects.get(name=name).delete() # 삭제
  return redirect('/students/list') # delete() <- 함수 기능을 /students/list 에서 실행