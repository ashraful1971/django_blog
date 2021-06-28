from django.contrib.auth.decorators import login_required
from app_post.forms import PostForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from app_post.models import Post
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your views here.

@login_required
def show_post(request):
    data = Post.objects.filter(author=request.user)
    return render(request, 'backend/post/posts.html', context={'data':data})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = slugify(new_post.title)
            new_post.save()
            messages.success(request,'New post added!')
            form = PostForm()
    else:
        form = PostForm()
    return render(request, 'backend/post/add_post.html', context={'form':form})

@login_required
def edit_post(request, pk):
    data = Post.objects.get(pk=pk)
    if data.author == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=data)
            if form.is_valid():
                current_post = form.save(commit=False)
                current_post.slug = slugify(current_post.title)
                current_post.save()
                messages.success(request,'Post updated!')
                form = PostForm(instance=current_post)
        else:
            form = PostForm(instance=data)
        return render(request, 'backend/post/edit_post.html', context={'form':form})
    else:
        messages.error(request,'You are not allowed to edit this post!')
        return HttpResponseRedirect(reverse('app_post:show_post'))

@login_required
def delete_post(request, pk):
    data = Post.objects.get(pk=pk)
    if data.author == request.user:
        data.delete()
        messages.success(request,'Post deleted!')
    return HttpResponseRedirect(reverse('app_post:show_post'))