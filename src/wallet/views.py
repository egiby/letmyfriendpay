from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from core.models import User
from payment.forms import PaymentCreateForm
from payment.models import Payment, Transaction
from .forms import WalletEditForm
from .models import Wallet, Balance


class WalletListView(ListView):
    model = Wallet
    template_name = 'wallet_list.html'
    context_object_name = 'wallet_list'


class WalletView(CreateView):
    # model = Payment
    template_name = 'wallet.html'
    # context_object_name = 'wallet'
    form_class = PaymentCreateForm

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.wallet = get_object_or_404(Wallet.objects.filter(id=pk, balance__member__exact=self.request.user))
        return super(WalletView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(WalletView, self).get_context_data(**kwargs)

        context['payments'] = Payment.objects.filter(wallet=self.wallet)
        context['wallet'] = self.wallet
        return context

    def form_valid(self, form):
        if abs(form.instance.amount) < 3e-2:
            return HttpResponseRedirect(self.get_success_url())

        form.instance.creator = self.request.user
        form.instance.wallet = self.wallet
        response = super(WalletView, self).form_valid(form)

        members = Balance.objects.filter(wallet=self.wallet)

        for member in members:
            transaction = Transaction()
            transaction.user = member.member
            transaction.payment = self.object
            # currency? not in alpha version

            # there will be error because of precision
            transaction.difference = -self.object.amount / len(members)
            if member.member == self.request.user:
                transaction.difference += self.object.amount

            transaction.save()
            member.member_balance += transaction.difference
            member.save()

        return response

    def get_success_url(self):
        return '#'


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
        return "/wallets/" + str(self.pk)


class BalanceView(DetailView):
    model = Wallet

    def render_to_response(self, context, **response_kwargs):
        data = dict(self.object.balance_set.all().values_list('member_id', 'member_balance'))
        return JsonResponse(data)
