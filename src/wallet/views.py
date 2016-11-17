from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import Wallet, Balance


class WalletListView(ListView):
    model = Wallet
    template_name = 'wallet_list.html'
    context_object_name = 'wallet_list'


class WalletView(DetailView):
    model = Wallet
    template_name = 'wallet.html'
    context_object_name = 'wallet'


class WalletCreateView(CreateView):
    model = Wallet
    template_name = 'create_wallet.html'
    fields = ('description',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(WalletCreateView, self).form_valid(form)
    #     for user in form.cleaned_data['members']:
    #         balance = Balance()
    #         balance.wallet = self.object
    #         balance.member = user
    #         balance.member_balance = 0.0
    #         balance.save()
    #     return response

    def get_success_url(self):
        return str(self.object.pk)

    # success_url = reverse_lazy('users:user_profile')


class WalletEditView(UpdateView):
    model = Wallet
    template_name = 'edit_wallet.html'
    fields = ('description',)

    def get_object(self, queryset=None):
        return get_object_or_404(Wallet, author=self.request.user)

    def get_success_url(self):
        return str(self.object.pk)
