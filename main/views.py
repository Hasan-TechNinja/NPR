from django.shortcuts import render, redirect
from django.views import View
from . forms import BrandModelForm

# Create your views here.

class HomeView(View):
    def get(self, request):
        
        return render(request, 'home.html')

    
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