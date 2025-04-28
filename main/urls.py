from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('brandCr/', views.BrandView.as_view(), name='brand'),
]
