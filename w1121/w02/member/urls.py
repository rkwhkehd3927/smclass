from django.urls import path, include
from . import views

app_name = 'member'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join01/', views.join01, name='join01'),
]
