from django.urls import path
from . import views
urlpatterns = [
    path('my_account/', views.my_account, name='my_account'),
    path('cart/', views.user_cart, name='cart_view'),
    path('remove-order-detail', views.remove_order_detail, name='remove-order-detail'),
    path('change-order-detail', views.change_order_detail, name='change-order-detail'),
    path('wishlist/', views.user_wishlist, name='wishlist_view'),
    path('remove-wishlist/', views.user_wishlist_remove, name='remove_wishlist'),
    path('shops_list/', views.user_ShopListView.as_view(), name='shops_list'),
    path('shop_detail/<int:pk>/', views.user_ShopDetailView.as_view(), name='shop_detail')
]