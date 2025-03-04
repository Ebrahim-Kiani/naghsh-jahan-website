from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product

class ProductSitemap(Sitemap):
    priority = 0.8  # میزان اهمیت
    changefreq = "weekly"  # تغییرات هفتگی

    def items(self):
        return Product.objects.all()  # لیست تمام محصولات

    def location(self, item):
        return reverse('product-detail', args=[item.slug])  # ایجاد URL از slug


