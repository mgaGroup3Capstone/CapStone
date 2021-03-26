from django import forms
from .models import Post, Reply

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'body')

		widgets = {
			# can pass any class needed to style in place of 'form-control'
			'title': forms.TextInput(attrs = {'class':'form-control'}),
			'author': forms.TextInput(attrs = {'class':'form-control', 'value':'', 'id':'user', 'type':'hidden'}),
			'body': forms.Textarea(attrs = {'class':'form-control', 'placeholder': 'Enter post content here.'}),
		}

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ('name', 'body')

		widgets = {
			# can pass any class needed to style in place of 'form-control'
			'name': forms.TextInput(attrs = {'class':'form-control', 'value':'', 'id':'user', 'type':'hidden',}),
			'body': forms.Textarea(attrs = {'class':'form-control'}),
		}