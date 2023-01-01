from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import Product,Service
from django.db.models import Q

# Create your views here.
class ProductsListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'productList'
    paginate_by: 20
    
    def get_queryset(self):  # new
        searched_list = Product.objects.all()
        product_searched = self.request.GET.get("q")
        
        if product_searched != '' and product_searched is not None:
            searched_list = searched_list.filter( 
                Q(part_number__icontains=product_searched) | Q(product_name__icontains=product_searched))
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
                    Q(service_name__icontains=service_searched) | Q(part_number__icontains=service_searched))
                
            context = {'object_list':searched_list,}
           
            return redirect(request , 'products/product_search.html', context)
           
    """ model = Product
        template_name = ""

        def get_queryset(self):  # new
            query = self.request.GET.get("q")
            object_list = Product.objects.filter(
                Q(part_number__icontains=query) | Q(product_name__icontains=query)
            )
            if object_list:
                return object_list
            else:
                object_list = Service.objects.filter(
                    Q(service_name__icontains=query) | Q(part_number__icontains=query)
                )
                return object_list"""
        
            
    