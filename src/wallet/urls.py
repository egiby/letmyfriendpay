from django.conf.urls import url

from .views import WalletListView, WalletView

urlpatterns = [
    url(r'wallet_list', WalletListView.as_view()),
    url(r'^(?P<pk>\d+)/$', WalletView.as_view())
]
