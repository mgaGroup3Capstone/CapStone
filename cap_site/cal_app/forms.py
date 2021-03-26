from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput
from calendar import HTMLCalendar
from cal_app.models import Event


class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = '__all__'# can be a list of form fields 
		# datetime-local is a HTML5 input type, format to make date time show on fields
		widgets = {
    		'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%m-%d-%Y %H:%M'),
			'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%m-%d-%Y %H:%M'),
		}
		exclude = ['event_owner']

	def __init__(self, *args, **kwargs):
		super(EventForm, self).__init__(*args, **kwargs)
		# input_formats to parse HTML5 datetime-local input to datetime field
		self.fields['start_time'].input_formats = ('%m-%d-%Y %H:%M',)
		self.fields['end_time'].input_formats = ('%m-%d-%Y %H:%M',)

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		
		# generates list of event for each day.  
		for event in events_per_day:
			d += f'<li> {event.get_html_url} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by user who is currentlly logged in, 
	# year, and month
	def formatmonth(self, cur_user,withyear=True):
		events = Event.objects.filter(event_owner=cur_user, start_time__year=self.year, start_time__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
