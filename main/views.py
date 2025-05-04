from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from . forms import BrandModelForm, ReviewModelForm
from . models import Brand, Category, Product, Review, Vote

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
    
class BrandDetailsView(View):
    def get(self, request, pk):
        brand = Brand.objects.get(id = pk)
        product = Product.objects.filter(brand = brand, active = True)

        context = {
            'brand':brand,
            'product':product
        }
        return render(request, 'branddetails.html', context)
    
class ProductDetailsView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        reviews = Review.objects.filter(product=product, active=True)
        form = ReviewModelForm()

        context = {
            'product': product,
            'review': reviews,
            'form': form
        }
        return render(request, 'productdetails.html', context)
    
class CategoryDetails(View):
    def get(self, request, pk):
        category = Category.objects.get(pk = pk, active = True)
        product = Product.objects.filter(category=category)

        context = {
            'category':category,
            'product':product
        }
        return render(request, 'categorydetails.html', context)


def PostReview(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product, active=True)

    user_review = Review.objects.filter(product=product, user=request.user).first()

    if request.method == 'POST':
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.active = True
            review.save()
            form = ReviewModelForm()  # Clear form after submission
            return redirect('postReview', pk=product.pk)
    else:
        form = ReviewModelForm(instance=user_review)

    context = {
        "product": product,
        "reviews": reviews,
        "form": form
    }
    return render(request, 'postreview.html', context)


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