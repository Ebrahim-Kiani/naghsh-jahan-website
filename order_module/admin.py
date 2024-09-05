import jdatetime
from django.contrib import admin
from order_module.models import Order, OrderDetail, Notification


# Register your models here.




class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order','get_user','get_user_full_name','product', 'count', 'final_price')
    search_fields = ['order__id']  # Enable search by username and email fields of the user

    def get_user_full_name(self, obj):
        return obj.order.user.full_name
    get_user_full_name.short_description = 'نام و نام خانوادگی کاربر:'
    def get_user(self, obj):
        return obj.order.user
    get_user.short_description = 'شماره کاربر:'

    def get_id(self, obj):
        return obj.order.id

    get_id.short_description = 'شماره سبد خرید:'

    # Set verbose name for the column
    get_user_full_name.short_description = 'نام و نام خانوادگی کاربر:'  # Label for the column

class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_id','user', 'get_user_full_name','is_paid', 'is_ordered','jalali_payment_date','jalali_created_date', 'grand_total')
    search_fields = ('user__full_name', 'user__phone', 'id')  # Enable search by username and email fields of the user
    list_filter = ('is_paid',)
    ordering = ('payment_date','is_ordered')

    def get_user_full_name(self, obj):
        return obj.user.full_name
    def get_id(self, obj):
        return obj.id

    def jalali_payment_date(self, obj):
        if obj.payment_date:
            shamsi_date = jdatetime.datetime.fromgregorian(datetime=obj.payment_date)
            return shamsi_date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return None
    def jalali_created_date(self, obj):
        if obj.created_date:

            shamsi_date = jdatetime.datetime.fromgregorian(datetime=obj.created_date)
            return shamsi_date.strftime('%Y-%m-%d %H:%M:%S')

        else:
            return None

    # Set verbose name for the column
    get_user_full_name.short_description = 'نام و نام خانوادگی کاربر:'  # Label for the column
    jalali_payment_date.short_description = 'تاریخ پرداخت:'
    jalali_created_date.short_description = 'تاریخ ثبت سفارش:'
    get_id.short_description = 'شماره سبد خرید:'

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'is_read', 'jalali_date')
    def jalali_date(self, obj):

        shamsi_date = jdatetime.date.fromgregorian(date=obj.created_at)
        return shamsi_date.strftime('%Y-%m-%d')

    jalali_date.short_description = 'تاریخ ثبت پیام:'

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetail,OrderDetailAdmin)
admin.site.register(Notification, NotificationAdmin)
