from django import forms

from .models import Wallet


class WalletEditForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ()

    new_member = forms.CharField()
