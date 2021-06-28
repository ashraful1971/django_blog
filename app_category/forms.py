from django import forms
from django.forms import fields
from app_category.models import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Category Name...'}))
    class Meta:
        model = Category
        fields = ['name',]