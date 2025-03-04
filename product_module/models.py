import os
from sorl.thumbnail import delete
from django.db import models
from django.urls import reverse
from slugify import slugify
from category_module.models import ProductCategory,ProductBrand


# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    image = models.ImageField(upload_to='images/products'
                              ,null=False, blank=False, verbose_name='تصویر محصول')
    price = models.PositiveBigIntegerField(verbose_name='قیمت')
    Discount = models.PositiveSmallIntegerField(verbose_name='درصد تخفیف %', null=False, blank=True, default=0)
    final_price = models.PositiveIntegerField(verbose_name='قیمت پس از اعمال تخفیف', null=True, blank=True)
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(default="", db_index=True, max_length=200, unique=True
                            , verbose_name='عنوان در url')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE
                              , related_name='product_brand', blank=True, null=True)

    instagram_link = models.URLField(verbose_name='لینک اینستاگرام محصول', blank=True, null=True)
    whatsup_link = models.URLField(verbose_name='لینک واتساپ محصول', blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')
    is_featured = models.BooleanField(default=False, verbose_name='محصول ویژه است؟')
    is_sale = models.BooleanField(default=False, verbose_name='آیا برای فروش آنلاین است؟')


    def calculate_discount(self):
        if self.Discount == 0:
            return None
        else:
            discount_price = self.price - (self.price * (self.Discount/100))
        return discount_price

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if self.Discount ==0:
            self.final_price= self.price
        else:
            self.final_price = self.calculate_discount()
        self.slug = slugify(self.title)

        # Check if there's an existing instance of this model
        try:
            this = Product.objects.get(id=self.id)
            if this.image != self.image:
                # If the logo has changed, delete the old one
                if os.path.isfile(this.image.path):
                    os.remove(this.image.path)
        except Product.DoesNotExist:
            pass  # No existing instance, so skip
        super().save(*args, **kwargs)

    def delete(self):
        self.delete_thumbnails()
        # Delete the image file from the server
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete()
    def delete_thumbnails(self):
        delete(self.image)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_images')
    image = models.ImageField(upload_to='images/products')

    def __str__(self):
        return f"عنوان محصول: {self.product.title}, {self.image}"

    def delete(self):

        # Delete the image file from the server
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete()


    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصویرهای محصولات'

