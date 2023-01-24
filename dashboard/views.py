from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from seller.forms import SupplierProfileForm
from seller.models import Supplier
from products.models import Product_Stock,Category,Store,Product_information,Brand,Picture,Descriptions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView,TemplateView)
from django.views.generic.edit import UpdateView
from django.views import View
from django.db.models import Q
from django.conf import settings

# Create your views here.

from products.forms import ProductForm,PictureForm


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    
class ManageProduct(TemplateView):
    template_name = 'dashboard/manageProduct.html'
    
class ProductListView(ListView) :
    model = Product_Stock
    context_object_name = 'product_list'
    paginate_by = 10
    template_name = 'dashboard/manageProduct.html'
    
class ProductCreateView(CreateView):
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
                return redirect('dashboard:Product_create')
            form = ProductForm()
            context = {'form': form}
            return render(request, 'dashboard/manageProduct.html', context)
    
    
class CategoryUpdateView(UpdateView):
	model = Category
	fields = ["category","sub_category"]
	success_url ="/dashboard/product_list/"

            
class StoreUpdateView(UpdateView): 
	model = Store
	fields = ['supplier','branch','location_lick','contact_name','email','website','country','city','wereda_kebela']
	success_url ="/dashboard/product_list/"
 
class BrandUpdateView(UpdateView): 
	model = Brand
	fields = ['brand','made_in','manufactured']
	success_url ="/dashboard/product_list/"      

    
class PictureUpdateView(UpdateView): 
	model = Picture
	fields = ['picture','picture2','picture3','picture4','picture5','picture6','alt']
	success_url ="/dashboard/product_list/" 
 
class DescriptionsUpdateView(UpdateView): 
	model = Descriptions
	fields = ['description','measurement','industry','application','instraction','warning']
	success_url ="/dashboard/product_list/" 
 
class ProductInformationUpdateView(UpdateView): 
	model = Product_information
	fields = ['name','part_number','category','description','barcode','is_active']
	success_url ="/dashboard/product_list/" 
 
class ProductStockUpdateView(UpdateView): 
	model = Product_Stock
	fields = [ 
            'store',
            'product' , 
            'brand',
            'quantity',
            'picture',
            'cost', 
            'price',
            'off_price_parentage',
            'off_price', 
            'is_available' ,
            'shelf_number',
            'shipping',
            'tags',
            'label',
            'return_police',
            'product_states',
            'barcode'
          ]
	success_url ="/dashboard/product_list/" 