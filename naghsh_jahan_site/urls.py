"""
URL configuration for naghsh_jahan_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from home_module.sitemaps import HomeSitemap  # ایمپورت نقشه سایت
from product_module.sitemaps import ProductSitemap
from category_module.sitemaps import CategorySitemap , BrandSitemap

sitemaps = {
    'home': HomeSitemap,  # ثبت sitemap صفحه اصلی
    'products': ProductSitemap,
    'categories': CategorySitemap,
    'brands': BrandSitemap,
}

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home_module.urls')),
    path('products/', include('product_module.urls')),
    path('contactus/', include('contact_module.urls')),
    path('account/', include('account_module.urls')),
    path('order/', include('order_module.urls')),
    path('panel/',include('user_panel_module.urls')),
    path('favorite/', include('favorite_module.urls')),
    path('site/', include('site_module.urls')),

    # site maps
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# In your main urls.py file
from django.conf.urls import handler404

handler404 = 'home_module.views.custom_404'  # If you create a custom view for the 404 error
