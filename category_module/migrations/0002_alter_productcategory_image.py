# Generated by Django 4.2.5 on 2024-05-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(default='images/categories/category_default.png', upload_to='media/images/categories', verbose_name='تصویر دسته بندی'),
        ),
    ]
