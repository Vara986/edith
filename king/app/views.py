import re
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Destination
def index(request):
    dests=Destination.objects.all()
    return render(request, 'index.html', {'dests' :dests})
def shop(request):
    return render(request, 'shop.html')
def cart(request):
    return render(request, 'cart.html')
def checkout(request):
    return render(request, 'checkout.html')
def detail(request):
    return render(request, 'detail.html')
def contact(request):
    return render(request, 'contact.html')

