from django.contrib import admin
from django.urls import path
from . import views
from .views import ForumStartView, ForumDetailView, CreatePostView, EditPostView, DeletePostView, CreateReplyView

urlpatterns = [
    path('', views.home, name="home"),
    path('forum-start/',ForumStartView.as_view(),name="forum-start"),
    path('forum/<int:pk>', ForumDetailView.as_view(), name = "post-detail"),
    path('create-post/', CreatePostView.as_view(), name="create-post"),
    path('forum/edit/<int:pk>', EditPostView.as_view(), name="edit-post"),
    path('forum/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),
    path('forum/<int:pk>/reply', CreateReplyView.as_view(), name="create-reply")
]