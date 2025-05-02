from django import forms
from . models import Brand, Category, Product


class BrandModelForm(forms.ModelForm):
    class Meta:
        model = Brand
        exclude = ["user", "created", "status"]


# class ReviewModelForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = { 'review', 'rating', 'vote'}