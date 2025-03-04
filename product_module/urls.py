from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap

urlpatterns = [

    path('', views.ProductListView.as_view(), name='product-list'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
    path('categories/<categories>', views.ProductListView.as_view(), name='product-category-list'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product-brand-list'),

]