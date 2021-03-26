from django.urls import path, include
from . import views

urlpatterns = [
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
	path('event/new/', views.event, name='event_new'),
	# path(r'event/edit/(?P<event_id>\d+)/', views.event, name='event_edit'), # old path may need to use anyway
    # path(r'event/edit/(<event_id>\d+)/', views.event, name='event_edit'), # another iteration of path may need to use anyway
    path('event/edit/<event_id>/', views.event, name='event_edit'),
]