from django.urls import path,include
from . import views

app_name = '' # 아무것도 들어오지 않으면!
urlpatterns = [
    path('', views.index,name='index'),
]
