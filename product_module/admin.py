from django.contrib import admin
from . import models


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_filter = ['category', 'is_active']
    list_display = ['title', 'price', 'is_active', 'is_delete', 'Discount']
    list_editable = ['price', 'is_active', 'Discount']


class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['url_title']


class ProductBrandAdmin(admin.ModelAdmin):
    readonly_fields = ['url_title']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand, ProductBrandAdmin)
