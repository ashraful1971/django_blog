from django.contrib.auth.models import User
from django.shortcuts import render
from app_post.models import Post
from django.core.paginator import Paginator

def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    author_info = User.objects.all()
    if author_info:
        author_info = author_info[0]
    else:
        author_info = None
    return render(request, 'frontend/home.html', context={'posts':page_obj, 'author_info':author_info})

def single_post(request, slug):
    post_data = Post.objects.get(slug=slug)
    author_info = User.objects.all()
    if author_info:
        author_info = author_info[0]
    else:
        author_info = None
    return render(request, 'frontend/single_post.html', context={'post':post_data,'author_info':author_info})