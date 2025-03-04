# Generated by Django 4.2.5 on 2024-09-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0008_alter_ads_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='eitaa_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='لینک ایتا'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='roobika_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='لینک روبیکا'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='telegram_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='لینک تلگرام'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='لینک اینستاگرام'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='whatsapp_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='لینک واتساپ'),
        ),
    ]
