from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
     path('shop',views.shop,name='shop'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('contact',views.contact,name='contact'),
    path('detail',views.detail,name='detail'),
   
    
]
