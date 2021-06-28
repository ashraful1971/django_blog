from django_blog import views
from django.urls import path
from . import views

app_name = 'app_auth'

urlpatterns = [
    path('', views.user_login, name='index'),
    path('panel', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]