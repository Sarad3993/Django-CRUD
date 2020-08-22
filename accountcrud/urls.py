from django.urls import path
from accountcrud.views import *


app_name = 'accountcrud'




urlpatterns = [
    path('signup',signup_user,name='signup'),
    path('login',login_user,name='login'),
    path('logout',logout_user,name='logout')
]