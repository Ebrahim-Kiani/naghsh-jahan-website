from django.urls import path
from . import views
urlpatterns = [
    path('', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('verify/', views.VerifyView.as_view(), name='verify')
]