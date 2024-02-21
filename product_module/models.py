from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
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

    def __str__(self):
        return f'({self.title} - {self.url_title} )'

    def save(self, *args, **kwargs):
        self.url_title = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    price = models.IntegerField(verbose_name='قیمت')
    Discount = models.IntegerField(verbose_name='درصد تخفیف %', null=True)
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(default="", db_index=True, max_length=200, unique=True
                            , verbose_name='عنوان در url')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, related_name='product_brand')

    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def calculate_discount(self):
        discount_price = self.price - (self.price * (self.Discount/100))
        return discount_price

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.caption
