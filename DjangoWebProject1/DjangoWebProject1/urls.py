"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.views import ProductsList


urlpatterns = [
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('', ProductsList.as_view(), name='home'), 
    path('admin/', admin.site.urls),
    path('items/<str:item_name>/',views.render_items, name='item'),
    path('items/<str:item_name>/cart',views.add_to_cart_go_to_cart, name='cart'),
    path('cart/',views.view_cart, name='viewcart'),
    path('cart/order', views.order, name='order')
]
