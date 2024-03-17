from django.contrib import admin
from category_module.models import ProductCategory,ProductBrand


# Register your models here.
class ProductBrandAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductBrand, ProductBrandAdmin)
