from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.
from .forms import CreateUserForm

def home(request):
	return render(request, 'accounts/home.html')

def forum(request):
	return render(request, 'accounts/forum.html')

def calendar(request):
	return render(request, 'accounts/calendar.html')

def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			#redirects to home page when loged in maybe create user page if needed?
			return redirect('home')
		else:
			messages.info(request, 'Incorrect username or password.')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, f'The account {user} was created.' )


			return redirect('login')

	context = {'form':form}
	return render(request, 'accounts/register.html', context)




