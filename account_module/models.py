import os
import random
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from account_module.utils.sms_package import SMSHandler
from django.urls import reverse
from site_module.models import SiteSetting


class MyUserManager(BaseUserManager):
    def create_user(self, phone, is_staff=False, **extra_fields):
        if not phone:
            raise ValueError('The Phone number must be set')
        user = self.model(phone=phone, is_staff=is_staff, **extra_fields)
        if is_staff:
            user.set_password(extra_fields.get('password'))
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, full_name, password=None, **extra_fields):
        # Ensure 'phone_number' is included
        if not phone:
            raise ValueError('The Phone number must be set')

        # Create the user with provided parameters
        user = self.create_user(
            phone=phone,
            password=password,
            full_name=full_name,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **extra_fields
        )
        return user

    def get_by_natural_key(self, phone):
        return self.get(**{self.model.USERNAME_FIELD: phone})


def validate_length_10(value):
    try:
        int(value)
    except:
        raise ValidationError('کد پستی و کد ملی باید به عدد وارد شوند.')

    if len(value) != 10:
        raise ValidationError('طول کد پستی و کد ملی باید دقیقا ۱۰ رقم باشد.')

class User(AbstractBaseUser, PermissionsMixin):
    objects = MyUserManager()
    phone = models.CharField(max_length=11, null=True, blank=True, unique=True, verbose_name='تلفن:')
    full_name = models.CharField(max_length=40, null=True, blank=False, verbose_name='نام و نام خانوادگی:')
    is_active = models.BooleanField(default=False, verbose_name='آیا کاربر فعال است؟')
    is_staff = models.BooleanField(default=False, verbose_name='آیا کاربر کارمند است؟')
    address = models.TextField(null=True, blank=False, verbose_name='آدرس شما:')
    melli_code = models.CharField(max_length=10 , null=True, blank=False, verbose_name='کد ملی', validators=[validate_length_10])
    code_posty =  models.CharField(max_length=10 , null=True , blank=False, verbose_name='کد پستی بدون خط فاصله:', validators=[validate_length_10])
    is_completed = models.BooleanField(null=False, blank=True ,default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return str(self.phone)

class Factors(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='عنوان:')
    file = models.FileField(upload_to='files/factors', null=True, blank=True,verbose_name='فایل فاکتور:')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='کاربر:' , null=True)
    date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ:', default=timezone.now)
    code_factor = models.CharField(max_length=9,unique=True ,null=True, blank=False, verbose_name='کد فاکتور:')

    def __str__(self):
        return f'title: {self.title}, User: {self.user}'

    def send_sms(self):
        sms_object = SMSHandler(self.user.phone, self.code_factor)

        factor_download_url = reverse('factor-download', kwargs={'factor_id': self.id})
        main_setting = SiteSetting.objects.filter(is_main_setting=True).first()
        domain_name = main_setting.site_url
        factor_download_url = f'https://{domain_name}' +factor_download_url

        SMSHandler.send_factor_code(sms_object, factor_download_url, self.title)

    def save(self, *args, **kwargs):

        if self.file:
            try:
                this = Factors.objects.get(id=self.id)
                if this.file != self.file:
                    # If the logo has changed, delete the old one
                    if os.path.isfile(this.file.path):
                        os.remove(this.file.path)
            except Factors.DoesNotExist:
                pass  # No existing instance, so skip

            # File is being added or updated, update the date field with Shamsi date
            self.date = timezone.now()  # Current time in Gregorian

            success = False
            retry_limit = 5
            attempts = 0

            while not success and attempts < retry_limit:
                try:
                    self.code_factor = f'{random.randint(0, 999999999):09}'
                    super().save(*args, **kwargs)
                    success = True
                except:
                    attempts += 1

            if success:
                self.send_sms()
            else:
                raise Exception("we have error to send sms")

    def delete(self):

        # Delete the image file from the server
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete()

    class Meta:
        verbose_name = "فاکتور"
        verbose_name_plural = 'فاکتور ها'
