import random
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone

class MyUserManager(BaseUserManager):

    def create_user(self, phone_number, is_staff=False, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone number must be set')
        user = self.model(phone_number=phone_number, is_staff=is_staff, **extra_fields)
        if is_staff:
            user.set_password(extra_fields.get('password'))
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, full_name, password=None):

        user = self.create_user(

            phone=phone,

            password=password,

            full_name=full_name,

        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def get_by_natural_key(self, phone):
        return self.get(**{self.model.USERNAME_FIELD: phone})


class User(AbstractBaseUser, PermissionsMixin):
    objects = MyUserManager()
    phone = models.CharField(max_length=11, null=True, blank=True, unique=True, verbose_name='تلفن:')
    full_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='نام و نام خانوادگی:')
    is_active = models.BooleanField(default=False, verbose_name='آیا کاربر فعال است؟')
    is_staff = models.BooleanField(default=False, verbose_name='آیا کاربر کارمند است؟')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس شما:')
    melli_code = models.CharField(max_length=10 , null=True, blank=True, verbose_name='کد ملی:')
    code_posty =  models.CharField(max_length=10 , null=True , blank=True, verbose_name='کد پستی بدون خط فاصله:')


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر:')
    date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ:', default=timezone.now)
    code_factor = models.CharField(max_length=6, unique=True ,null=True, blank=False, verbose_name='کد فاکتور:')

    def __str__(self):
        return f'title: {self.title}, User: {self.user}'

    def save(self, *args, **kwargs):
        if self.file:
            # File is being added or updated, update the date field with Shamsi date
            self.date = timezone.now()  # Current time in Gregorian
            self.code_factor = f'{random.randint(0, 999999):06}'

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "فاکتور"
        verbose_name_plural = 'فاکتور ها'
