from django.urls import path
from .views import registrationView, loginView

urlpatterns = [
    path('register/', registrationView, name='registration'),
    path('login/', loginView, name='login'),
    
]
