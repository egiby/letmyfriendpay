from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Wallet


class WalletListView(ListView):
    model = Wallet
    template_name = 'wallet/wallet_list.html'
    context_object_name = 'wallet_list'


class WalletView(DetailView):
    model = Wallet
    template_name = 'wallet/wallet.html'
    context_object_name = 'wallet'
