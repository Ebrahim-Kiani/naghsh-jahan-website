from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-favorite', views.AddProductFavorite.as_view(), name='product-favorite'),
    path('cat/<cat>', views.ProductListView.as_view(), name='product-category-list'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product-brand-list'),

]