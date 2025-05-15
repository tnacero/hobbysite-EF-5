from django import forms

from .models import *

class WikiCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']

class WikiCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']   

class WikiUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']