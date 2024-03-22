from django.contrib import admin
from . import models


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_filter = ['category', 'is_active']
    list_display = ['title','price', 'is_active', 'is_delete', 'Discount']
    list_editable = ['price', 'is_active', 'Discount']







admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductTag)

