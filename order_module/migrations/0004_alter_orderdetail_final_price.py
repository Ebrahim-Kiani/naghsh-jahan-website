# Generated by Django 4.2.5 on 2024-07-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0003_alter_orderdetail_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='final_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='قیمت نهایی'),
        ),
    ]
