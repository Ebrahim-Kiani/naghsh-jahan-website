# Generated by Django 4.2.5 on 2024-08-18 20:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0009_user_code_posty_user_melli_code_alter_factors_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factors',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='تاریخ:'),
        ),
    ]
