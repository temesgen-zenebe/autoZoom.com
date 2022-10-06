from django.shortcuts import render
from django.views.generic import TemplateView
from seller.forms import SupplierProfileForm
from seller.models import Supplier
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView,TemplateView)
from django.views import View
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'
     
class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'
    
class TermsPolicesView(TemplateView):
    template_name = 'pages/terms_Polices.html'
    
class DashboardView(TemplateView):
    template_name = 'pages/dashboard.html'
    

    

