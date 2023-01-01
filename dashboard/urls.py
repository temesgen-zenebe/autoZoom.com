from django.urls import path
from .views import(
    DashboardView,
    ManageProduct,
    ProductInfoView,
    
    )
from . import views

app_name = 'dashboard'

urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'), 
    path('dashboard/ManageProduct/',ProductInfoView.as_view(), name='product_info'),
    path('dashboard/ManageProduct/', ManageProduct.as_view(), name='Manage-products'), 
    path('dashboard/ManageProduct/search/', views.search, 'search'),
]