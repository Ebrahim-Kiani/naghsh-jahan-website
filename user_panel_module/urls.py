from django.urls import path
from . import views
urlpatterns = [
    path('my_account/', views.my_account, name='my_account'),
    path('cart/', views.user_cart, name='cart_view'),
    path('remove-order-detail', views.remove_order_detail, name='remove-order-detail')
]