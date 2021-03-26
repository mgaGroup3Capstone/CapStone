from django.urls import path
from . import views
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
# from .views import UserRegisterView
# UserEditView

urlpatterns = [
	path('register/', UserRegisterView.as_view(), name = 'register'),
	# path('edit_profile/', UserEditView.as_view(), name = 'edit_profile'),
	#
    # path('profile/edit/', views.edit_profile, name = "edit_profile"),
    path('edit_profile/', UserEditView.as_view(), name = 'edit_profile'),
    # path('profile/change-password/', views.change_password, name = "change_password"),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
]