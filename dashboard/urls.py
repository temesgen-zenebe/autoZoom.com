from django.urls import path
from .views import(
    DashboardView,
    ManageProduct,
    ProductListView, 
    ProductCreateView,
    CategoryUpdateView,
    StoreUpdateView, 
    BrandUpdateView, 
    PictureUpdateView,
    DescriptionsUpdateView,
    ProductInformationUpdateView, 
    ProductStockUpdateView,
    )
from . import views   

app_name = 'dashboard' 

urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'), 
    path('dashboard/product_list/', ProductCreateView.as_view(), name='Product_create'),
    path('dashboard/updated_category/<slug:slug>/', CategoryUpdateView.as_view(), name='updated_category'),
    path('dashboard/updated_store/<slug:slug>/', StoreUpdateView.as_view(), name='updated_store'),
    path('dashboard/updated_brand/<slug:slug>/', BrandUpdateView.as_view(), name='updated_brand'),
    path('dashboard/updated_picture/<slug:slug>/', PictureUpdateView.as_view(), name='updated_picture'),
    path('dashboard/updated_description/<slug:slug>/', DescriptionsUpdateView.as_view(), name='updated_description'),
    path('dashboard/updated_product/<slug:slug>/', ProductInformationUpdateView.as_view(), name='updated_product'),
    path('dashboard/updated_ProductStock/<slug:slug>/', ProductStockUpdateView.as_view(), name='updated_ProductStock'),
    path('dashboard/product_list/', ProductListView.as_view(), name='Product_list'),
    path('dashboard/ManageProduct/', ManageProduct.as_view(), name='Manage-products'), 
    #path('dashboard/ManageProduct/search/', views.search, 'search'),
]