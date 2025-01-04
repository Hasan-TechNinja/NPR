from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registrationView, name='registration'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    
]
