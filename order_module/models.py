from django.db import models
from django.contrib.auth import get_user_model
from product_module.models import Product


# Create your models here.
User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='آیا سفارش پرداخت شده است؟')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    grand_total = models.IntegerField(null=True, blank=True, verbose_name='مبلغ نهایی', default=0)
    def __str__(self):
        return str(self.id)

    def update_grand_total(self):
        self.grand_total = sum(detail.final_price for detail in self.orderdetail_set.all())
        self.save()  # Save the Order object to update the grand_total

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید کاربران'

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True,verbose_name='قیمت نهایی', default=0)
    count = models.SmallIntegerField(null=True, blank=True,verbose_name='تعداد')

    def save(self, *args, **kwargs):
        if self.count is not None and self.product is not None:
            self.final_price = self.count * self.product.final_price
        super().save(*args, **kwargs)
        self.order.update_grand_total()  # Call the update_grand_total method of the related Order object
    def __str__(self):
        return str(self.order.user)
    class Meta:
        verbose_name = 'جزئیات سبد خرید'
        verbose_name_plural = 'لیست جزئیات سبد خرید'
