from django.urls import path
from .views import * 
from .views import (ProductsListView , ProductsDetailViews,)

app_name = 'products'
urlpatterns = [
    path('product', ProductsListView.as_view(), name="product-list"),
    path('product/<slug:slug>', ProductsDetailViews.as_view(), name="product-detail"),
]