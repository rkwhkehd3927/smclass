from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('blist/', views.blist, name='blist'), # 글 목록
    path('bwrite/', views.bwrite, name='bwrite'), # 글 쓰기
    path('bview/<int:bno>/', views.bview, name='bview'), # 글 상세
    path('bdelete/<int:bno>/', views.bdelete, name='bdelete'), # 글 삭제
    path('bupdate/<int:bno>/', views.bupdate, name='bupdate'), # 글 수정
    path('breply/<int:bno>/', views.breply, name='breply'), # 답글 쓰기
]
