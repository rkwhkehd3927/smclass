from django.urls import path,include
from . import views

app_name = "board"
urlpatterns = [
    path('blist/', views.blist,name="blist"),
    path('form/', views.form,name="form"),
    path('bview/<int:bno>/', views.bview,name="bview"),
    path('likes/', views.likes, name='likes'),
]


