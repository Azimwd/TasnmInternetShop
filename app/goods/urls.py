from django.urls import path
from goods.views import *

app_name = 'goods'

urlpatterns = [
    path("", shop, name = "index"),
    path("singleproduct/", singleproduct, name = "singleproduct"),  
]
