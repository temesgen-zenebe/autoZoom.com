from cProfile import label
import email
from email.mime import application
from locale import currency
from unicodedata import category
from django.db import models
from django.conf import settings
from django.utils.timezone import datetime
from django.urls import reverse
from django.utils import timezone
from common.utils.text import unique_slug
from seller.models import Supplier
import barcode # additional imports
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
 
class Descriptions(models.Model):
    description = models.CharField(max_length=600,blank=True ,null=True)
    measurement = models.CharField(max_length=100,blank=True ,null=True)
    industry = models.CharField(max_length=300,blank=True ,null=True)
    application = models.CharField(max_length=300,blank=True ,null=True)
    instraction =  models.CharField(max_length=300,blank=True ,null=True)
    warning =  models.CharField(max_length=300,blank=True ,null=True)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
      return reverse('products:category_update', kwargs={'slug': self.slug})
  
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
          
    
    def __str__(self):
        return self.description

class Brand(models.Model):
    brand = models.CharField(max_length=100,blank=True ,null=True)
    made_in = models.CharField(max_length=100,blank=True ,null=True)
    manufactured = models.CharField(max_length=100,blank=True ,null=True)
    manufactured_date = models.DateField(auto_now_add=True, blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
      return reverse('products:category_update', kwargs={'slug': self.slug})
  
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
          
    def __str__(self):
        return self.brand

class Category(models.Model):
    category = models.CharField(max_length=100, blank=True ,null=True )
    sub_category = models.CharField(max_length=100, blank=True ,null=True )
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
      return reverse('dashboard:updated_category', kwargs={'slug': self.slug})
  
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
          
    def __str__(self):
        return self.category
    
class Cost(models.Model):
    CURRENCY = ((None, '--Please choose--'),('Birr', 'Birr'),('USD', 'USD'), ('Euro', 'Euro'),
        ('Yuan', 'Yuan'),('Dirham', 'Dirham'),)
    cost = models.DecimalField(decimal_places=2, max_digits=6,default = 1.00)
    currency = models.CharField(max_length=10, choices=CURRENCY)
    recite_number = models.CharField(max_length=50,blank=True ,null=True)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
      return reverse('products:category_update', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
        
    def __str__(self):
        return str(self.cost)

 
class Store(models.Model): 
    supplier = models.ForeignKey(Supplier ,on_delete=models.PROTECT , blank=True ,null=True )
    branch = models.IntegerField(default=1)
    location_lick = models.CharField(max_length=300 ,blank=True ,null=True )
    contact_name = models.CharField(max_length=300 ,blank=True ,null=True )
    email = models.EmailField(max_length=254 ,blank=True ,null=True )
    website = models.CharField(max_length=100, default="www.autoZoom.com", blank=True ,null=True )
    country = models.CharField(max_length=100, blank=True ,null=True )
    city = models.CharField(max_length=100, blank=True ,null=True )
    wereda_kebela = models.CharField(max_length=300, blank=True ,null=True )
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
      return reverse('products:category_update', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
        
    def __str__(self):
        return str(f'{self.supplier}-branch:{self.branch}')

class Picture(models.Model):
    picture = models.ImageField(upload_to="products/%Y/%m/%d" )
    picture2 = models.ImageField(upload_to="products/%Y/%m/%d" , blank=True)
    picture3 = models.ImageField(upload_to="products/%Y/%m/%d" , blank=True)
    picture4 = models.ImageField(upload_to="products/%Y/%m/%d" , blank=True)
    picture5 = models.ImageField(upload_to="products/%Y/%m/%d" , blank=True)
    picture6 = models.ImageField(upload_to="products/%Y/%m/%d" , blank=True)
    alt = models.CharField(max_length=100, blank=True ,null=True )
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
      return reverse('products:Picture_update', kwargs={'slug': self.slug})
  
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
  
    def __str__(self):
        return str(self.picture)
       
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    service_number = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.ForeignKey(Descriptions ,on_delete=models.CASCADE, blank=True,null=True )
    picture = models.ForeignKey(Picture ,on_delete=models.CASCADE, blank=True,null=True )
    price = models.DecimalField(decimal_places=2,max_digits=6, blank=True,null=True  )
    off_price_parentage = models.SmallIntegerField(blank=True , null=True)
    off_price = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    category = models.ForeignKey(Category ,on_delete=models.PROTECT, blank=True,null=True )
    supplier = models.ForeignKey(Supplier ,on_delete=models.PROTECT , blank=True ,null=True )
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    
    def get_absolute_url(self):
      return reverse('products:service-detail', kwargs={'slug': self.slug})
  
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        
        if self.tags == 'sell':
            self.off_price  = self.price - ((self.price * self.off_price_parentage)/100)
            
        super().save(*args, **kwargs)


    class Meta:
        ordering=("-service_name",) 
     
        
    def createdDate(self):
        self.created = timezone.now()
        self.save()
    
    def __str__(self):
        return self.service_name
    
  
class Product_information(models.Model):
    name = models.CharField(max_length=600,blank=True ,null=True)
    part_number = models.CharField(max_length=600,blank=True ,null=True)
    category = models.ForeignKey(Category ,on_delete=models.PROTECT,blank=True ,null=True)
    description = models.ForeignKey(Descriptions ,on_delete=models.CASCADE, blank=True,null=True )
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    barcode = models.ImageField(upload_to='barcodes/', blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
      return reverse('products:product-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs): # overriding save() 
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
            
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.name}', writer=ImageWriter()).write(rv)
        self.barcode.save(f'{self.name}.png', File(rv), save=False)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.name)
    
    
class Product_Stock(models.Model):
    TAGS = ( (None, '--Please choose--'),('sell', 'sell'),('Hot', 'Hot'),('Fast moving', 'Fast moving'), )
    LABEL = ((None, '--Please choose--'),('Bast seller', 'Bast seller'), ('AutoZoom Choice', 'AutoZoom Choice'),('New', 'New'),)
    RETURN_POLICE=((None, '--Please choose--'),('No Return', 'No Return'),('same day', 'same day'),('seven days', 'seven days')
                   ,('Fifteen(15) days', 'Fifteen(15) days'),('Thirty(30) days', 'Thirty(30) days'),)
    SHIPPING = ( (None, '--Please choose--'),('Free', 'Free'),('Not Free', 'Not Free')
                ,('on Stor pickup', 'on Stor pickup'),('Buy 5+ get free', 'Buy 5+ get free')
                ,('let you know on checkout', 'let you know on checkout'), )
    STATES = ((None, '--Please choose--'),('New Brand', 'New Brand'),('Used', 'Used'), 
              ('Refurnished', 'Refurnished'),('Open Box', 'Open Box'),)
    store = models.ForeignKey(Store ,on_delete=models.PROTECT ,default=1, blank=True ,null=True )
    product = models.ForeignKey(Product_information ,on_delete=models.CASCADE, blank=False,null=False,related_name="product" )
    brand = models.ForeignKey(Brand ,on_delete=models.CASCADE, blank=True,null=True )
    quantity = models.IntegerField(default=1)
    picture = models.ForeignKey(Picture ,on_delete=models.CASCADE, blank=True,null=True)
    cost = models.ForeignKey(Cost ,on_delete=models.CASCADE, blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=6, blank=True,null=True )
    off_price_parentage = models.SmallIntegerField(blank=True , null=True)
    off_price = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    shelf_number = models.CharField(max_length=50, null=True, blank=True)
    shipping = models.CharField(max_length=30, choices=SHIPPING ,blank=True, null=True)
    tags = models.CharField(max_length=30, choices=TAGS)
    label = models.CharField(max_length=30, choices=LABEL)
    return_police = models.CharField(max_length=30, choices=RETURN_POLICE) 
    product_states= models.CharField(max_length=30, choices=STATES)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    barcode = models.ImageField(upload_to='barcodes/', blank=True)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
      return reverse('products:product-detail', kwargs={'slug': self.slug})
  
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
            
        if self.tags == 'sell':
            self.off_price  = self.price - ((self.price * self.off_price_parentage)/100)
            
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.product}-{self.brand}', writer=ImageWriter()).write(rv)
        self.barcode.save(f'{self.product}-{self.brand}.png', File(rv), save=False)   
        
        super().save(*args, **kwargs)
    
    def createdDate(self):
        self.created = timezone.now()
        self.save()

    def __str__(self):
        return str(self.product)