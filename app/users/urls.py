from django.contrib import admin
from django.urls import path
from users.views import *

app_name = 'user'

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("registration/", registration, name="registration"), 
    path("login/", login, name="login"), 
    path("logout/", logout, name="logout"),
    
]
