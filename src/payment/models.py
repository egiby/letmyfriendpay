from django.db import models
from django.conf import settings


class Payment(models.Model):
    wallet = models.ForeignKey('wallet.Wallet', related_name='wallets', null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)

    CURRENCY_CHOICES = [('USD', 'United States dollar'),
                        ('RUB', 'Russian rouble'),
                        ('EUR', 'Euro')]

    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, null=True)

    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Transaction',
                                     through_fields=('payment', 'user'),
                                     related_name='payment_members')


class Transaction(models.Model):
    payment = models.ForeignKey(Payment)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    difference = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    time = models.DateTimeField(auto_now_add=True)
