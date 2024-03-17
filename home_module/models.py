from django.db import models

# Create your models here.

class slide(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/slides')
    link = models.URLField(max_length=300)
    link_title = models.CharField(max_length=50)

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



