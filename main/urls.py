from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('product/', views.ProductView, name='product'),
    path('add/', views.ProductAdd, name='add_product'),
    path('pDetails/', views.ProductDetails.as_view(), name="pDetails"),
    path('pDetails/<int:id>', views.ProductDetails.as_view(), name='pDetails'),
]

