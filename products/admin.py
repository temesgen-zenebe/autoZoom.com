from django.contrib import admin
from .models import (
        Descriptions,
        Brand,
        Category,
        Cost,
        Store,
        Picture,
        Product_information,
        Product_Stock,
        Service,
    )

    
@admin.register(Descriptions)
class DescriptionsAdmin(admin.ModelAdmin):
    model = Descriptions
    list_display = ['description','measurement','industry','application','instraction','warning','slug','created','update']
   
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','created','update')

        return ()
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = [
                    'brand',
                    'made_in',
                    'manufactured',
                    'slug',
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
    list_display = ['category','sub_category','slug','created','update',]   
    
    
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
    
@admin.register(Product_information)
class Product_informationAdmin(admin.ModelAdmin):
    model = Product_information
    list_display = ['name','part_number','category','description','slug','barcode','is_active','created','update']
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')
        return ()
    
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    model = Store
    list_display = ['supplier','branch','location_lick','contact_name','email','website','country','city','wereda_kebela','slug','created','update',]
   
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')
        return ()
    
@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    model = Picture
    list_display = ['picture','picture2','picture3','picture4','picture5','picture6','alt','slug','created','update',]
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created','update')
        return ()
    
    
@admin.register(Product_Stock)
class Product_StockAdmin(admin.ModelAdmin):
    model = Product_Stock
    search_fields = ['store', 'product']
    list_display = [
        'store',
        'product' , 
        'brand',
        'quantity',
        'picture',
        'cost', 
        'price',
        'off_price_parentage',
        'off_price', 
        'is_available' ,
        'shelf_number',
        'shipping',
        'tags',
        'label',
        'return_police',
        'product_states',
        'slug',
        'barcode',
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
        'service_number', 
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