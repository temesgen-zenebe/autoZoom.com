from django.shortcuts import render
from django.views.generic import TemplateView
from seller.forms import SupplierProfileForm
from seller.models import Supplier
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView,TemplateView)
from django.views import View
from django.db.models import Q
from django.conf import settings
# Create your views here.


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    
class ManageProduct(TemplateView):
    template_name = 'dashboard/manageProduct.html'
    
class ProductInfoView(View):
    def get(self, request): 
        product_list = Product.objects.all()
        
        context = {'product_list':product_list}
        return render(request , 'dashboard/manageProduct.html',context)
    
    def post(self, request):
        pass
    

""""
    def search(request):        
        if request.method == 'GET': # this will be GET now      
            search_product =  request.GET.get('search') # do some research what it does       
            try:
                product = Product.objects.filter(Q(part_number__icontains=search_product)) # filter returns a list so you might consider skip except part
                return render(request,"dashboard/manageProduct.html",{"product":product})
            except:
                return render(request,"dashboard/manageProduct.html",{'product':product})
        else:
            return render(request,"dashboard/manageProduct.html",{})"""
    
