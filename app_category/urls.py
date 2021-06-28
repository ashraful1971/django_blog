from django.urls import path
from . import views

app_name = 'app_category'

urlpatterns = [
    path('', views.show_categories, name='show_category'),
    path('add/', views.add_category, name='add_category'),
    path('edit/<int:pk>', views.edit_category, name='edit_category'),
    path('delete/<int:pk>', views.delete_category, name='delete_category'),
]