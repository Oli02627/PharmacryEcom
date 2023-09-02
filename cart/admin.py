from django.contrib import admin
from .models import Cart, PlaceOrder

#Cart
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product','quantity']

# PlceOrder
@admin.register(PlaceOrder)
class PlaceOrderModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product','quantity','order_date','status']

