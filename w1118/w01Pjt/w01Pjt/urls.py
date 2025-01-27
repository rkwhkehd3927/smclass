from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')), # urls 추가1
    path('', include('home.urls')), # urls 추가2
    path('board/', include('board.urls')), # urls 추가2
]
