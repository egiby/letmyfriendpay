from django.conf import settings
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import CustomUserCreationForm
from .models import User


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'user_list'


class UserView(DetailView):
    model = User
    template_name = 'users/user.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    # def get_context_data(self, **kwargs):
    #


class UserCreateView(CreateView):
    template_name = 'authorization/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy(settings.LOGIN_URL)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/user_edit.html'
    fields = ('email', 'first_name', 'last_name', 'avatar')

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    success_url = reverse_lazy('users:user_profile')
