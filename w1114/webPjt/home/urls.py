from django.urls import path,include
from . import views


#### 메인 URL ####
app_name = ''
urlpatterns = [
    ### url 주소, views.py.함수명, url 이름
    # http://127.0.0.1:8000/students/reg/ (연결방식 1)
    # students: reg (연결방식 2)
    path('', views.index,name='index'),
]
