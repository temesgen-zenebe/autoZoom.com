from django.contrib import admin
from .models import (
        Descriptions,
        Brand,
        Category,
        Cost,
        Product_location,
        Stock_info,
        Picture,
        Product,
        Service,
    )

    
@admin.register(Descriptions)
class DescriptionsAdmin(admin.ModelAdmin):
    model = Descriptions
    list_display = ['description','product_states','created','update',]
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')

        return ()
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = [
                    'brand',
                    'made_in',
                    'manufactured',
                    'created',
                    'update',
                ]
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')

        return ()
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['category','sub_category','created','update',]   
    
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')
        return ()
    
    
@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    model = Cost
    list_display = [ 'cost','currency','recite_number','slug','created','update',]
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')
        return ()
    
@admin.register(Product_location)
class Product_locationAdmin(admin.ModelAdmin):
    model = Product_location
    list_display = ['country','city','wereda','kebela','house_number','shelf_number','created','update',]
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')
        return ()
    
@admin.register(Stock_info)
class Stock_infoAdmin(admin.ModelAdmin):
    model = Stock_info
    list_display = ['quantity','Supplier','product_location','slug','created','update',]
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')
        return ()
    
@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    model = Picture
    list_display = ['picture','picture2','picture3','picture4','alt','created','update',]
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')
        return ()
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = [
        'product_name' ,
        'part_number', 
        'brand',
        'description',
        'picture',
        'cost', 
        'tags',
        'price',
        'off_price_parentage',
        'off_price', 
        'available' ,
        'category',
        'stock_info', 
        'label',
        'return_police',
        'slug',
        'created',
        'update', 
    ]
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','created','update')

        return ()
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = [
        'service_name' ,
        'part_number', 
        'brand',
        'description',
        'picture',
        'price',
        'off_price_parentage',
        'off_price', 
        'category',
        'supplier',
        'location',
        'contact',
        'available' ,
        'slug',
        'created',
        'update', 
    ]
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','created','update')

        return ()