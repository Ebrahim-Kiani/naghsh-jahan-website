from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order/', views.add_product, name='add-product-to-order')
]