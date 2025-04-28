from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="brand/")
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='category/')
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
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    description = models.TextField()
    image = models.ImageField(upload_to="product/")
    rating = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    review = models.TextField(max_length=500)
    rating = models.PositiveIntegerField()
    vote_score = models.IntegerField(default=0)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name}"