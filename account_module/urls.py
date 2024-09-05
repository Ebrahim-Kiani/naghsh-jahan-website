from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify/', views.VerifyView.as_view(), name='verify'),
    path('resend/', views.resend_otp, name='resend'),
    path('logout/' , views.LogoutView, name='logout'),
    path('login_password/' , views.LoginPasswordView.as_view(), name='login_password')
]