from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import HomeSitemap  # ایمپورت نقشه سایت
from django.urls import include


sitemaps = {
    'home': HomeSitemap,  # ثبت sitemap صفحه اصلی
}
urlpatterns = [
    path('', views.home_index, name='home-page'),
]