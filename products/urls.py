from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_collections, name='all_collections'),
    path('<str:category>/<str:permalink>',views.ProductDetailsView.as_view(), name='product_page'),
] 