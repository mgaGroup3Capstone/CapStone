from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# return reverse('post-detail', args=(str(self.id)))
		return reverse('home')

class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = RichTextField(blank=True, null=True)
	# body = models.TextField()
	date_created = models.DateField(auto_now_add = True)
	category = models.CharField(max_length=255, default= 'help')

	def __str__(self):
		return self.title + '|' + str(self.author)

	def get_absolute_url(self):
		return reverse('post-detail', args=(str(self.id)))

class Reply(models.Model):
	post = models.ForeignKey(Post, related_name="replies", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = RichTextField(blank=True, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)

	def get_absolute_url(self):
		return reverse('post-detail', args=(str(self.post.id)))