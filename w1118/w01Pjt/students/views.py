from django.shortcuts import render, redirect
from students.models import Student


# 학생상세페이지 - url
def view(request,name):
  print("modify 이름정보: ", name)
  qs = Student.objects.filter(name = name) # 데이터 1개 넘어옴(list타입의 데이터) # 정보가 없을 경우, {} = 에러는 안남 
  print(qs)
  context = {'stu':qs[0]}
  return render(request,'view.html',context)
  # qs = Student.objects.get(name = name) # 정보가 없을 경우, 에러
  # qs = get_object_or_404(Student,name = name) # 정보가 없을 경우, 구문을 리턴



# 학생수정페이지1 - url, 매개변수로 데이터값을 전달받음.
def modify(request,name):
  if request.method == 'GET':
    print("modify 이름정보: ", name)
    # 1개의 데이터를 가져오기
    qs = Student.objects.filter(name=name)
    context = {'stu':qs[0]} # 'stu' 에 qs[0] 넣기
    return render(request, 'update.html', context)
  else:
    print("POST 호출")
    # qs = Student.objects.filter(name=name) # 얘는 왜 저장이 안됑 ?ㅠㅠ
    qs = Student.objects.get(name=name)
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print("수정 정보: ",name,major,grade,age,gender)
    ## db 저장
    # qs[0].major = major
    # qs[0].grade = grade
    # qs[0].age = age
    # qs[0].gender = gender
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.save()
    return redirect('students:list')


# 학생수정페이지2 - 파라미터
def modify2(request):
  name = request.GET.get('name')
  print("modify2 이름정보: ", name)
  # 1개의 데이터를 가져오기
  qs = Student.objects.filter(name=name)
  context = {'stu':qs[0]} # 'stu' 에 qs[0] 넣기
  return render(request, 'update.html', context)

# 학생수정페이지3 - appName, 매개변수로 데이터값을 전달받음.
def modify3(request,name):
  print("modify3 이름정보: ", name)
  # 1개의 데이터를 가져오기
  qs = Student.objects.filter(name=name)
  context = {'stu':qs[0]} # 'stu' 에 qs[0] 넣기
  return render(request, 'update.html', context)



# 학생 삭제
def delete(request,name):
  print("삭제정보 :",name)
  Student.objects.get(name=name).delete()
  return redirect("students:list")




# 학생리스트
def list(request):
  qs = Student.objects.all()
  # context = 데이터를 전달하는 변수
  context = {"slist":qs}
  return render(request, 'list.html', context)

# 학생입력 페이지 호출
def write(request):
  if request.method == 'GET':
  # render = html 파일 호출
    print("GET 방식으로 들어옴")
    return render(request, 'write.html')
  else:
    print("POST 방식으로 들어옴")
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print("입력데이터 : ",name,major,grade,age,gender)

    ## DB 저장
    Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender)
    print("학생 정보 저장")
    return redirect("/students/list")
  

# 학생입력정보저장
# def doWrite(request):S
#   if request.method == 'POST':
#     name = request.POST['name']
#     major = request.POST['major']
#     grade = request.POST['grade']
#     age = request.POST['age']
#     gender = request.POST['gender']
#     print("입력데이터 : ",name,major,grade,age,gender)
#     return redirect("/")
#   else:
#     print("해당되는 데이터가 없습니다.")
