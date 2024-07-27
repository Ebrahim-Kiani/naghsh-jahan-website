from django.contrib import admin
from . import models


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_filter = ['category', 'is_active']
    list_display = ['title','price', 'is_active', 'is_delete', 'Discount', 'is_sale']
    list_editable = ['price', 'is_active', 'Discount', 'is_sale']







admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductImage)
admin.site.register(models.ProductTag)

