# Generated by Django 4.2.5 on 2024-08-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0011_alter_factors_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='factors',
            name='code_factor',
            field=models.CharField(max_length=6, null=True, unique=True, verbose_name='کد فاکتور:'),
        ),
    ]