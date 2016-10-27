from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from .views import UserListView

urlpatterns = [
    # url(r'^(?P<slug>\w+)/$', UserListView.as_view(), name="user")
    url(r'user_list', UserListView.as_view(), name='user_list'),
]
