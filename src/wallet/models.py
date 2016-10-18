from django.conf import settings
from django.db import models


class Wallet(models.Model):
    time_of_creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='created_wallets')
    description = models.TextField(max_length=1024, blank=True, null=True)

    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Balance',
                                     through_fields=('wallet', 'member'),
                                     related_name='my_wallets')


class Balance(models.Model):
    wallet = models.ForeignKey(Wallet)
    member = models.ForeignKey(settings.AUTH_USER_MODEL)
    member_balance = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
