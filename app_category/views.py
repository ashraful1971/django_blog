from app_category.models import Category
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from app_category.forms import CategoryForm
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def show_categories(request):
    data = Category.objects.filter(author=request.user)
    return render(request, 'backend/category/categories.html', context={'data':data})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.slug = slugify(new_category.name)
            new_category.author = request.user
            new_category.save()
            messages.success(request, 'New category created!')
            form = CategoryForm()
    else:
        form = CategoryForm()
    return render(request, 'backend/category/add_category.html', context={'form':form})

@login_required
def edit_category(request, pk):
    data = Category.objects.get(pk=pk)
    if data and data.author == request.user:
        form = CategoryForm(instance=data)
        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=data)
            form.save()
            messages.success(request, 'Category updated!')
        return render(request, 'backend/category/edit_category.html', context={'form':form})
    else:
        messages.error(request, 'You are not allowed to edit this category!')
        return HttpResponseRedirect(reverse('app_category:show_category'))

@login_required
def delete_category(request, pk):
    data = Category.objects.get(pk=pk)
    if data and data.author == request.user:
        data.delete()
        messages.success(request, 'Category deleted!')
    return HttpResponseRedirect(reverse('app_category:show_category'))