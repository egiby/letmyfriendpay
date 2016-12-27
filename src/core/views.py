from django.conf import settings
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import User

from wallet.models import Wallet


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'user_list'


class UserView(DetailView):
    model = User
    template_name = 'users/user.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['created_wallets'] = Wallet.objects.filter(author=self.request.user)
        context['available_wallets'] = Wallet.objects.filter(members__exact=self.request.user)
        return context


class UserCreateView(CreateView):
    template_name = 'authorization/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy(settings.LOGIN_URL)


class UserUpdateView(UpdateView):
    template_name = 'users/user_edit.html'
    form_class = CustomUserUpdateForm

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    def form_valid(self, form):
        if 'avatar' in form.files:
            form.instance.avatar = form.files['avatar']

        response = super(UserUpdateView, self).form_valid(form)

        return response

    success_url = reverse_lazy('users:user_profile')
