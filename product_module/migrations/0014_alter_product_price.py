# Generated by Django 4.2.5 on 2024-09-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0013_remove_product_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveBigIntegerField(verbose_name='قیمت'),
        ),
    ]
