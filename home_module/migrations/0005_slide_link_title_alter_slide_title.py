# Generated by Django 4.2.5 on 2024-02-29 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0004_slide_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='link_title',
            field=models.CharField(default='Products', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slide',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]