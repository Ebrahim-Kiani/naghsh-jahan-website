from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import ProductCategory, ProductBrand

class CategorySitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return ProductCategory.objects.all()

    def location(self, item):
        return reverse('product-category-list', args=[item.slug])

class BrandSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return ProductBrand.objects.all()

    def location(self, item):
        return reverse('product-brand-list', args=[item.slug])