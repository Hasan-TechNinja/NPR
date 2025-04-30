from django.shortcuts import render, redirect
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