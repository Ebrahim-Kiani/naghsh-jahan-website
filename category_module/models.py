import os
from django.core.exceptions import ValidationError
from django.db import models
from slugify import slugify
from sorl.thumbnail import delete

# Create your models here.
class ProductBrand(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان')
    slug= models.CharField(max_length=100, db_index=True, verbose_name='عنوان در URL')
    is_active = models.BooleanField(verbose_name= 'فعال/غیرفعال')

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندهای محصولات'



class ProductCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان')
    slug = models.CharField(max_length=100, db_index=True, verbose_name='عنوان در URL', null=False, unique=True)
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / حذف نشده')
    parent_category = models.ForeignKey('self', blank=True, null=True, related_name='subcategories',
                                     on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/categories',
                              default='images/categories/category_default.png', verbose_name='تصویر دسته بندی')
    def delete(self):
        self.delete_thumbnails()
        # Delete the image file from the server
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete()
    def delete_thumbnails(self):
        delete(self.image)

    def clean(self):
        existing_categories = ProductCategory.objects.exclude(id=self.id)
        if existing_categories.filter(title=self.title).exists():
            raise ValidationError('A category with this title already exists.')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # Check if there's an existing instance of this model
        try:
            this = ProductCategory.objects.get(id=self.id)
            if this.image != self.image:
                # If the logo has changed, delete the old one
                if os.path.isfile(this.image.path):
                    os.remove(this.image.path)
        except ProductCategory.DoesNotExist:
            pass  # No existing instance, so skip
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
