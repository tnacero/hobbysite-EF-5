from django import forms

from .models import *

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']   

class WikiUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']