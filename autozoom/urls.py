from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Admin
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    
    # User Management
    path('account/', include('users.urls')),
    path('account/', include('allauth.urls')),
    
    # Local Apps
    path('', include('pages.urls')),
    path('', include('products.urls')),
    path('', include('seller.urls')),
    path('', include('buyer.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 



