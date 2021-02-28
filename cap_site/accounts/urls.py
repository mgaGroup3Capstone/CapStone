from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('forum/', views.forum, name = "forum"),
    path('calendar/', views.calendar, name = "calendar"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('register/', views.registerPage, name = "register"),
]
