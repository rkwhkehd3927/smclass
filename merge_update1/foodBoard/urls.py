from django.urls import path
from . import views

app_name = "foodBoard"
urlpatterns = [
    path("foodList/", views.foodList, name="foodList"),
    path("foodWrite/", views.foodWrite, name="foodWrite"),
    path("foodView/<int:bNo>/", views.foodView, name="foodView"),
    path("foodRes/<int:bNo>/", views.foodRes, name="foodRes"),
    path("Stars/", views.Stars, name="Star"),
    path("Likes/", views.Likes, name="Like"),
    path("Ratings/", views.Ratings, name="Rating"),
]