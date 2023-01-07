from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from .models import Product,category,Product_location,Stock_info, Picture


def validate_checked(value):
    if not value:
        raise ValidationError("Required.")
    
class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = (
                  'picture','picture2','picture3','picture4','alt'
                )
        widgets = {}
    
class ProductForm(forms.ModelForm):
    confirmation = forms.BooleanField(
        label = 'I certify that the information I have provided is true and i accept the terms.',
        validators=[validate_checked]
    )
    class Meta:
        model = Product
        fields = (
                'product_name' ,
                'part_number', 
                'brand',
                'description',
                'picture',
                'cost', 
                'tags',
                'price',
                'off_price_parentage',
                'off_price', 
                'available' ,
                'category',
                'stock_info', 
                'supplier',
                'label',
                'return_police',
                )
        widgets = {}
        

class ProductForm(forms.ModelForm):
    confirmation = forms.BooleanField(
        label = 'I certify that the information I have provided is true and i accept the terms.',
        validators=[validate_checked]
    )
    class Meta:
        model = Product
        fields = (
                'product_name' ,
                'part_number', 
                'brand',
                'description',
                'picture',
                'cost', 
                'tags',
                'price',
                'off_price_parentage',
                'off_price', 
                'available' ,
                'category',
                'stock_info', 
                'supplier',
                'label',
                'return_police',
                )
        widgets = {}
        