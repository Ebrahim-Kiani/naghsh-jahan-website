from django.urls import path
from . import  views

urlpatterns = [
    path('our-service/', views.ServicesView.as_view(), name='our_service'),
    path('about-us', views.AboutUsView.as_view(), name='about_us')
]