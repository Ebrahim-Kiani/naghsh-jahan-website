# Generated by Django 4.2.5 on 2024-07-25 10:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0005_factors_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factors',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date'),
        ),
    ]
