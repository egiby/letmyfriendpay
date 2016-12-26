from django.forms import ModelForm

from .models import Payment


class PaymentCreateForm(ModelForm):
    class Meta:
        model = Payment
        fields = ('amount', 'currency')
