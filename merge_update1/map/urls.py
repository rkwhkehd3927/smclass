from django.urls import path, include
from . import views

app_name = 'map'
urlpatterns = [
    path('success/', views.success, name='success'),
    path('test4/', views.test4, name='test4'),
    path('weather/', views.weather, name='weather')
]

