import django_filters 
from .models import Product


class ProductFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product 
        fields = ('product_name','part_number', 'brand','tags','category')
        
    