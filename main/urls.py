from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('brandCr/', views.BrandView.as_view(), name='brand'),
    path('prodtls/', views.ProductDetailsView.as_view(), name='pDetails'),
    path('prodtls/<int:pk>', views.ProductDetailsView.as_view(), name='pDetails'),

    path('brands/', views.BrandsView, name='brands'),
    path('brandtls/<int:pk>', views.BrandDetailsView.as_view(), name="brandDetails"),
    path('category/', views.CategoryView, name='category'),
    path('catdetails/<int:pk>', views.CategoryDetails.as_view(), name="catdetails"),
    path('product/', views.ProductView, name='product'),
    path('postRev/<int:pk>', views.PostReview, name='postReview'),
    path('search/', views.search, name='search'),
    path('helpful/<int:pk>', views.Helpful, name='helpful'),
    
    path('nhelpful/<int:pk>', views.NotHelpful, name='nhelpful'),
    path('helpful/', views.Helpful, name='helpful'),
    path('rupdate/<int:pk>', views.UpdateReview, name='updatereview'),
    
    path('delete/<int:pk>', views.DeleteReview, name='delete'),
    path('delete/', views.DeleteReview, name='delete'),
]
