from django.contrib import admin
from order_module.models import Order, OrderDetail

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderDetail)