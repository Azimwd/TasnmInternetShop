from django.shortcuts import render
from goods.models import Products

def catalog(request):
    products = Products.objects.all()
    context = {
        'products': products,
    }
    return render(request, "goods/shop.html",context)


def product(request, product_slug):
    productslug = Products.objects.get(slug = product_slug)

    context = {
        'product': productslug
    }
    return render(request, "goods/product.html", context = context)