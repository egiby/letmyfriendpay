from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout

from .views import UserListView, UserView, UserUpdateView, UserCreateView

urlpatterns = [
    url(r'^user_list', UserListView.as_view(), name='user_list'),
    url(r'^login/', login, {'template_name': 'authorization/login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'authorization/logout.html'}, name="logout"),
    url('^register/', UserCreateView.as_view()),
    url(r'^profile', login_required(UserView.as_view(), login_url=settings.LOGIN_URL), name="user_profile"),
    url(r'^edit_profile/', login_required(UserUpdateView.as_view(), login_url=settings.LOGIN_URL), name="edit_user"),
]
