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
    phone = models.CharField(max_length=11, null=True, blank=True, unique=True)
    full_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='full name')
    is_active = models.BooleanField(default=False, verbose_name='is user active?')
    is_staff = models.BooleanField(default=False, verbose_name='is user staff?')
    address = models.TextField(null=True, blank=True, verbose_name='address')
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = 'Uesr'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.phone

class Factors(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='title')
    file = models.FileField(upload_to='files/factors', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False, verbose_name='date', default=timezone.now)

    def __str__(self):
        return f'title:{self.title}, User:{self.user.phone}'

    def save(self, *args, **kwargs):
        if self.file:
            # File is being added or updated
            self.date = timezone.now()  # Update the date field with the current timestamp
        super().save(*args, **kwargs)