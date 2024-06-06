from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def checkout(request):
    return render(request, "checkout.html")


def shop(request):
    return render(request, "shop.html")


def singleproduct(request):
    return render(request, "single-product.html")


def wishlist(request):
    return render(request, "wishlist.html")


def registration(request):
    return render(request, "registration.html")


def login(request):
    return render(request, "login.html")
