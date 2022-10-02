from django.urls import path
from .views import HomePageView,AboutUsView,ContactUsView,TermsPolicesView ,DashboardView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'), 
    path('terms-polices/', TermsPolicesView.as_view(), name='terms-polices'), 
    path('dashboard/', DashboardView.as_view(), name='dashboard'), 
]