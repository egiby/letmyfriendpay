from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from core.models import User
from .forms import WalletEditForm
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
        response = super(WalletCreateView, self).form_valid(form)

        balance = Balance()
        balance.member = self.request.user
        balance.wallet = self.object
        balance.member_balance = 0.00
        balance.save()

        return response

    def get_success_url(self):
        return str(self.object.pk)


class WalletEditView(UpdateView):
    model = Wallet
    template_name = 'edit_wallet.html'
    fields = ('description', )

    def dispatch(self, request, *args, **kwargs):
        self.pk = int(kwargs['pk'])
        return super(WalletEditView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Wallet, author=self.request.user, pk=self.pk)

    def get_success_url(self):
        return "/wallets/" + str(self.pk)


class WalletAddMemberView(UpdateView):
    template_name = 'add_member.html'

    form_class = WalletEditForm

    def dispatch(self, request, *args, **kwargs):
        self.pk = int(kwargs['pk'])
        return super(WalletAddMemberView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Wallet, author=self.request.user, pk=self.pk)

    def form_valid(self, form):
        response = super(WalletAddMemberView, self).form_valid(form)
        if User.objects.filter(username=form.cleaned_data['new_member']):
            user = User.objects.get(username=form.cleaned_data['new_member'])
            if not Balance.objects.filter(wallet=self.object, member=user):
                balance = Balance()
                balance.member = user
                balance.wallet = self.object
                balance.member_balance = 0.00
                balance.save()

        return response

    def get_success_url(self):
        return "/wallets/" + str(self.pk) + "/edit_wallet"
