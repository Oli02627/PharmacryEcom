from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart',views.add_to_cart, name='add_to_cart'),
    path('cartproducts',views.shop_cart, name='shop_cart'),
    path('pluscart',views.plus_cart, name='plus_cart'),
    path('minuscart',views.minus_cart, name='minus_cart'),
    path('removecart',views.remove_cart, name='remove_cart'),
    path('checkout',views.checkout, name='checkout'),
    path('paymentdone',views.payment_done, name='payment_done'),
    path('edit-address',views.editaddress, name='editaddress'),
    path('create-checkout-session',views.create_checkout_session, name='create_checkout_session'),
    path('order',views.order, name='order'),
    
    ] 