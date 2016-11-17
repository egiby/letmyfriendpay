from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
