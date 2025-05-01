from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('brandCr/', views.BrandView.as_view(), name='brand'),
    path('prodtls/<int:pk>', views.ProductDetails, name='pDetails'),

    path('brands/', views.BrandsView, name='brands'),
    path('category/', views.CategoryView, name='category'),
    path('product/', views.ProductView, name='product'),
]
