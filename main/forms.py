from django import forms
from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        max_size_kb = 1024
        if image.size > max_size_kb * 1024:
            raise forms.ValidationError(f"Image size cannot exceed {max_size_kb} KB.")
        return image