from django.contrib import admin
from . models import Brand, Category, Product, Review, Visitor

# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'name', 'description', 'image', 'created'
    )
admin.site.register(Brand, BrandAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'name', 'description', 'image', 'created',
    )
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'name', 'brand', 'category', 'description', 'image', 'rating', 'price'
    )
admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product', 'review', 'rating', 'vote_score', 'visitor', 'created'
    )
admin.site.register(Review, ReviewAdmin)


class VisitorAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'email', 'image', 'last_visit', 'created_at'
    )
admin.site.register(Visitor, VisitorAdmin)