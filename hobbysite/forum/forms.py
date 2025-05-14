"""This file defines the forms used by the different views."""
from django import forms
from .models import Comment

class CommentForm(forms.Form):
    """Creates the form to be used by the model Comment"""
    
    class Meta:
        """This class uses metadata from the models 
        import to get the Comment form's fields."""
        model = Transaction
        fields = ['product', 'amount', 'status']
