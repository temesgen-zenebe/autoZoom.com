from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ( CreateView, DeleteView, DetailView, ListView, UpdateView,TemplateView)
from django.shortcuts import get_object_or_404
from .models import Supplier
from .forms import SupplierProfileForm

class SupplierCreateView(LoginRequiredMixin,CreateView):
    model = Supplier
    form_class = SupplierProfileForm 
    success_url = reverse_lazy('seller:list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

        
class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy('seller:list')
    
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
    
class SupplierUpdateView(UserPassesTestMixin, UpdateView):
    model = Supplier
    form_class = SupplierProfileForm
    
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class SupplierDetailView(DetailView):
    model = Supplier
      
class SupplierListView(ListView):
    model = Supplier
    
class SupplierProfileConfirmationThanksView(TemplateView):
    template_name = 'seller/confirmation.html'
    
class SellerDashboardView(TemplateView):
    template_name = 'seller/dashboard.html'
    
def supplier_detail(request, slug):
    supplier=get_object_or_404(Supplier, slug=slug) 
    return render(request,'pages/dashboard.html',{'supplier': supplier})