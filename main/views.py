from django.shortcuts import render
from . forms import ProductForm

# Create your views here.

def HomeView(request):
    return render(request, 'home.html')

def ProductView(request):
    form = ProductForm
    
    context = {
        'form':form
    }
    return render(request, 'product.html', context)