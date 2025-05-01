from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from . forms import BrandModelForm
from . models import Brand, Category, Product, Review

# Create your views here.

class HomeView(View):
    def get(self, request):
        category = Category.objects.all()
        context = {
            'category':category
        }
        return render(request, 'home.html', context)

    
class BrandView(View):
    def get(self, request):
        form = BrandModelForm(request.POST)
        context = {
            'form':form
        }
        return render(request, 'create_brand.html', context)
    
    def post(self, request):
        form = BrandModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form':form
        }
        return render(request, 'create_brand.html')
    
def ProductDetails(request, pk):
    product = get_object_or_404(Product, pk = pk)
    context = {
        'product':product
    }
    return render(request, 'productdetails.html', context)


def BrandsView(request):
    brands = Brand.objects.all()
    context = {
        'brands':brands
    }
    return render(request, 'brands.html', context)


def CategoryView(request):
    category = Category.objects.all()
    context = {
        'categorys':category
    }
    return render(request, 'categorys.html', context)


def ProductView(request):
    products = Product.objects.all()
    context = {
        'product':products
    }
    return render(request, 'products.html', context)