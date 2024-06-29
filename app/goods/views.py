from django.shortcuts import render
from goods.models import Products

def catalog(request):
    products = Products.objects.all()
    context = {
        'products': products,
    }
    return render(request, "goods/shop.html",context)


def product(request, product_id):
    product = Products.objects.get(id = product_id)

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context = context)

# def singleproduct(request):
#     return render(request, "goods/single-product.html")
