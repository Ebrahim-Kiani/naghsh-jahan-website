# Generated by Django 4.2.5 on 2024-07-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0009_product_final_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False, verbose_name='آیا برای فروش آنلاین است؟'),
        ),
    ]
