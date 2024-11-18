from django.urls import path, include
from . import views # 현재 폴더안에서 views 가져오기

app_name = '' # name:url 시 사용
urlpatterns = [
    path('', views.index,name='index'), # 메인페이지 이름을 주로 'index, main, default' 이렇게 씀
]
