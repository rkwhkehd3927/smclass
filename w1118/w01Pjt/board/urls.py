from django.urls import path, include
from . import views # 현재 폴더안에서 views 가져오기

app_name = 'board' # name:url 시 사용
urlpatterns = [
    path('list/', views.list,name='list'), # 학생입력페이지
]
