"""This file sets up the forms for the commissions app."""
from django import forms
from .models import Commission, Job, JobApplication


class CommissionForm(forms.ModelForm):
    """
    Class for the Commission Form.

    Contains the fields 'title', 'description', and 'status' 
    Other fields are added automatically.
    """
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']
        

class JobForm(forms.ModelForm):
    """
    Class for the Job Form.

    Contains the fields 'role', 'manpower_required', and 'status'
    Other fields are added automatically.
    """
    class Meta:
        model = Job
        fields = ['role', 'manpower_required', 'status']
