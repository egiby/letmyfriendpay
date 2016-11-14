from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Wallet, Balance


class WalletListView(ListView):
    model = Wallet
    template_name = 'wallet/wallet_list.html'
    context_object_name = 'wallet_list'


class WalletView(DetailView):
    model = Wallet
    template_name = 'wallet/wallet.html'
    context_object_name = 'wallet'


class WalletCreateView(CreateView):
    model = Wallet
    template_name = 'wallet/create_wallet.html'
    fields = ('description', 'members')

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save(commit=False)

        for user in form.cleaned_data['members']:
            balance = Balance()
            balance.wallet = self.object
            balance.member = user
            balance.member_balance = 0.0
            # balance.save()

        return super(WalletCreateView, self).form_valid(form)

    success_url = reverse_lazy('users:user_profile')
