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
users = settings.AUTH_USER_MODEL 

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    
class ManageProduct(TemplateView):
    template_name = 'dashboard/manageProduct.html'
    
class ProductInfoView(View):
    def get(self, request): 
        #seller = Supplier.objects.filter(Q(user = request.user) )
        #product_list = Product.objects.filter(Q(current_user = product)).order_by('-created')
        product_list = Product.objects.all()
        context = {'product_list':product_list}
        return render(request , 'dashboard/manageProduct.html',context=context)
    
    def post(self, request):
        pass
