from django.shortcuts import get_object_or_404, render
from goods.models import Products


def catalog(request, category_slug):
    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = get_object_or_404(Products.objects.filter(category__slug=category_slug))
    
        
    context = {
        "goods": goods,
    }
    return render(request, "goods/shop.html", context)


def product(request, product_slug):
    productslug = Products.objects.get(slug=product_slug)

    context = {"product": productslug}
    return render(request, "goods/product.html", context=context)