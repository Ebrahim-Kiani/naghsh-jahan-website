# Generated by Django 4.2.5 on 2023-10-15 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLinkBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'دسته بندی لینک های فوتر',
                'verbose_name_plural': 'دسته بندی های لینک های فوتر',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200, verbose_name='نام سایت')),
                ('site_url', models.CharField(max_length=200, verbose_name='دامنه سایت')),
                ('address', models.CharField(max_length=300, verbose_name='آدرس')),
                ('address2', models.CharField(max_length=300, verbose_name='آدرس2')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='تلفن')),
                ('copy_right', models.TextField(verbose_name='متن کپی رایت سایت')),
                ('about_us_text', models.TextField(verbose_name='متن درباره ما سایت')),
                ('site_logo', models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')),
                ('is_main_setting', models.BooleanField(max_length=200, verbose_name='تنظیمات اصلی')),
                ('whatsapp_link', models.CharField(max_length=200, verbose_name='لینک واتساپ')),
                ('instagram_link', models.CharField(max_length=200, verbose_name='لینک اینستاگرام')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(max_length=500, verbose_name='لینک')),
                ('url_title', models.CharField(max_length=200, verbose_name='عنوان لینک')),
                ('description', models.TextField(verbose_name='توضیحات اسلایدر')),
                ('image', models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(max_length=500, verbose_name='لینک')),
                ('footer_link_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_module.footerlinkbox', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'لینک فوتر',
                'verbose_name_plural': 'لینک های فوتر',
            },
        ),
    ]