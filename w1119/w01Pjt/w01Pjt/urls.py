from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls), # admin 관리자 사이트
    path('students/', include('students.urls')),
    path('', include('home.urls')),
]
