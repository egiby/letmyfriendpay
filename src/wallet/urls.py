from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import WalletListView, WalletView, WalletCreateView

urlpatterns = [
    url(r'^wallet_list', WalletListView.as_view()),
    url(r'^(?P<pk>\d+)/', login_required(WalletView.as_view(), login_url=settings.LOGIN_URL)),
    url(r'^create_wallet', login_required(WalletCreateView.as_view(), login_url=settings.LOGIN_URL), name='create'),
]
