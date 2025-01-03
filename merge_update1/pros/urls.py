from django.urls import path
from . import views

app_name = "pros"
urlpatterns = [
    ### 로그인
    path("login/", views.prologin, name="prologin"),  # 로그인
    path("loginChk/", views.prologinChk, name="prologinChk"),  # 로그인 체크
    path("layout/", views.prolayout, name="prolayout"),  # 로그인
]
