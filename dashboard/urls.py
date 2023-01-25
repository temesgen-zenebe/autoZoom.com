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
    CategoryCreate,
    BrandCreate, 
    StoreCreate, 
    CostCreate,
    DescriptionsCreate,
    PictureCreate,
    ProductInformationCreate,
    productStockCreate, 
    StockDeleteView,
    )
from . import views   

app_name = 'dashboard' 

urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'), 
    path('dashboard/product_list/', ProductCreateView.as_view(), name='Product_create'),
    path('dashboard/product_list/', ProductListView.as_view(), name='Product_list'),
    path('dashboard/updated_category/<slug:slug>/', CategoryUpdateView.as_view(), name='updated_category'),
    path('dashboard/updated_store/<slug:slug>/', StoreUpdateView.as_view(), name='updated_store'),
    path('dashboard/updated_brand/<slug:slug>/', BrandUpdateView.as_view(), name='updated_brand'),
    path('dashboard/updated_picture/<slug:slug>/', PictureUpdateView.as_view(), name='updated_picture'),
    path('dashboard/updated_description/<slug:slug>/', DescriptionsUpdateView.as_view(), name='updated_description'),
    path('dashboard/updated_product/<slug:slug>/', ProductInformationUpdateView.as_view(), name='updated_product'),
    path('dashboard/updated_ProductStock/<slug:slug>/', ProductStockUpdateView.as_view(), name='updated_ProductStock'),
    path('dashboard/add_category/', CategoryCreate.as_view(), name='add_category'),
    path('dashboard/add_brand/', BrandCreate.as_view(), name='add_brand'),
    path('dashboard/add_store/', StoreCreate.as_view(), name='add_store'),
    path('dashboard/add_cost/', CostCreate.as_view(), name='add_cost'),
    path('dashboard/add_descriptions/', DescriptionsCreate.as_view(), name='add_descriptions'), 
    path('dashboard/add_productInformation/', ProductInformationCreate.as_view(), name='add_productInformation'),
    path('dashboard/add_picture/', PictureCreate.as_view(), name='add_picture'), 
    path('dashboard/add_productStock/', productStockCreate.as_view(), name='add_productStock'),
    path('dashboard/ManageProduct/', ManageProduct.as_view(), name='Manage-products'), 
    path('dashboard/delete_stack/<slug:slug>', StockDeleteView.as_view(), name='delete_stack'),
    #path('dashboard/ManageProduct/search/', views.search, 'search'),
]