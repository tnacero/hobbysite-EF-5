"""This file sets up the views for the user_management app."""
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm, CustomUserCreationForm

from django.contrib.auth.models import User
# Create your views here.

class UserCreateView(CreateView):
    """
    Class for the User Create View.

    Contains the form for create a user.
    Creates a profile when a user is created.
    """
    model = User
    form_class = CustomUserCreationForm
    template_name = 'profile_user_create.html'

    def get_success_url(self):
        return reverse_lazy('home:homepage')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        profile = Profile()
        profile.user = user
        profile.name = user.username
        profile.email = user.email
        profile.save()
        return super().form_valid(form)

class ProfileForbiddenView(TemplateView):
    """
    Class for the Profile Forbidden View
    """
    template_name = 'profile_forbidden.html'


class ProfileUpdateView(UpdateView, LoginRequiredMixin):
    """
    Class for the Profile Update View

    Contains the form to update the name of the profile of a user
    """
    model = Profile
    form_class = ProfileForm
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'profile_form.html'

    def get_success_url(self):
        return reverse_lazy('home:homepage')

    def get_object(self):

        object = get_object_or_404(User, username=self.kwargs.get("username"))

        if self.request.user.username == object.username:
            return object
        else:
            return reverse_lazy('user_management:profile-forbidden')

 