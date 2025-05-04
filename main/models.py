from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, max_length=500)
    image = models.ImageField(upload_to="brand/", default='brand/default.png')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, max_length=500)
    image = models.ImageField(upload_to='category/', default='category/default.png')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='visitor/', blank=True, null=True)
    last_visit = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brands')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorys')
    description = models.TextField(blank=True, null=True, max_length=500)
    image = models.ImageField(upload_to="product/", default='product/default.png')
    rating = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    review = models.TextField(max_length=800)
    rating = models.PositiveIntegerField()
    helpful = models.PositiveIntegerField(default=0)
    not_helpful = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Review by {self.user} on {self.product.name} - Rating: {self.rating}"


class Vote(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='votes')
    reactor = models.ForeignKey(User, on_delete=models.CASCADE)
    positive = models.BooleanField(default=False)
    negative = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)


