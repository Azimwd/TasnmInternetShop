from django.shortcuts import render
from goods.models import Products

def shop(request):
    products = Products.objects.all()
    context = {
        'products': products,
    }
    return render(request, "goods/shop.html",context)


def singleproduct(request):
    return render(request, "goods/single-product.html")
