from django.urls import path
from .views import(
    DashboardView,
    ManageProduct,
    ProductInfoView, 
    #ProductListView,
    #ProductCreateView,
    
    )
from . import views   

app_name = 'dashboard'  

urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'), 
    path('dashboard/ManageProduct/',ProductInfoView.as_view(), name='product_info'),
    #path('dashboard/ProductList/', ProductListView.as_view(), name='Product-list'),
    #path('dashboard/ProductList/', ProductCreateView.as_view(), name='Product-create'),
    path('dashboard/ManageProduct/', ManageProduct.as_view(), name='Manage-products'), 
    #path('dashboard/ManageProduct/search/', views.search, 'search'),
]