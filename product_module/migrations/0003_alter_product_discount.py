# Generated by Django 4.2.5 on 2024-03-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_product_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Discount',
            field=models.IntegerField(blank=True, null=True, verbose_name='درصد تخفیف %'),
        ),
    ]
