from django.urls import path
from .views import(
    HomePageView,
    AboutUsView,
    ContactUsView,
    TermsPolicesView,
    
    )

app_name = 'pages'

urlpatterns = [
  
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'), 
    path('terms-polices/', TermsPolicesView.as_view(), name='terms-polices'), 
    
]