from django.shortcuts import render
from django.views.generic import(
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView, 
	DeleteView,)
from .models import Post, Reply
from .forms import PostForm, ReplyForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
# 	return render(request, 'forumapp/home.html', {})

def home(request):
	return render(request, 'forum/home.html')

class ForumStartView(ListView):
	model = Post
	template_name = 'forum/forum_start.html'
	ordering = ['-date_created']
	# ordering = ['-id']# post in order new to old with out date

class ForumDetailView(DetailView):
	model = Post
	template_name = 'forum/post_detail.html'

class CreatePostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'forum/create_post.html'
	# fields = '__all__'
	# fields = ('title', 'body')

class CreateReplyView(CreateView):
	model = Reply
	form_class = ReplyForm
	template_name = 'forum/create_reply.html'
	# fields = '__all__'
	# success_url = reverse_lazy('home')

	# associates reply with a post.
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

class EditPostView(UpdateView):
	model = Post
	template_name = 'forum/edit_post.html'
	fields = ['title', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'forum/delete_post.html'
	success_url = reverse_lazy('forum-start')
