from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView
from django.views.generic import ListView

from .models import User
from .forms import CustomUserCreationForm

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'user_list'