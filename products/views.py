from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import Product

# Create your views here.
class ProductsListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'productList'
    paginate_by: 20
    
class ProductsDetailViews(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    
