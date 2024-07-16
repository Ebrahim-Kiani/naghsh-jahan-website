from django.urls import path
from . import views

urlpatterns = [
    path('add-to-wishlist/', views.add_wishlist, name='AddWishlist')
]