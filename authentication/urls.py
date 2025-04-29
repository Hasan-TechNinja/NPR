from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.LogoutView, name='logout'),
    path('login/', views.LoginView, name='login'),
    path('registration/', views.Registration, name='registration')
]
