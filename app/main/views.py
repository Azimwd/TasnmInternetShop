from django.shortcuts import render
from goods.models import Categories

def index(request):
    

    context={
        
    }
    return render(request, "main/index.html",context)


def checkout(request):
    return render(request, "main/checkout.html")


def shop(request):
    return render(request, "main/shop.html")


def singleproduct(request):
    return render(request, "main/single-product.html")


def wishlist(request):
    return render(request, "main/wishlist.html")


def registration(request):
    return render(request, "main/registration.html")


def login(request):
    return render(request, "main/login.html")
