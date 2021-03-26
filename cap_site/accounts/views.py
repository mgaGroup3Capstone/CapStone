from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm

# class UserRegisterView(generic.CreateView):
# 	form_class = SignUpForm
# 	template_name = 'registration/register.html'
# 	success_url = reverse_lazy('login')

# class UserEditView(generic.UpdateView):
# 	form_class = UserChangeForm
# 	template_name = 'registration/edit_profile.html'
# 	success_url = reverse_lazy('home')

# 	def get_object(self):
# 		return self.request.user



# def profile(request):
# 	args = {'user': request.user}
# 	return render(request, 'registration/profile.html', args)

# def edit_profile(request):
# 	if request.method == 'POST':
# 		form = EditProfileForm(request.POST, instance=request.user)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('/profile')
# 	else:
# 		form = EditProfileForm(instance=request.user)
# 		args = {'form': form}
# 		return render(request, 'registration/edit_profile.html', args)

# def change_password(request):
# 	if request.method == 'POST':
# 		form = PasswordChangeForm(data=request.POST, user=request.user)

# 		if form.is_valid():
# 			form.save()
# 			update_session_auth_hash(request, form.user)
# 			return redirect('/profile')
# 		else:
# 			return redirect('/profile/change-password') 
# 	else:
# 		form = PasswordChangeForm(user=request.user)
# 		args = {'form': form}
# 		return render(request, 'registration/edit_profile.html', args)


class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('home')

class UserRegisterView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user