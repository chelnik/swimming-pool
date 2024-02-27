from django.urls import path
from django.contrib.auth.views import LoginView

from .views import register_view, signin_view, logout_view, user_detail

app_name = 'users'

urlpatterns = [
    path('signin/', signin_view, name='login'),
    path('signup/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('me/', user_detail, name='user_detail'),
]
