from django.contrib import admin
from .models import (
        Supplier_location,
        Supplier,
        Contract
        )

# Register your models here.
@admin.register(Supplier_location)
class Supplier_locationAdmin(admin.ModelAdmin):
    model = Supplier_location
    list_display = [ 
            'country',
            'city',
            'wereda',
            'kebela',
            'house_number',
            'Building_number',
            'slug',
            'created',
            'update',
        ]
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','created','update')

        return ()
    
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
    list_display = [ 
                'user',    
                'company',
                'contact_name',
                'phone',
                'email',
                'website',
                'supplier_location',
                'license_number',
                'license_states',
                'states',
                'slug',
                'created',
                'update',
            ]
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','created','update')

        return ()
    
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    model = Contract
    list_display = [ 
            'contract_code' ,
            'contract_plan',
            'date_of_acceptance' ,
            'date_of_expiration',
            'supplier',
            'contract_with', 
            'contract_status' ,
            'slug', 
            'created' ,
            'update' , 
            ]
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug','created','update')

        return ()   
      