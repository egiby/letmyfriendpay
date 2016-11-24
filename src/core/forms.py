from django.contrib.auth.forms import UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'avatar']
        # fields = ['username', 'password1', 'password2']
        fields = ['username', 'password1', 'password2', 'avatar']
