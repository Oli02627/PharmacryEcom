from django.conf import settings
from .models import StaticPosts, SiteData
from cart.models import Cart

#Static-Page-Post
def staticposts(request):
    staticposts = StaticPosts.objects.all()
    return {"staticposts": staticposts}

#Footer Data
def sitedata(request):
    sitedata = SiteData.objects.all()[0]
    total_cart_item = 0
    if request.user.is_authenticated:
        total_cart_item = len(Cart.objects.filter(user=request.user))
    return {"sitedata": sitedata,'total_cart_item':total_cart_item}