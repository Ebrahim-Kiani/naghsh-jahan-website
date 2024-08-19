from django.contrib import admin
from order_module.models import Order, OrderDetail

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

class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_id','user', 'get_user_full_name','is_paid', 'payment_date', 'grand_total')
    search_fields = ('user__full_name', 'user__phone', 'id')  # Enable search by username and email fields of the user
    list_filter = ('is_paid', 'payment_date',)

    def get_user_full_name(self, obj):
        return obj.user.full_name
    def get_id(self, obj):
        return obj.id

    get_user_full_name.short_description = 'نام و نام خانوادگی کاربر:'
    get_id.short_description = 'شماره سبد خرید:'

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetail,OrderDetailAdmin)