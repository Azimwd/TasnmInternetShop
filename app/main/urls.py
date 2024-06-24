from django.contrib import admin
from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", index, name="index"), 
]
