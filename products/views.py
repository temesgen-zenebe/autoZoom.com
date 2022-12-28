from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import Product
from django.db.models import Q
# Create your views here.
class ProductsListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'productList'
    paginate_by: 20
    
    def get_queryset(self):
       # ordering = self.get_ordering()
        qs = Product.objects.all()
        
        if 'q' in self.request.GET: # Filter by search query
            q = self.request.GET.get('q') 
           # username = self.kwargs['username']
            #qs = qs.filter(Q(question__icontains=q) | Q(answer__icontains=q)| Q(user__username=username) )
            qs = qs.filter(Q(part_number__icontains=q) | Q(product_name__icontains=q))
        return qs.prefetch_related('category')
    
class ProductsDetailViews(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'productDetail'
    
