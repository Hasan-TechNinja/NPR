from django.shortcuts import render, redirect, get_object_or_404
from . forms import ProductForm
from . models import Product
from django.views import View

# Create your views here.

def HomeView(request):
    return render(request, 'home.html')

def ProductView(request):
    data = Product.objects.all()
    context = {
        'data': data,
    }
    
    return render(request, 'product.html', context)


def ProductAdd(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm()
    
    context = {
        'form': form,
    }
    return render(request, 'addproduct.html', context)


class ProductDetails(View):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)

        context = {
            'product':product,
        }
        return render(request, 'productDetails.html', context)