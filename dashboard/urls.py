from django.urls import path
from .views import(
    
    DashboardView,
    ManageProduct
    )

app_name = 'dashboard'

urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'), 
    path('dashboard/ManageProduct/', ManageProduct.as_view(), name='Manage-products'), 
]