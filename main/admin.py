from django.contrib import admin
from . models import Brand, Category, Product, Visitor, Review, Vote

# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'name', 'description', 'image', 'created', 'active'
    )
admin.site.register(Brand, BrandAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'name', 'description', 'image', 'created', 'active'
    )
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'name', 'brand', 'category', 'description', 'image', 'rating', 'price', 'active'
    )
admin.site.register(Product, ProductAdmin)

class VoteAdmin(admin.ModelAdmin):
    list_display = (
      'id', 'review', 'reactor', 'positive', 'negative', 'created'
    )
admin.site.register(Vote, VoteAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'product', 'review', 'rating', 'helpful', 'not_helpful', 'created', 'modified', 'active'
    )
admin.site.register(Review, ReviewAdmin)

class VisitorAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'email', 'image', 'last_visit', 'created_at'
    )
admin.site.register(Visitor, VisitorAdmin)