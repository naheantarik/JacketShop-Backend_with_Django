from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):

    product = Product.all_product

    return render(request, 'index.html', {'products': product})