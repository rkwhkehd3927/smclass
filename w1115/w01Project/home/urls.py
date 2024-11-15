from django.urls import path, include

# import func 이랑 비슷한 거임
from . import views # views 파일 속 함수()를 실행할 수 있도록 함

app_name = '' # app 이름= '이름' 으로 접근할 때 사용
urlpatterns = [
  # write/ 로 실행하여 views.py 로 연결 - views 안의 함수 호출
    path('',views.index,name='index')
]
