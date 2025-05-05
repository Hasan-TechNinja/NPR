from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from . forms import BrandModelForm, ReviewModelForm
from . models import Brand, Category, Product, Review, Vote
from django.db.models import Q
from django.utils import timezone

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
        my_reviews = Review.objects.filter(product=product, active=True, user = request.user)
        others_review = Review.objects.filter(product=product, active=True).order_by('-created')
        total_reviews = len(my_reviews)
        form = ReviewModelForm()

        context = {
            'product': product,
            'my_review': my_reviews,
            'form': form,
            'total_reviews': total_reviews,
            'others_review': others_review
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
            form = ReviewModelForm()
            return redirect('pDetails', pk=product.pk)
    else:
        form = ReviewModelForm()

    context = {
        "product": product,
        "reviews": reviews,
        "form": form
    }
    return render(request, 'postreview.html', context)

def Helpful(request, pk):
    review = get_object_or_404(Review, id = pk)
    product = review.product
    for i in range(1):
        review.helpful = review.helpful + 1
        if review.not_helpful > 0:
            review.not_helpful = review.not_helpful - 1
        review.save()
        return redirect('pDetails', pk = product.id)

def NotHelpful(request, pk):
    review = get_object_or_404(Review, id = pk)
    product = review.product
    review.not_helpful += 1
    if review.helpful > 0:
        review.helpful -= 1
    review.save()
    return redirect('pDetails', pk = product.id)

def UpdateReview(request, pk):
    review = get_object_or_404(Review, id=pk)

    if request.method == "POST":
        form = ReviewModelForm(request.POST, instance=review)
        if form.is_valid():
            review_update = form.save(commit=False)
            review_update.user = request.user
            review_update.save()
            return redirect('pDetails', pk=review.product.id)
    else:
        form = ReviewModelForm(instance=review)

    context = {'form': form}
    return render(request, 'reviewUpdate.html', context)


def DeleteReview(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    product = review.product
    review.delete()
    return redirect('pDetails', pk=product.id)


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



def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            product = Product.objects.filter(
            Q(name__icontains=query) |
            Q(brand__name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(id__icontains=query)
)

            return render(request, 'search.html', {'product': product, 'query': query})
        else:
            return render(request, 'search.html', {'product': []})