from django.shortcuts import render
from django.views import View
from products.models import Product, Size, Color
from cart.models import Cart
from django.db.models import Q
#====Product-page================#
def all_collections(request):
    pass

#====Product-page================#
class ProductDetailsView(View):
    def get(self, request, permalink, category):
        try:
            product = Product.objects.get( permalink= permalink )
            psize = Size.objects.filter(product=product)
            pcolor = Color.objects.filter(product=product)
            item_already_in_cart = None
            if request.user.is_authenticated:
                item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
            return render(request, 'product/product_page.html',{'product':product,'psize':psize,'pcolor':pcolor, 'item_already_in_cart':item_already_in_cart})
        except:
            return render(request, 'home/404.html')