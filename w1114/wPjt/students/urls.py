from django.urls import path,include
from . import views

app_name = 'students'
urlpatterns = [
    path('students/', views.students, name='students'),
]