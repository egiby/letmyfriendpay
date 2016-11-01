from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from .views import WalletView

urlpatterns = [
    url(r'wallet_list', WalletView.as_view()),
]
