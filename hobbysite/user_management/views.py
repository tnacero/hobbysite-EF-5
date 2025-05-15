from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'profile_user_create.html'

class ProfileForbiddenView(TemplateView):
    template_name = 'profile_forbidden.html'


class ProfileUpdateView(UpdateView, LoginRequiredMixin):
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

 