"""This file sets up the forms for the commissions app."""
from django import forms
from .models import Commission, Job, JobApplication


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']
        

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'manpower_required', 'status']


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['status']
        wdgets = {
            'status', forms.Select()
        }



