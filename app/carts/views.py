
from django.contrib import sessions
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from carts.models import Cart
from goods.models import Categories
from goods.models import Products

def cart_add(request, product_slug):

    goods = Products.objects.all()

    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity = 1)
    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product )
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'], goods)

def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": cart}, request=request)

    response_data = {
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(response_data)

def cart_remove(request, cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])
