from app_category.models import Category
from django import forms
from app_post.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Content'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}), queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image',]