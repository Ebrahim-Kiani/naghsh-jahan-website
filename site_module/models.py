import os

from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=300, verbose_name='آدرس')
    address2 = models.CharField(max_length=300, verbose_name='آدرس2' , blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن')
    copy_right = models.TextField(verbose_name='متن کپی رایت سایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت')
    site_logo = models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')
    is_main_setting = models.BooleanField(max_length=200, verbose_name='تنظیمات اصلی')
    whatsapp_link = models.CharField(max_length=200, verbose_name='لینک واتساپ')
    instagram_link = models.CharField(max_length=200, verbose_name='لینک اینستاگرام')
    def delete(self):

        # Delete the image file from the server
        if self.image:
            if os.path.isfile(self.site_logo.path):
                os.remove(self.site_logo.path)
        super().delete()
    def save(self, *args, **kwargs):
        # Check if there's an existing instance of this model
        try:
            this = SiteSetting.objects.get(id=self.id)
            if this.site_logo != self.site_logo:
                # If the logo has changed, delete the old one
                if os.path.isfile(this.site_logo.path):
                    os.remove(this.site_logo.path)
        except SiteSetting.DoesNotExist:
            pass  # No existing instance, so skip

        super(SiteSetting, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title

class Ads(models.Model):
    text1 = models.CharField(max_length=100, verbose_name='متن اول')
    text2 = models.CharField(max_length=100, verbose_name='متن دوم')
    text3 = models.CharField(max_length=100, verbose_name='متن سوم')
    text4 = models.CharField(max_length=100, verbose_name='متن چهارم')
    text5 = models.CharField(max_length=100, verbose_name='متن پنجم')
    text6 = models.CharField(max_length=100, verbose_name='متن ششم')

    def __str__(self):
        return "تبلیغات"
    class Meta:
        verbose_name = 'تبلیغ بالای سایت'
        verbose_name_plural = 'تبلیغات بالای سایت'

class Service(models.Model):
    our_mission = models.TextField(verbose_name='ماموریت ما:')
    our_vision = models.TextField(verbose_name='دیدگاه ما:')
    our_philosophy = models.TextField(verbose_name='فلسفه ما:')
    we_are_trusted = models.TextField(verbose_name='به ما اعتماد کنید زیرا:')
    we_are_professional = models.TextField(verbose_name='ما حرفه ای هستیم زیرا:')
    our_stories = models.TextField(verbose_name='داستان ما:')

    class Meta:
        verbose_name = 'سرویس ما'
        verbose_name_plural = 'سرویس های ما'

class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='موضوع')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='images/about_us', verbose_name='تصویر درباره ما')

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره های ما'

    def __str__(self):
        return self.title