# Generated by Django 4.2.5 on 2024-08-19 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0007_order_is_ordered_alter_order_is_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_ordered',
        ),
    ]
