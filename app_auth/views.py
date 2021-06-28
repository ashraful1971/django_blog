from app_auth.forms import LoginForm, RegisterForm, UserForm, UserInfoForm
from app_auth.models import UserInfo
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def check_auth(user):
    if user.is_authenticated:
        return False
    else:
        return True

@login_required
def dashboard(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        userinfo_form = UserInfoForm(request.POST, request.FILES, instance=request.user.user_info)
        if user_form.is_valid() and userinfo_form.is_valid():
            user_model = user_form.save()
            if user_form.cleaned_data.get('old_password') and user_form.cleaned_data.get('new_password'):
                if user_model.check_password(user_form.cleaned_data.get('old_password')):
                    user_model.set_password(user_form.cleaned_data.get('new_password'))
                    user_model.save()
                else:
                    messages.error(request, 'Please check your password!')
            userinfo_form.save()
            messages.success(request, 'Your profile has been updated!')
        else:
            messages.error(request, 'Check the fields and try agian!')
    user_form = UserForm(instance=request.user)
    userinfo_form = UserInfoForm(instance=request.user.user_info)
    return render(request, 'backend/auth/dashboard.html', context={'form1':user_form, 'form2':userinfo_form})

@user_passes_test(check_auth, login_url='/auth/panel')
def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('app_auth:dashboard'))
        else:
            messages.error(request, 'Please check the username and password!')
            return HttpResponseRedirect(reverse('app_auth:login'))
    return render(request, 'backend/auth/login.html', context={'form':form})

@user_passes_test(check_auth, login_url='/auth/panel')
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(new_user.password)
            new_user.save()
            user_info = UserInfo()
            user_info.user = new_user
            user_info.save()
            messages.info(request, 'Account has been created!')
    return render(request, 'backend/auth/register.html', context={'form': form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_auth:login'))