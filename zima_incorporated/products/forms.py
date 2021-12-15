
from django import forms
from . models import products

class ProductAddForm(forms.ModelForm):
    class Meta:
        model=products
        fields=["product_name", "publisher_name"]