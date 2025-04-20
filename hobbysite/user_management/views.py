from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import ProfileForm
# Create your views here.

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_form.html'
