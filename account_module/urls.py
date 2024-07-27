from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('verify/', views.VerifyView.as_view(), name='verify'),
    path('resend/', views.resend_otp, name='resend')
]