# Generated by Django 4.2.5 on 2024-05-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0008_alter_productimage_options_alter_productimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='final_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت پس از اعمال تخفیف'),
        ),
    ]
