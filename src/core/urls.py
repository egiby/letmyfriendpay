from django.conf.urls import url, include
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout
from django.views.generic import CreateView
from django.conf import settings

from .forms import CustomUserCreationForm
from .views import UserListView


urlpatterns = [
    # url(r'^(?P<slug>\w+)/$', UserListView.as_view(), name="user")
    url(r'user_list', UserListView.as_view(), name='user_list'),
    url(r'^login/', login, {'template_name': 'authorization/login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'authorization/logout.html'}, name="logout"),
    url('^register/', CreateView.as_view(
        template_name='authorization/register.html',
        form_class=CustomUserCreationForm,
        success_url=settings.LOGIN_URL
    )),
    url('', include('django.contrib.auth.urls')),
]
