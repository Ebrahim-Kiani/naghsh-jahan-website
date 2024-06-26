# Generated by Django 4.2.5 on 2024-03-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='instagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=300)),
                ('image', models.ImageField(default='images/instagrams/insta-logo.png', upload_to='images/instagrams')),
            ],
            options={
                'verbose_name': 'پست اینستاگرام',
                'verbose_name_plural': 'پست های اینستاگرام',
            },
        ),
        migrations.CreateModel(
            name='slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='images/slides')),
                ('link', models.URLField(max_length=300)),
                ('link_title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'اسلاید',
                'verbose_name_plural': 'اسلاید ها',
            },
        ),
    ]
