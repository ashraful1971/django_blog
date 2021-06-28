from django.urls import path
from app_post import views

app_name = 'app_post'

urlpatterns = [
    path('', views.show_post, name='show_post'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:pk>', views.edit_post, name='edit_post'),
    path('delete/<int:pk>', views.delete_post, name='delete_post'),
]