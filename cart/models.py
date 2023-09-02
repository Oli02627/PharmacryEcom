from http.client import ACCEPTED
from django.db import models
from numpy import product
from account.models import User, Customer
from products.models import Product, Color, Size

# Cart.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)
    
    @property 
    def total_cost(self):
        return self.quantity * self.product.selling_price
    @property 
    def total_shipping(self):
        return self.quantity * self.product.shipping_price

#statuc-Choices
STATUS_CHOICES = (
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),

)
#Place-Order
class PlaceOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=100, default="None", null=True)
    color = models.CharField(max_length=100, default="None", null=True)
    size = models.CharField(max_length=100, default="None", null=True)
    state = models.CharField(max_length=100, default="None", null=True)
    address = models.CharField(max_length=200, default="None", null=True)
    city = models.CharField(max_length=100, default="None", null=True)
    zip_code = models.IntegerField(default="123", null=True)
    phone = models.IntegerField(default = 123456789, null=True)
    order_price = models.FloatField(default=0 , null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default="Pending")
