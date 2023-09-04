from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import redirect, render
from numpy import product
from cart.models import Cart, PlaceOrder
from products.models import Product, Color, Size
from django.db.models import Q
from account.models import User
from account.forms import EditUserAddressForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
import stripe
from django.conf import settings
import json
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    data = json.loads(request.body)
    total_amount = data['amount']
    total_amount = int(total_amount*100)
    base_url = request.build_absolute_uri('/')[:-1]  # Remove trailing slash
    success_url = f'{base_url}/cart/paymentdone'
    cancel_url = f'{base_url}/cart/checkout'
    print(total_amount)
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': 'Total Amount',
                    },
                    'unit_amount': total_amount, # in cents, meaning $20.00
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
            customer_email=request.user.email,
        )
        return JsonResponse({
            'id': session.id
        })
    return redirect('index')
#====add-to-cart================#
@login_required
def add_to_cart(request):
        user=request.user
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id = product_id)
        color_id = request.GET.get('color_id')
        size_id = request.GET.get('size_id')

        if color_id != None:
            color = Color.objects.get(id = color_id)
        else:
            color = None

        if size_id != None:
            size = Size.objects.get(id = size_id)
        else:
            size = None

        Cart(user=user, product=product, color=color, size=size).save()
        return redirect('shop_cart')
#====show-cart================#
@login_required
def shop_cart(request):
        user = request.user
        cart = Cart.objects.filter(user=user).order_by('-pk')
        amount = 0.0
        total_amount = 0.0
        summary_amount = 0.0
        summary_shipping = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]

        if cart_product:
            for p in cart_product:
                tempamount = p.quantity * (p.product.selling_price + p.product.shipping_price)
                amount += tempamount 
                total_amount =  amount 
                s_shipping = (p.quantity * p.product.shipping_price)
                summary_shipping += s_shipping
                s_amount = (p.quantity * p.product.selling_price)
                summary_amount +=s_amount
        return render(request, 'product/cart.html', {'cart':cart, 'totalamount':total_amount,'summary_shipping':summary_shipping,'summary_amount':summary_amount})


#==plus-cart=============#
@login_required
def plus_cart(request):
    if request.method == 'GET':
        cart_id = request.GET['cart_id']
        c = Cart.objects.get(Q(id=cart_id) & Q(user=request.user))
        c.quantity +=1
        c.save()
        amount = 0.0
        total_amount = 0.0
        summary_amount = 0.0
        summary_shipping = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        
        for p in cart_product:
            tempamount = p.quantity * (p.product.selling_price + p.product.shipping_price)
            amount += tempamount 
            total_amount =  amount
            s_shipping = (p.quantity * p.product.shipping_price)
            summary_shipping += s_shipping
            s_amount = (p.quantity * p.product.selling_price)
            summary_amount +=s_amount

        data = {
                'quantity': c.quantity,
                'amount': amount,
                'productprice': c.product.selling_price,
                'shippingprice': c.product.shipping_price,
                'total_amount':total_amount,
                'summary_shipping':summary_shipping,
                'summary_amount': summary_amount,

            }

        return JsonResponse(data)


#==minus-cart=============#
@login_required
def minus_cart(request):
    if request.method == 'GET':
        cart_id = request.GET['cart_id']
        c = Cart.objects.get(Q(id=cart_id) & Q(user=request.user))
        if c.quantity > 1:
            c.quantity -=1
            c.save()
        else:
            pass
        user = request.user
        amount = 0.0
        total_amount = 0.0
        summary_amount = 0.0
        summary_shipping = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        
        for p in cart_product:
            tempamount = (p.quantity * (p.product.selling_price + p.product.shipping_price))
            amount += tempamount 
            total_amount =  amount
            s_shipping = (p.quantity * p.product.shipping_price)
            summary_shipping += s_shipping
            s_amount = (p.quantity * p.product.selling_price)
            summary_amount +=s_amount

        data = {
                'quantity': c.quantity,
                'amount': amount,
                'productprice': c.product.selling_price,
                'shippingprice': c.product.shipping_price,
                'total_amount':total_amount,
                'summary_shipping':summary_shipping,
                'summary_amount': summary_amount,
            }

        return JsonResponse(data)


#==remove-cart=============#
@login_required
def remove_cart(request):
    if request.method == 'GET':
        cart_id = request.GET['cart_id']
        c = Cart.objects.get(Q(id=cart_id) & Q(user=request.user))
        c.delete()

        amount = 0.0
        total_amount = 0.0
        summary_amount = 0.0
        summary_shipping = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        
        for p in cart_product:
            tempamount = p.quantity * (p.product.selling_price + p.product.shipping_price)
            amount += tempamount 
            total_amount =  amount
            s_shipping = (p.quantity * p.product.shipping_price)
            summary_shipping += s_shipping
            s_amount = (p.quantity * p.product.selling_price)
            summary_amount +=s_amount

        data = {
                'total_amount':total_amount,
                'summary_shipping':summary_shipping,
                'summary_amount': summary_amount,
            }
        return JsonResponse(data)

#==Edit-Address========================#
@login_required
def editaddress(request):
        if request.method=="POST":
            fm = EditUserAddressForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                return redirect('checkout')
        else:
            fm = EditUserAddressForm(instance=request.user)
        return render(request,'product/addressedit.html',{'form':fm})

#====checkout================#
@login_required
def checkout(request):
        user = request.user
        cart_item = Cart.objects.filter(user = user).order_by('-pk')
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        total_amount = 0.0
        amount = 0.0
        summary_shipping = 0.0
        summary_amount = 0.0 

        for p in cart_product:
            tempamount = p.quantity * (p.product.selling_price + p.product.shipping_price)
            amount += tempamount 
            total_amount =  amount
            s_shipping = (p.quantity * p.product.shipping_price)
            summary_shipping += s_shipping
            s_amount = (p.quantity * p.product.selling_price)
            summary_amount +=s_amount

        return render(request, 'product/checkout.html',{'cart_item':cart_item, 'total_amount':total_amount, 'summary_amount':summary_amount, 'summary_shipping':summary_shipping })


#====order================#
@login_required
def payment_done(request):
    user = request.user
    name = user.first_name + user.last_name
    address = user.address
    state = user.state
    city = user.city
    zip_code = user.zip_code
    phone = user.phone
    cart = Cart.objects.filter(user=user)
    for c in cart:
        if c.color == None:
            color = "None"
        else:
            color = c.color.name

        if c.size == None:
            size = "None"
        else:
            size = c.size.name
        order_price = c.quantity * (c.product.selling_price + c.product.shipping_price)
        PlaceOrder(user=user, name=name, address=address, state=state, city=city, phone=phone, zip_code=zip_code, quantity=c.quantity, product=c.product, color=color,order_price=order_price, size=size).save()
        c.delete()
    return redirect('order')
#====order================#
@login_required
def order(request):
    user = request.user
    order = PlaceOrder.objects.filter(user=user).order_by('-pk')
    return render(request, 'product/order.html', {'order':order})
    

