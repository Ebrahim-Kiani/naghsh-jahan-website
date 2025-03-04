from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class HomeSitemap(Sitemap):
    priority = 1.0  # میزان اهمیت (۱ بالا‌ترین مقدار است)
    changefreq = "monthly"  # میزان تغییرات (روزانه)

    def items(self):
        return ['home-page']  # نامی که در urls.py ثبت شده است

    def location(self, item):
        return reverse(item)  # تولید آدرس URL
