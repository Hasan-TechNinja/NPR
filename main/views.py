from django.shortcuts import render, redirect
from . forms import ProductForm
from . models import Product

# Create your views here.

def HomeView(request):
    return render(request, 'home.html')

def ProductView(request):
    data = Product.objects.all()
    print(data)
    context = {
        'data': data,
    }
    
    return render(request, 'product.html', context)


def ProductAdd(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('add_product')
    else:
        form = ProductForm
    
    context = {
        'form':form
    }
    return render(request, 'addproduct.html', context)