from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog/posts.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'