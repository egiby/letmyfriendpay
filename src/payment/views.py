from django.views.generic import DetailView

from .models import Payment


class PaymentView(DetailView):
    model = Payment
    template_name = 'payment.html'
    context_object_name = 'payment'
