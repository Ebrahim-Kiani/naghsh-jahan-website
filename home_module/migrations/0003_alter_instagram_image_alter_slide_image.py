# Generated by Django 4.2.5 on 2024-05-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0002_alter_slide_content_alter_slide_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagram',
            name='image',
            field=models.ImageField(default='images/instagrams/insta-logo.png', upload_to='media/images/instagrams'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='media/images/slides', verbose_name='تصویر اسلایدر'),
        ),
    ]