import os

from django.db import models

# Create your models here.

class slide(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    content = models.CharField(max_length=400, verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/slides', verbose_name='تصویر اسلایدر')
    link = models.URLField(max_length=300, verbose_name='لینک')
    link_title = models.CharField(max_length=50, verbose_name='عنوان لینک')
    def delete(self):

        # Delete the image file from the server
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete()
    def save(self, *args, **kwargs):
        # Check if there's an existing instance of this model
        try:
            this = slide.objects.get(id=self.id)
            if this.image != self.image:
                # If the logo has changed, delete the old one
                if os.path.isfile(this.image.path):
                    os.remove(this.image.path)
        except slide.DoesNotExist:
            pass  # No existing instance, so skip

        super(slide, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلاید ها'

class instagram(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=300)
    image = models.ImageField(upload_to='images/instagrams', default='images/instagrams/insta-logo.png')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'پست اینستاگرام'
        verbose_name_plural = 'پست های اینستاگرام'



