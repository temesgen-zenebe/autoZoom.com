from multiprocessing.sharedctypes import Value
from random import choice
from string import digits
from django.db import models
from django.utils import timezone
from datetime import timedelta,datetime
from django.utils.timezone import now
from django.conf import settings
from common.utils.text import unique_slug
from django.urls import reverse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(
            message=f'{value} The contract expired; need renewed to use webapp.', code='past_date'
        )
        
def getUniqueCode():
    code = list()
    for i in range(9):
         code.append(choice(digits))
    return ''.join(code)


# Create your models here.
   
class Supplier_location(models.Model):
    country = models.CharField(max_length=100, blank=True ,null=True )
    city = models.CharField(max_length=100, blank=True ,null=True )
    wereda = models.CharField(max_length=100, blank=True ,null=True )
    kebela = models.CharField(max_length=100, blank=True ,null=True )
    house_number = models.CharField(max_length=100, blank=True ,null=True )
    Building_number = models.CharField(max_length=100, blank=True ,null=True )
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
      return reverse('seller:supplier_location_detail', kwargs={'slug': self.slug})
  
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.city

class Supplier(models.Model):
    LICENSE_STATES = ((None, '--Please choose--'),('active', 'active'),('pending', 'pending'), 
              ('suspended', 'suspended'),)
   
    BUSINESS_TYPE = ((None, '--Please choose--'),('Product', 'product'),('service', 'service'),)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='seller')
    company = models.CharField(max_length=100,blank=True ,null=True)
    contact_name = models.CharField(verbose_name="contact full Name", max_length=100,blank=True ,null=True)
    business_type = models.CharField(verbose_name="business type", max_length=30, default="product", choices=BUSINESS_TYPE)
    phone = models.CharField(max_length=15,blank=True ,null=True)
    email = models.CharField(max_length=100,blank=True ,null=True,help_text='A valid email address.')
    website = models.URLField(blank=True,null=True , validators=[URLValidator(schemes=['http', 'https'])])
    supplier_location = models.ForeignKey(Supplier_location ,on_delete=models.CASCADE , blank=True ,null=True )
    license_number = models.CharField(verbose_name="License Number",max_length=100,blank=True ,null=True)
    license_states = models.CharField(verbose_name="License States",max_length=30, choices=LICENSE_STATES)
    states = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
      return reverse('seller:detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
      
    def createdDate(self):
        self.created = timezone.now()
        self.save()
    
    def __str__(self):
        return self.company
    

class Contract(models.Model):
    CONTRACT_PLAN = ((None, '--Please choose--'),('yearly', 'yearly'),('3years', '3years'), ('5years', '5years'),) 
    CONTRACT_STATUS = ((None, '--Please choose--'),('active', 'active'),('pending', 'pending'), ('suspended', 'suspended'),)  
    
    contract_code = models.CharField(verbose_name="contract code", max_length=20, default= getUniqueCode, blank=False ,null=False)
    contract_plan = models.CharField(verbose_name="contract plan", max_length=30, default="yearly", choices=CONTRACT_PLAN)
    date_of_acceptance = models.DateField(auto_now_add=True, blank=True, null=True)
    date_of_expiration = models.DateField(verbose_name="contract expiration date", help_text = 'contract expiration date',validators=[validate_future_date])
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE)
    contract_with = models.CharField(max_length=100,default="autoZoom.inc")
    contract_status = models.CharField(max_length=30, default="pending", choices=CONTRACT_STATUS)  
    slug = models.SlugField(max_length=100, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True) 
    
    def get_absolute_url(self):
      return reverse('seller:contract_detail', kwargs={'slug': self.slug})                                   
   
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))   
            
        if self.contract_plan=="5years":
            self.date_of_expiration=now() + timedelta(days=1800)
            
        elif self.contract_plan=="3years":
            self.date_of_expiration=now() + timedelta(days=1080)
            
        else:
           self.date_of_expiration=now() + timedelta(days=360)
            
        super().save(*args, **kwargs)
        
    def createdDate(self):
        self.created = timezone.now()
        self.save()
    
    def __str__(self):
        return str(self.contract_code)