from django.shortcuts import render
from django.views.generic import TemplateView
from seller.forms import SupplierProfileForm
from seller.models import Supplier
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView,TemplateView)
from django.views import View
# Create your views here.

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    
class ManageProduct(TemplateView):
    template_name = 'dashboard/manageProduct.html'
