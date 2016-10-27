from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import User

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'user_list'