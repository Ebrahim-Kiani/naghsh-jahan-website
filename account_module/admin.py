import jdatetime
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Factors
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationFormNoPassword
# Register your models here.
User = get_user_model()

# Optionally, you can customize the User admin as well to ensure it supports searching properly:
# Register the User model with custom search fields
class UserAdmin(BaseUserAdmin):
    form = UserCreationFormNoPassword
    add_form = UserCreationFormNoPassword
    add_form_template = 'admin/auth/user/add_form.html'
    list_display = ('phone', 'full_name', 'is_active', 'is_staff')
    search_fields = ('phone', 'full_name')
    ordering = ('-phone',)


    fieldsets = (
        (None, {'fields': ('phone', 'full_name', 'address', 'melli_code', 'code_posty', 'is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {'fields': ('phone', 'full_name', 'address', 'melli_code', 'code_posty', 'is_active', 'is_staff')}),
    )


# Register the User model with the admin
admin.site.register(User, UserAdmin)


@admin.register(Factors)
class FactorsAdmin(admin.ModelAdmin):
    list_display = ('code_factor','title', 'user', 'get_user_full_name', 'jalali_date')  # Display these fields in the list view
    search_fields = ('user__full_name', 'user__phone', 'code_factor','title')  # Enable search by username and email fields of the user
    autocomplete_fields = ['user']  # Enable search for the user field
    # Optionally, you can add filters and ordering:
    list_filter = ('date',)
    ordering = ('-date',)
    exclude = ['date', 'code_factor']

    # Custom method to display the user's full name
    def get_user_full_name(self, obj):
        return obj.user.full_name
    def jalali_date(self, obj):

        shamsi_date = jdatetime.datetime.fromgregorian(datetime=obj.date)
        return shamsi_date.strftime('%Y-%m-%d')

    # Set verbose name for the column
    get_user_full_name.short_description = 'نام و نام خانوادگی کاربر:'  # Label for the column
    jalali_date.short_description = 'تاریخ ثبت فاکتور:'