"""This file defines the forms used by the different views."""
from django import forms
from .models import Comment

class CommentForm(forms.Form):
    """Creates the form to be used by the model Comment"""
    
    class Meta:
        """This class uses metadata from the models 
        import to get the Comment form's fields."""
        model = Comment
        fields = ['author', 'thread', 'entry']

from .models import Thread

class ThreadForm(forms.ModelForm):
    """Creates the form to be used by the create and add views"""
    
    class Meta:
        """This class uses metadata from the models 
        import to get the Thread form's fields."""
        model = Thread
        fields = ['title', 'category', 'entry', 'image', 'updated_on']