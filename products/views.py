from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView
from django.views import View
from .models import Product,Service,Category,Brand
from django.db.models import Q
from .filters import ProductFilter   
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 


# Create your views here.

class ProductsListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'productList'
    paginate_by: 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["filter"] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context
    
    

    def get_queryset(self):  # new
        searched_list = Product.objects.all()
        product_searched = self.request.GET.get("q")
       
        if product_searched != '' and product_searched is not None:
            searched_list = searched_list.filter( Q(part_number__icontains=product_searched) | Q(product_name__icontains=product_searched))
         
        return searched_list     

class ProductsDetailViews(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'productDetail'

class ServiceListView(ListView):
    model = Service
    template_name = 'products/service_list.html'
    context_object_name = 'serviceList'
    paginate_by: 20
      
class ServiceDetailViews(DetailView):
    model = Service
    template_name = 'products/service_detail.html'
    context_object_name = 'serviceDetail'
    
class SearchResultsView(ListView):
    def get(self,request):
            searched_list = Product.objects.all()
            product_searched = self.request.GET.get("q")
            service_searched = self.request.GET.get("q")
            
            if product_searched != '' and product_searched is not None:
                searched_list = searched_list.filter( 
                    Q(part_number__icontains=product_searched) | Q(product_name__icontains=product_searched))
                
            if service_searched != '' and service_searched is not None:
                searched_list =  Service.objects.filter(
                    Q(service_name__icontains=service_searched) | Q(service_number__icontains=service_searched))
                
            context = {'object_list':searched_list,}
           
            return redirect(request , 'products/product_search.html', context)
           

      
        
            
    