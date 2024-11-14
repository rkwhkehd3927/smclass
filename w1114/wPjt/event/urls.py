from django.urls import path,include
from . import views

app_name = 'eventView'
urlpatterns = [
    path('eventView/', views.eventView, name='eventView'),
]