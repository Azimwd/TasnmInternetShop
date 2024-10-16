from django.contrib import admin
from django.urls import path
from orders.views import *

app_name = 'orders'

urlpatterns = [
    path("craete_order/", craete_order, name="craete_order"),

]
