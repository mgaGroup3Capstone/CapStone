from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'accounts/home.html')

def forum(request):
	return render(request, 'accounts/forum.html')

def calendar(request):
	return render(request, 'accounts/calendar.html')