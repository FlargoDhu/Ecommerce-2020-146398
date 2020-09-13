"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic.list import ListView 
from json import dumps 

# relative import of forms 
from .models import Products, Orders 


from django.contrib import admin
admin.site.register(Products)
admin.site.register(Orders)


  
class ProductsList(ListView): 
  
    # specify the model for list view 
    model = Products    

def render_items(request, item_name):
    item = get_object_or_404(Products, product_name=item_name)
    return render(request, 'app/TEMPLATE.html', {'item': item })

def add_to_cart_go_to_cart(request, item_name):
    item = get_object_or_404(Products, product_name=item_name)
    request.session['cart'] = True
    request.session[str(item.id)] = item.product_name
    if str(item.id)+"q" in request.session.keys():
        request.session[str(item.id)+"q"] += 1
    else:
        request.session[str(item.id)+"q"] = 1
    return redirect('viewcart')

def view_cart(request):
    if request.session['cart'] == True:
        InsideCart = dict()
        InsideCartQuantity = dict()
        InsideCartPrice = dict()
        string = ""
        keys = request.session.keys()
        for k in keys:
            if k.isdigit() == True:
                item = get_object_or_404(Products, id=k)
                InsideCart[k] = item.product_name
                InsideCartQuantity[k] = request.session[k+"q"]
                InsideCartPrice[k] = item.price_grosze
        InsideCart = dumps(InsideCart)
        InsideCartQuantity = dumps(InsideCartQuantity)
        InsideCartPrice = dumps(InsideCartPrice)
        return render(request, 'app/TEMPLATE_CART_VIEW.html', {'InsideCart': InsideCart, 'InsideCartQuantity': InsideCartQuantity, 'InsideCartPrice': InsideCartPrice })

def order(request):
    if request.session['cart'] == True:
        InsideCart = dict()
        InsideCartQuantity = dict()
        InsideCartPrice = dict()
        total = 0
        keys = request.session.keys()
        for k in keys:
            if k.isdigit() == True:
                item = get_object_or_404(Products, id=k)
                InsideCart[k] = item.product_name
                InsideCartQuantity[k] = request.session[k+"q"]
                InsideCartPrice[k] = item.price_grosze
                total += item.price_grosze * request.session[k+"q"]

        obj = Orders.objects.latest('id')
        order = Orders.objects.create(
            req_title = str(obj.id)+"543",
            price_grosze = total,
            product_container = dumps(InsideCart),
            product_ammounts = dumps(InsideCartQuantity),
            product_prices = dumps(InsideCartPrice),
           )
        order.save()
        return render(request, 'app/ORDER_TEMPLATE.html', {'order': order })