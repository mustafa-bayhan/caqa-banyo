from django.urls import path
from . import views
urlpatterns=[
   
    path('',views.home, name='home'),
    path('about-us',views.about, name='about'),
    path('products',views.products, name='products'),
    path('catalog',views.catalog, name='catalog'),
    path('references',views.references, name='references'),
    path('contact-us',views.contact, name='contact'),
    path('products/<slug:slug>',views.product_detail, name='product_detail'),


]