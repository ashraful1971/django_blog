from django.db.models import fields
from app_auth import models
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Enter Your Username...'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Enter Your Email...'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control form-control-user', 'placeholder':'Enter Your Password...'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Enter Your Username...'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control form-control-user', 'placeholder':'Enter Your Password...'}))
    class Meta:
        model = User
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Enter Your First Name...'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Enter Your Last Name...'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Enter Your Email...'}))
    old_password = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'password', 'class':'form-control form-control-user', 'placeholder':'Enter Your Old Password...'}))
    new_password = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'password', 'class':'form-control form-control-user', 'placeholder':'Enter Your New Password...'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',]

class UserInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    twitter = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Twitter Profile Link'}))
    facebook = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Facebook Profile Link'}))
    instagram = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Instagram Profile Link'}))
    linkedin = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'LinkedIn Profile Link'}))
    github = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Github Profile Link'}))
    image = forms.ImageField(required=False)
    class Meta:
        model = models.UserInfo
        fields = ['image', 'bio', 'twitter', 'facebook', 'instagram', 'linkedin', 'github',]