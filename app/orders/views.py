from django.shortcuts import render

def craete_order(request):

    return render(request, 'orders/create_order.html')
