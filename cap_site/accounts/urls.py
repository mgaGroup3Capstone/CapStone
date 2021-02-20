from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('forum/', views.forum),
    path('calendar/', views.calendar),
]
