# Generated by Django 4.2.5 on 2024-07-17 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0004_factors'),
    ]

    operations = [
        migrations.AddField(
            model_name='factors',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 17, 13, 9, 54, 523634, tzinfo=datetime.timezone.utc), verbose_name='date'),
        ),
    ]
