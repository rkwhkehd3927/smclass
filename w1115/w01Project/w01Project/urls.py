
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # root 페이지 주소 뒤에 /admin 이 들어오면 이 사이트를 실행시켜줘! 라는 명령어
    path('admin/', admin.site.urls), 
    # students 폴더에 urls 로 보내줘! 하는 명령어 
    path('students/', include('students.urls')),
    # root 주소 뒤에 '' 빈 공백일때 home 폴더의 urls 로 보내기
    path('', include('home.urls')),
]
