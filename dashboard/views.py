from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from seller.forms import SupplierProfileForm
from seller.models import Supplier
from products.models import Product_Stock
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView,TemplateView)
from django.views import View
from django.db.models import Q
from django.conf import settings

# Create your views here.

from products.forms import ProductForm,PictureForm


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    
class ManageProduct(TemplateView):
    template_name = 'dashboard/manageProduct.html'
    
    
    

class ProductInfoView(CreateView, LoginRequiredMixin):   
    model = Product_Stock
    paginate_by = 10
    
    def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)
        
    def get(self, request): 
        #users = self.request.user
        form = ProductForm()
        #forms = inlineformset_factory(Supplier, Product, form )
        product_list = Product_Stock.objects.all()
    
        context = {'product_list':product_list,'form': form}
        return render(request , 'dashboard/manageProduct.html',context)
    
    def post(self, request):
         if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard:product_info')
            form = ProductForm()
            context = {'form': form}
            return render(request, 'dashboard/manageProduct.html', context)
            
        

    
         