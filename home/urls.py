from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductView.as_view(), name='index'),
    path('all-products',views.ProductAll.as_view(), name='allproduct'),
    path('contact',views.contact, name='contact'),
    path('search',views.search, name='search'),
    path('<str:slug>',views.staticpost, name='staticpost'),
]