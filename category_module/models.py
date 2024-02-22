from django.db import models
from django.utils.text import slugify

# Create your models here.
class ProductBrand(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان در URL')
    is_active = models.BooleanField(verbose_name= 'فعال/غیرفعال')


    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندهای محصولات'



class ProductCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان در URL', null=False)
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / حذف نشده')
    parent_category = models.ForeignKey('self', blank=True, null=True, related_name='subcategories',
                                     on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.title} - {self.url_title} )'

    def save(self, *args, **kwargs):
        self.url_title = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
