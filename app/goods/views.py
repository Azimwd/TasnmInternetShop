from django.core.paginator import Paginator
from django.shortcuts import render
from goods.utils import q_search
from goods.models import Products


def catalog(request, category_slug = None, page = 1):

    page = request.GET.get('page', 1)

    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    query = request.GET.get('q', None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)
    
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 6)
    current_page = paginator.page(page)

    context = {
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/shop.html", context)


def product(request, product_slug):
    productslug = Products.objects.get(slug=product_slug)

    context = {"product": productslug}
    return render(request, "goods/product.html", context=context)