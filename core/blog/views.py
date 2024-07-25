from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView,CreateView,FormView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .form import *
from accounts.models import Profile


# Create your views here.

#def indexview(request):
#    return render (request,"index.html")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        return context
    

class PostList(LoginRequiredMixin,ListView):
    #model = Post
    #queryset = Post.objects.all()
    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by('-id')
        return posts

    context_object_name = "posts"

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)
    

class PostEdit(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/post/'