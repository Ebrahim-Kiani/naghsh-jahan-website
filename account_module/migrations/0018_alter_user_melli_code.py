# Generated by Django 4.2.5 on 2024-08-30 11:51

import account_module.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0017_alter_user_melli_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='melli_code',
            field=models.CharField(max_length=10, null=True, validators=[account_module.models.validate_length_10], verbose_name='کد ملی'),
        ),
    ]
