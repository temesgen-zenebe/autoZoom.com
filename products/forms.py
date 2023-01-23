from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from .models import Product_Stock,Category, Picture


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
        model = Product_Stock
        fields = (
                'store',
                'product' , 
                'brand',
                'quantity',
                'picture',
                'cost', 
                'price',
                'off_price_parentage',
                'is_available' ,
                'shelf_number',
                'shipping',
                'tags',
                'label',
                'return_police',
                'product_states',
                )
        widgets = {}
        

        