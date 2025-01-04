from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_size(image):
    max_size_kb = 1024
    if image.size > max_size_kb * 1024:
        raise ValidationError(f"Image size cannot exceed {max_size_kb} KB.")


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='Profile/', validators=[validate_size])

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='Brand')

    def __str__(self):
        return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
#     image = models.ImageField(upload_to='Product/', validators=[validate_size])
#     qr_code = models.ImageField(upload_to='QR code/', blank=True)

#     def __str__(self):
#         return self.name
    
def validate_size(image):
    max_size_kb = 1024
    if image.size > max_size_kb * 1024:
        raise ValidationError(f"Image size cannot exceed {max_size_kb} KB.")

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100, default=0)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')  # Better related_name
    image = models.ImageField(upload_to='Product/', validators=[validate_size])
    qr_code = models.ImageField(upload_to='QR_code/', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Custom logic (e.g., generate QR code) can be added here
        super().save(*args, **kwargs)

class Rating(models.Model):
    value = models.CharField(max_length=10)
    
    def __str__(self):
        return self.value
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    review_text = models.TextField(max_length=200)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, related_name='rating')
    vote = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product.name}, {self.rating}, {self.vote}'