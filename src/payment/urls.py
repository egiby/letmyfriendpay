from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from payment.views import PaymentView

urlpatterns = [
    url('^(?P<pk>\d+)/$', PaymentView.as_view()),
]
