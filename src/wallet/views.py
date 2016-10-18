from django.shortcuts import render
from django.views.generic import ListView

from .models import Wallet


class WalletView(ListView):
    model = Wallet
    template_name = 'wallet/wallets.html'
