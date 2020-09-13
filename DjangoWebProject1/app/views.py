"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic.list import ListView 
from json import dumps 

# relative import of forms 
from .models import Products 


from django.contrib import admin
admin.site.register(Products)


  
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
                string += InsideCart[k] + " " + str(InsideCartQuantity[k]) + " " + str(InsideCartPrice[k]) + " "
        InsideCart = dumps(InsideCart)
        InsideCartQuantity = dumps(InsideCartQuantity)
        InsideCartPrice = dumps(InsideCartPrice)
        return render(request, 'app/TEMPLATE_CART_VIEW.html', {'InsideCart': InsideCart, 'InsideCartQuantity': InsideCartQuantity, 'InsideCartPrice': InsideCartPrice })