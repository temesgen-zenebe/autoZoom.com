import django_filters 
from .models import Product_Stock


class ProductFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending','Descending')
        )
    ordering = django_filters.ChoiceFilter(
        label='Ordering' , 
        choices=CHOICES,
        method='filter_by_order'
        )
    
    
    class Meta:
        model = Product_Stock 
        fields = ('product', 'brand','tags')
        
    def filter_by_order(self, queryset,name ,value):
        expression = 'created' if value =='ascending' else '-created'
        return queryset.order_by(expression)