from django.urls import path
from . import views
from .views import * 
from .views import(
    SupplierCreateView,
    SupplierDetailView,
    SupplierDeleteView,
    SupplierUpdateView, 
    SupplierListView,  
    SupplierProfileConfirmationThanksView,
    SellerDashboardView,
    )

app_name = 'seller' 

urlpatterns = [
    path('profile/<slug>/update/', SupplierUpdateView.as_view(), name='update'),
    path('profile/<slug>/delete/', SupplierDeleteView.as_view(), name='delete'),
    path('profile/create/', SupplierCreateView.as_view(), name='create'),
    path('profile/<slug:slug>/',views.supplier_detail,name='supplier_detail'),
    path('profile/<slug>/', SupplierDetailView.as_view(), name='detail'),
    path('profile/', SupplierListView.as_view(), name='list'),
    path('seller_dashboard/', SellerDashboardView.as_view(), name='dashboard'),
    path('profile_confirmation/', SupplierProfileConfirmationThanksView.as_view(), name='profile_confirmation'),
]